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
  'backbone-forms',
  'models/EntryModel',
  'utils/utils',
  // Using the Require.js text! plugin, we are loaded raw text
  // which will be used as our views primary template.
  'text!templates/blog/entry_add.html'],
  function($, _, Backbone, Form, EntryModel, utils, entryAddViewTemplate){

      var EntryAddView = Backbone.View.extend({
            tagName: 'div',
            className: 'post-preview',

            initialize: function(){
                this.render();

            },

            events: {
                'click input[type=submit]': 'on_submit'
            },

            render: function(model) {
                var entryModel;
                if (typeof(model) !== "undefined") {
                    entryModel = model;
                }
                else{
                    entryModel = new EntryModel();
                };

                var form = new Backbone.Form({
                    template: _.template($(entryAddViewTemplate).html()),
                    model: entryModel
                }).render();

                $(this.el).html('').append(form.el);
                return this.$el;
            },

            on_submit: function(e){
                var newEntryModel = new EntryModel({
                    title: this.$('#text-EntryPost').val(),
                    markdown: this.$('#markdown-EntryPost').val()
                });

                newEntryModel.save(null, {success: _.bind(this.onSuccess, this),
                    error: this.onError });
            },

            onSuccess: function(model, response) {
                var href = response.id +'';
                href = "/entry/" + href;
                alert("Success Create New Post! " + href);
                Backbone.history.navigate(href, { trigger: true });
            },

            onError: function(model, response) {
                alert("Error, Post is not created!");
            }


        });
      // Returning instantiated views.
      return EntryAddView;

});
