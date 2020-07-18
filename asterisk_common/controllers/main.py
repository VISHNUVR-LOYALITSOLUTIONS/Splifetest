import logging
from odoo import http, SUPERUSER_ID, registry
from odoo.api import Environment
from werkzeug.exceptions import BadRequest

logger = logging.getLogger(__name__)


class AsteriskCommonController(http.Controller):

    def check_ip(self):
        allowed_ips = http.request.env[
            'asterisk_common.settings'].sudo().get_param(
            'permit_ip_addresses')
        if allowed_ips:
            remote_ip = http.request.httprequest.remote_addr
            if remote_ip not in [
                    k.strip(' ') for k in allowed_ips.split(',')]:
                raise BadRequest(
                    'Your IP address {} is not allowed!'.format(remote_ip))

    def _get_partner_by_number(self, db, number, country_code):
        # If db is passed init env for this db
        dst_partner_info = {'id': None}  # Defaults
        if db:
            try:
                with registry(db).cursor() as cr:
                    env = Environment(cr, SUPERUSER_ID, {})
                    dst_partner_info = env[
                        'res.partner'].sudo().get_partner_by_number(
                        number, country_code)
            except Exception:
                logger.exception('Db init error:')
                raise BadRequest('Db error, check Odoo logs')
        else:
            dst_partner_info = http.request.env[
                'res.partner'].sudo().get_partner_by_number(
                number, country_code)
        return dst_partner_info

    @http.route('/asterisk_common/get_caller_name', type='http', auth='none')
    def get_caller_name(self, **kw):
        self.check_ip()
        number = kw.get('number').replace(' ', '')  # Strip spaces
        country_code = kw.get('country')
        if not number:
            raise BadRequest('Number not specified in request')
        db = kw.get('db')
        logger.debug(
            'CALLER NAME REQUEST FOR NUMBER {} country {}'.format(
                number, country_code))
        dst_partner_info = self._get_partner_by_number(
            db, number, country_code)
        if dst_partner_info['id']:
            return dst_partner_info['name']
        return ''

    @http.route('/asterisk_common/get_partner_manager', auth='public')
    def get_partner_manager(self, **kw):
        self.check_ip()
        number = kw.get('number').replace(' ', '')  # Strip spaces
        country_code = kw.get('country')
        if not number:
            raise BadRequest('Number not specified in request')
        db = kw.get('db')
        dst_partner_info = self._get_partner_by_number(
            db, number, country_code)
        if dst_partner_info['id']:
            # Partner found, get manager.
            partner = http.request.env['res.partner'].sudo().browse(
                dst_partner_info['id'])
            if partner.user_id:
                # We have sales person set now let check if he has extension.
                if partner.user_id.asterisk_channel:
                    # We have user configured so let return his exten
                    result = partner.user_id.asterisk_channel
                    logger.info("Returning partner %s manager's channel %s",
                                partner.name, result)
                    return result
        return ''

    @http.route('/asterisk_common/get_caller_tags', auth='none', type='http')
    def get_caller_tags(self, **kw):
        self.check_ip()
        number = kw.get('number').replace(' ', '')  # Strip spaces
        country_code = kw.get('country')
        if not number:
            raise BadRequest('Number not specified in request')
        db = kw.get('db')
        dst_partner_info = self._get_partner_by_number(
            db, number, country_code)
        if dst_partner_info['id']:
            # Partner found, get manager.
            partner = http.request.env['res.partner'].sudo().browse(
                dst_partner_info['id'])
            if partner:
                return ','.join([k.name for k in partner.category_id])
        return ''
