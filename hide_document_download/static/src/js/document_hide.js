
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


     init: function(parent, options) {

            var user = session.uid;

            if (user){

             rpc.query({
                                    model: 'res.users',
                                    method: 'user_access',
                                    args:[['document_hide']],
                                })
                                .then(function(users_logged) {

                                 if (users_logged==false) {

                                     $('.o_inspector_download').css('visibility', 'hidden')

                                 }
//                                 else{
//
//                                 this._super(parent, options);
//                                 }


                                })
                                }
        this._super(parent, options);
    },


    });

    return DocumentsController;





});
