 /*
Filename: EntryCollection.js
Backbone EntryCollection

(c) Vladyslav Ishchenko 12.2014
*/


'use strict';
define([
  'underscore',
  'backbone',
  'models/EntryModel'],
  function(_, Backbone, EntryModel){

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
      var EntryCollection = Backbone.Collection.extend({
        model: EntryModel,
        url: 'entry'
      });

      // Return the collection.
      return EntryCollection;

});
