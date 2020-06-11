odoo.define('hide_document_download.DocumentViewer', function (require) {
"use strict";


var core = require('web.core');
var fieldRegistry = require('web.field_registry');
var session = require('web.session');
var dialogs = require('web.view_dialogs');
var Widget = require('web.Widget');
var DocumentViewer = require('mail.DocumentViewer');
var rpc = require('web.rpc');

var _t = core._t;
var qweb = core.qweb;

var core = require('web.core');
var Widget = require('web.Widget');


    var DocumentsviewController = DocumentViewer.include({


//    var user = session.user_id;



    events: _.extend({}, DocumentViewer.prototype.events, {

     'click .o_download_btn': '_onDownload',
    }),

//    custom_events: _.extend({}, DocumentViewer.prototype.custom_events, {
//
//        download: '_onDownload',
//
//    }),


    init: function (parent, attachments, activeAttachmentID) {
        this._super.apply(this, arguments);
        this.modelName = 'documents.document';
    },






        _onDownload: function(e){
//            var self =this
            var user = session.uid;

            if (user){

             rpc.query({
                                    model: 'documents.document',
                                    method: 'user_access',
                                    args:[['document_hide']],
                                })
                                .then(function(users_logged) {

                                 if (users_logged==false) {

//                                  $('.o_download_btn').addClass('oe_hidden');

//                                alert('download ')
 document.getElementById('secondaryDownload').style.visibility = 'hidden';

                                  $('.o_download_btn').css('visibility', 'hidden')

                                  $('#secondaryDownload').css('visibility', 'hidden')


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

    return DocumentsviewController;


});

