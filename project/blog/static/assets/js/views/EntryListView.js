/*
Filename: EntryListView.js
Backbone EntryListView

(c) Vladyslav Ishchenko 12.2014
*/


'use strict';
define([
  'jquery',
  'underscore',
  'backbone',
  'views/EntryView'],
  function($, _, Backbone, EntryView){

      var EntryListView = Backbone.View.extend({
          // EntryList View for render a list of objects.

          tagName: 'div',

          initialize: function(){
              this.listenTo(this.collection, 'sync', this.render);
              //this.listenTo(this.collection, 'add', this.renderEntryView);
          },

          render: function() {
              console.log($(this.el)[0]);
              $(this.el).html('');
              this.collection.each(this.renderEntryView, this);
              return $(this.el).html();
          },

          renderEntryView: function(item) {
              var entryView = new EntryView({model: item});
              this.$el.append($(entryView.render()));
          },


    });
      // Returning instantiated views.
      return EntryListView;

});
