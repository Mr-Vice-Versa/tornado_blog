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
  'backbone.marionette',
  'views/EntryView'],
  function($, _, Backbone, Marionette, EntryView){

      var EntryListView = Backbone.Marionette.CompositeView.extend({

          tagName: 'div',

          initialize: function(){
              this.listenTo(this.collection, 'sync', this.render);
              //this.listenTo(this.collection, 'add', this.renderEntryView);
          },

          render: function() {
              $(this.el).html('');
              this.collection.each(this.renderEntryView, this);
              return $(this.el).html();
          },

          renderEntryView: function(item) {
              var entryView = new EntryView({model: item});
              this.$el.append($(entryView.render()));
          },


    });
      return EntryListView;

});
