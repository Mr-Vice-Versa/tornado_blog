/*
Filename: main.js

(c) Vladyslav Ishchenko 12.2014

*/


'use strict';
require.config({
	// The shim config allows us to configure dependencies for
	// scripts that do not call define() to register a module.
	shim: {
		underscore: {
			exports: '_'
		},
		backbone: {
			deps: [
				'underscore',
				'jquery'
			],
			exports: 'Backbone'
		},
        'backbone-relational': {
			deps: [
				'backbone',
			],
			exports: 'RelationalModel'
		},
        'modernizr': {
            exports: 'Modernizr'
        }
	},

	paths: {
		jquery: 'libs/jquery/jquery',
		underscore: 'libs/underscore/underscore',
		backbone: 'libs/backbone/backbone',
        'backbone-relational': 'libs/backbone-relational/backbone-relational',
		text: 'libs/requirejs-text/text',
        modernizr: 'libs/modernizr/modernizr'
	}
});



'use strict';
require([
    'jquery',
    'underscore',
    'backbone',
    'backbone-relational',
    'utils/utils',
	'initializer',
    ],
function ($, _, Backbone, RelationalModel, utils, App){
$(document).ready(function(){
    // Run selected app.
    App();

});
});
