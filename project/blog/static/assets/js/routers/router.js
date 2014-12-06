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
    'collections/EntryCollection',
    'views/EntryListView',
    'modernizr',
    'utils/utils'],
    function ($, _, Backbone, EntryCollection, EntryListView,
              Modernizr, utils) {

        // Blog Routers

        var BlogRouter = Backbone.Router.extend({
            routes: {
                '(?*query)': 'indexPage',
            },

            indexPage: function(query) {
                // indexPage
                console.log("indexPage");
                var entryCollection = new EntryCollection();
                var entryListView = new EntryListView({
                    el: $('[data-container=main]'),
                    collection: entryCollection
                });

                if (query) {
                    var queryData = utils.parseQueryString(query);
                    entryCollection.fetch({data: queryData});

                } else {
                    entryCollection.fetch(
                    );
                    console.log("indexPage.fetch");
                }

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
