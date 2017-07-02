'use strict';
angular.module('u-ramos', ['ngMaterial']).config(function($interpolateProvider) {
    $interpolateProvider.startSymbol('{$');
    $interpolateProvider.endSymbol('$}');
});;