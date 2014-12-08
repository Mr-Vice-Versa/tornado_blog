/**
 File: utils.js
Set up XSRFToken token for POST for Tornado.

 Very IMPORTANT! line for Backbone Apps and Tornado XSRFToken (_xsrf):

    xhr.setRequestHeader("Content-type","application/x-www-form-urlencoded");

 (c) Vladyslav Ishchenko 12.2014, http://python-django.net
 */


'use strict';
define(
    ['jquery'],
    function( $ ){
        var utils = {};

        utils.parseQueryString = function( queryString ) {
            var params = {}, queries, temp, i, l;

            // Split into key/value pairs
            queries = queryString.split("&");

            // Convert the array of strings into an object
            for ( i = 0, l = queries.length; i < l; i++ ) {
                temp = queries[i].split('=');
                params[temp[0]] = temp[1];
            }

            return params;
        };

        // Set up CSRF token before app.initialize.
        utils.ajaxSetup = function(){
            // getCookie
            function getCookie(name) {
                var cookieValue = null;
                if (document.cookie && document.cookie != '') {
                    var cookies = document.cookie.split(';');
                    for (var i = 0; i < cookies.length; i++) {
                        var cookie = jQuery.trim(cookies[i]);
                        // Does this cookie string begin with the name we want?
                        if (cookie.substring(0, name.length + 1) == (name + '=')) {
                            cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                            break;
                        }
                    }
                }
                return cookieValue;
            };

            $.ajaxSetup({
                crossDomain: false,
                beforeSend: function(xhr, settings) {
                    var csrfSafeMethod = function(method) {
                        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
                    };
                    var csrftoken = getCookie('_xsrf');
                    console.log('getCookie', csrftoken);
                    if (!csrfSafeMethod(settings.type)) {
                       xhr.setRequestHeader("X-XSRFToken", csrftoken);
                       xhr.setRequestHeader("Content-type","application/x-www-form-urlencoded");
                    }
                }
            });
        };

        return utils;
    }
);
