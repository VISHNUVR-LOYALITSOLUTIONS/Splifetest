odoo.define('hide_document_download.DocumentsInspector', function (require) {
"use strict";

var core = require('web.core');
var fieldRegistry = require('web.field_registry');
var session = require('web.session');
var dialogs = require('web.view_dialogs');
var Widget = require('web.Widget');
var DocumentsInspector = require('documents.DocumentsInspector');
var rpc = require('web.rpc');

var _t = core._t;
var qweb = core.qweb;


    var DocumentsController = DocumentsInspector.include({


//    var user = session.user_id;

    events: _.extend({}, DocumentsInspector.prototype.events, {
        'click .o_inspector_download': '_onDownload',
    }),

    custom_events: _.extend({}, DocumentsInspector.prototype.custom_events, {

        download: '_onDownload',

    }),


     init: function(parent, options) {
        this.events["click .o_inspector_download"] = "_onDownload";
        this._super(parent, options);
    },



        _onDownload: function(){
//            var self =this
            var user = session.uid;

            if (user){

             rpc.query({
                                    model: 'res.users',
                                    method: 'user_access',
                                    args:[['document_hide']],
                                })
                                .then(function(users_logged) {

                                 if (users_logged==false) {

//                                  $('.o_inspector_download').addClass('oe_hidden');

                                  $('.o_inspector_download').css('visibility', 'hidden')

                                 }


//                                   if (users_logged==true) {
//
////                $('.btn fa fa-download o_inspector_button o_inspector_download').removeClass('oe_hidden');
////                $('.btn fa fa-download o_inspector_button o_inspector_download').show();
//                $('.o_inspector_download').css('visibility', 'visible')
////                $('.btn fa fa-download o_inspector_button o_inspector_download').css({"display":""});
////                this.$('.btn fa fa-download o_inspector_button o_inspector_download').removeClass('oe_hidden');
//
//            }else{
////                $('.btn fa fa-download o_inspector_button o_inspector_download').addClass('oe_hidden');
////                $('.btn fa fa-download o_inspector_button o_inspector_download').hide();
//                $('.o_inspector_download').css('visibility', 'hidden')
////                $('.btn fa fa-download o_inspector_button o_inspector_download').css({"display":"none"});
////               $('.btn fa fa-download o_inspector_button o_inspector_download').removeClass('hide');
//
//            }

                                })
                                }





        }

    });

    return DocumentsController;





});
