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
        // href
        // utils.ajaxSetup();
        $(document).on('click', 'a[data-backbone=archive]', function(e) {
            console.log("click a[data-backbone=archive]");
            e.preventDefault();
            var href = $(e.currentTarget).attr('href');
            Backbone.history.navigate(href, { trigger: true });
        });

        Router.initialize();
      };

      return {
        initialize: initialize
      };


});
