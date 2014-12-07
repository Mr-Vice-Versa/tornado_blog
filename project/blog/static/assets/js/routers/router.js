 /*
Filename: router.js
Backbone Blog Router

(c) Vladyslav Ishchenko 12.2014
*/


'use strict';
define([
    'jquery',
    'underscore',
    'backbone',
    'models/EntryModel',
    'collections/EntryIndexCollection',
    'collections/EntryCollection',
    'views/EntryDetailView',
    'views/EntryListView',
    'views/EntryAddView',
    'modernizr',
    'utils/utils'],
    function ($, _, Backbone, EntryModel, EntryIndexCollection, EntryCollection,
              EntryDetailView, EntryListView, EntryAddView, Modernizr, utils) {

        // Blog Routers

        var BlogRouter = Backbone.Router.extend({
            routes: {
                '': 'indexPage',
                'entry': 'entryList',
                'entry/:id': 'entryId',
                'entry/new/': 'entryAdd'
            },

            indexPage: function(){
                // indexPage 5 Entries.

                console.log("indexPage");
                var entryIndexCollection = new EntryIndexCollection();
                var entryListView = new EntryListView({
                    el: $('[data-container=main]'),
                    collection: entryIndexCollection
                });

                // sync data from server.
                entryIndexCollection.fetch();
            },

            entryId: function(id){
                // indexPage 5 get Entry by Id.

                console.log("entryId", id);
                var entryModel = new EntryModel({id: id});
                var entryDetailView = new EntryDetailView({
                    el: $('[data-container=main]'),
                    model: entryModel
                });
                // Get entry from server.
                entryModel.fetch();

            },

            entryList: function(){
                // entryList, all Entries without paginations.

                console.log("entryList");
                var entryCollection = new EntryCollection();
                var entryListView = new EntryListView({
                    el: $('[data-container=main]'),
                    collection: entryCollection
                });

                // sync data from server.
                entryCollection.fetch();
            },

            entryAdd: function(){
                // entryAdd, Add new Entries.

                console.log("entryAdd");
                var entryAddView = new EntryAddView({
                    el: $('[data-container=main]')
                });

            }

        });

        var initialize = function(){

            var blogRouter = new BlogRouter();

            // pushState Modernizr.
            Backbone.history.start({ pushState: Modernizr.history, silent: true });
            if(!Modernizr.history) {
                var rootLength = Backbone.history.options.root.length;
                var fragment = window.location.pathname.substr(rootLength);
                Backbone.history.navigate(fragment, { trigger: true });
            } else {
                Backbone.history.loadUrl(Backbone.history.getFragment());
            };

        };

        return {
            initialize: initialize
        };

});
