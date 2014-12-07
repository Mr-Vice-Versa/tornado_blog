 /*
Filename: EntryIndexCollection.js
Backbone EntryIndexCollection

(c) Vladyslav Ishchenko 12.2014
*/


'use strict';
define([
  'underscore',
  'backbone',
  'models/EntryModel',
  'backbone.paginator'],
  function(_, Backbone, EntryModel, PageableCollection){

      // Helpers
      var _parse = function(data){
        // Parse server response.
        if ( _.isObject(data.results) ) {
                return data.results;
            } else {
                return data;
            }
      };

      // EntryTitleModel Model
      var EntryIndexCollection = Backbone.PageableCollection.extend({
        model: EntryModel,
        url: '/entry',
        state: {
            pageSize: 5
        }
      });

      // Return the collection.
      return EntryIndexCollection;

});
