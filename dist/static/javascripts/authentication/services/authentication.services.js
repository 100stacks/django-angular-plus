/**
*	Authentication
*	@namespace thinkster.authentication.services
*/

(function() {
	'use strict';
	angular 
		.module('django-angular-plus.authentication.services')
		.factory('Authentication', Authentication);

	Authentication.$inject = ['$cookies', '$http'];
})
