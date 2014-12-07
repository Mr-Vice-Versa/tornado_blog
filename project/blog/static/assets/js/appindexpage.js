 /*
Filename: appindexpage.js
Backbone Blog App

(c) Vladyslav Ishchenko 12.2014
*/


'use strict';
define([
  'jquery',
  'underscore',
  'backbone',
  'routers/router',
  'utils/utils'],

  function($, _, Backbone, Router, utils){
      var initialize = function(){
        utils.ajaxSetup();
        $(document).on('click', 'a[data-backbone=backbone]', function(e) {
            e.preventDefault();
            var href = $(e.currentTarget).attr('href');
            if (href === "/entry/new/"){
                Backbone.history.navigate(href, { trigger: true });
                Backbone.history.navigate("");
            }
            else{
                Backbone.history.navigate(href, { trigger: true });
            }

        });

        Router.initialize();
      };

      return {
        initialize: initialize
      };


});
