 #
    # @api.model
    # def _name_search(self, name, args=None, operator='ilike', limit=100, name_get_uid=None):
    #     args = args or []
    #     domain = []
    #     if name:
    #         domain = ['|', ('barcode', '=ilike', name + '%'), ('name', operator, name)]
    #         if operator in expression.NEGATIVE_TERM_OPERATORS:
    #             domain = ['&'] + domain
    #     bank_ids = self._search(domain + args, limit=limit, access_rights_uid=name_get_uid)
    #     return models.lazy_name_get(self.browse(bank_ids).with_user(name_get_uid))

    # def name_get(self):
    #     resi = super(Hremployee, self).name_get()
    #     res = []
    #     for field in self:
    #         res.append((field.id, '%s %s' % (field.name,(field.barcode))))
    #         # res.append((field.id, '%s' % field.name_seq))
    #         print(res)
    #     return res

    # @api.depends('name', 'barcode')
    # def name_get(self):
    #     res = super(Hremployee, self).name_get()
    #     result = []
    #     for rec in self:
    #         name = str(rec.barcode)
    #         result.append((rec.id, name))
    #     return result

# class HrWorkEntry(models.Model):
#     _inherit = 'hr.work.entry'
#
#     def name_search(self, name, args=None, operator='ilike', limit=100):
#         if not args:
#             args = []
#         if name:
#             args += ['|', '|', '|', ("barcode_one", operator, name), ("barcode_two", operator, name),
#                      ("barcode_three", operator, name), ("barcode_four", operator, name)]
#         return super(HrWorkEntry, self).name_search(name, args=args, operator=operator, limit=limit)
#
#     @api.onchange('employee_id')
#     def _onchange_barcode_scan(self):
#         product_rec = self.env['hr.employee']
#         product_ids = []
#         result = {}
#         if self.employee_id:
#             product = product_rec.search(['|',('name','like',self.employee_id.name),('barcode', '=', self.employee_id.barcode)])
#             if product:
#                 product_ids.append(product.id)
#
#             product_tmpl_ids = self.env['hr.employee'].search(['|',('name','like',self.employee_id.name),('barcode', '=', self.employee_id.barcode)])
#
#             for product_tmpl in product_tmpl_ids:
#                 product = product_rec.search([('product_tmpl_id', '=', product_tmpl.product_tmpl_id.id)])
#                 product_ids.append(product.id)
#             # if len(product_ids) == 1:
#             #     self.product_id = product_ids[0]
#             # else:
#             result['domain'] = {'employee_id': [('id', 'in', product_ids)]}
#
#             return result
#         else:
#             products = self.env['product.product'].search([]).ids
#             result['domain'] = {'product_id': [('id', 'in', products)]}
#
#             return result
#
#     def name_get(self):
#         res = super(HrWorkEntry, self).name_get()
#         data = []
#         for country in self:
#             display_value = ''
#             display_value += country.name or ""
#             display_value += ' ['
#             display_value += country.code or ""
#             display_value += ']'
#             data.append((country.id, display_value))
#         return data

# class HrPayslip(models.Model):
#     _inherit = 'hr.payslip'
#
#     def name_get(self):
#         res = super(HrPayslip, self).name_get()
#         data = []
#         for country in self:
#             display_value = ''
#             display_value += country.barcode or ""
#             display_value += ' ['
#             display_value += country.barcode or ""
#             display_value += ']'
#             data.append((country.id, display_value))
#         return data

    # def name_get(self):
    #     if not len(self.ids):
    #         return []
    #     resuhh = []
    #     product_name = []
    #     for record in self:
    #         if (record.ref) and (record.job):
    #             product_name = '[' + str(record.job) + ']' + '[' + str(record.ref) + ']'
    #             product_name += str(record.name)
    #             s = resuhh.append((record.id, product_name))
    #         elif record.ref:
    #             product_name = '[' + str(record.ref) + ']'
    #             product_name += str(record.name)
    #             s = resuhh.append((record.id, product_name))
    #         elif record.job:
    #             product_name = '[' + str(record.job) + ']'
    #             product_name += str(record.name)
    #             s = resuhh.append((record.id, product_name))
    #
    #         else:
    #             s = resuhh.append((record.id, record.name))
    #
    #     return resuhh

    # @api.model
    # def name_search(self, name, args=None, operator='ilike', limit=100):
    #     args = args or []
    #     recs = self.browse()
    #     if name:
    #         recs = self.search((args + ['|', ('ref', 'ilike', name), ('barcode', 'ilike', name)]),
    #                            limit=limit)
    #     if not recs:
    #         recs = self.search([('name', operator, name)] + args, limit=limit)
    #     return recs.name_get()

