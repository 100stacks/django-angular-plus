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


	/**
	*	@name Authentication
	*	@desc The Factory to be returned
	*/

	function Authentication($cookies, $http) {
		/**
		* 	@name Authentication
		* 	@desc The Factory to be returned
		*/

 		var Authentication = {
			register: register
		};

		return Authentication;


		//////////////////////////

		/**
		*	@name register
		*	@param Try to register a new user
		*	@param {string} username The username entered by the user
		* 	@param {string} password The password entered by the user
		* 	@param {string} email The email entered by the user
		* 	@returns {Promise}
		* 	@memberOf django-angular-plus.authentication.services.Authentication
		*/

		function register(email, password, username) {
			return $http.post('/api/v1/accounts' , { 
				username: username,
				password: password,
				email: email
			});
		}
	}
})();
