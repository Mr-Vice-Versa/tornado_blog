/*
File: initializer.js
Backbone Apps initializer

(c) Vladyslav Ishchenko 12.2014
* */


'use strict';
define([
  'jquery',
  'appindexpage'],
  function($, appIndexPage){

      var runApp = function() {

          // Blog Index page App.
          $('container').ready(function() {
              var runApp = appIndexPage.initialize();
              return runApp;
          });

          // Next app here.

      }

      return runApp;
});
