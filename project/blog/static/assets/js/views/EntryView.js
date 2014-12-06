/*
Filename: EntryView.js
Backbone EntryView

(c) Vladyslav Ishchenko 12.2014
*/


'use strict';
define([
  'jquery',
  'underscore',
  'backbone',
  // Using the Require.js text! plugin, we are loaded raw text
  // which will be used as our views primary template.
  'text!templates/blog/entry.html'],
  function($, _, Backbone, entryTemplate){

      var EntryView = Backbone.View.extend({
            // EntryView for render one instance object.
            tagName: 'div',
            className: 'post-preview',

            initialize: function(options){
                // For chose template for Entry when render it.
                this.listenTo(this.model, 'add', this.render);
            },

            template: _.template($(entryTemplate).html()),

            render: function() {
                // Pas to template entry variable.
                console.log("EntryView.render")
                var data = {entry: this.model.toJSON()};
                // Render Entry template.
                $(this.el).html(this.template(data));
                return this.$el;

            }

        });
      // Returning instantiated views.
      return EntryView;

});
