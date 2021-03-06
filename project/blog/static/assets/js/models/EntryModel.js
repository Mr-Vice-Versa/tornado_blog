/*
Filename: EntryModel.js
Backbone EntryModel

(c) Vladyslav Ishchenko 12.2014, http://python-django.net
*/


'use strict';
define([
  'underscore',
  'backbone'],
  function(_, Backbone){

      // Helpers
      var _parse = function(data){
        // Parse server response.
        if ( _.isObject(data.results) ) {
                return data.results;
            } else {
                return data;
            }
      };

      // EntryModel Model
      var EntryModel = Backbone.Model.extend({
        urlRoot: '/entry',
        idAttribute: 'id',

        // For Backbone.Form
        schema: {
            id:         'Text',
            author_id:  'Text',
            slug:       'Text',
            title:      'Text',
            markdown:   'Text',
            html:       'Text',
            published:  'Text',
            updated:    'Text'
        }
    });

  return EntryModel;


});
