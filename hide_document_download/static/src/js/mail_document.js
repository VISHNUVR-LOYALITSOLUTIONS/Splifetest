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


    init: function (parent, attachments, activeAttachmentID) {

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

// <button id="secondaryDownload" class="secondaryToolbarButton download visibleMediumView" title="Download" tabindex="54" data-l10n-id="download">
//              <span data-l10n-id="download_label">Download</span>
//            </button>


                                  $('.o_download_btn').css('visibility', 'hidden')


                                 }

//                                 else{
//
//                                 this._super.apply(this, arguments);
//                                 }
//
                                })
                                }


        this._super.apply(this, arguments);
        this.modelName = 'documents.document';
    },


    });

    return DocumentsviewController;


});

