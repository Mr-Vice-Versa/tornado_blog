/*
Filename: EntryDetailView.js
Backbone Entry Detail View

(c) Vladyslav Ishchenko 12.2014
*/


'use strict';
define([
  'jquery',
  'underscore',
  'backbone',
  'backbone.marionette',
  // Using the Require.js text! plugin, we are loaded raw text
  // which will be used as our views primary template.
  'text!templates/blog/entry_detail.html'],
  function($, _, Backbone, Marionette, entryDetailTemplate){

      var EntryDetailView = Backbone.Marionette.ItemView.extend({
            tagName: 'div',
            className: 'post-preview',

            initialize: function(options){
                this.listenTo(this.model, 'change', this.render);
            },

            template: _.template($(entryDetailTemplate).html()),

            render: function() {

                var data = {entry: this.model.toJSON()};
                $(this.el).html(this.template(data));
                return this.$el;

            }

        });
      return EntryDetailView;

});
