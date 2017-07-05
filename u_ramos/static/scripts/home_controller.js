'use strict';
angular.module('u-ramos').controller('AppCtrl',function ($scope, $timeout, $mdSidenav, $log,$http) {
    $scope.toggleLeft = buildDelayedToggler('left');
    $scope.progressStatus =  true;
    var self = this;

    var init = function() {
      self.selectedProfesItem = null;
      self.searchTextProfes = null;
      self.selectedProfesTags = [];
      self.selectedRamosItem = null;
      self.searchTextRamos = null;
      self.selectedRamosTags = [];
    };
    init()
    self.selectedItemChange = function(item){
      if(typeof item != 'undefined'){
        $scope.toggleLeft();
        $scope.progressStatus= true;
        
        return $http.get('ramo_profe/?name_profe=' + (self.selectedProfesItem ? self.selectedProfesItem : '') + '&name_ramo=' + (self.selectedRamosItem ? self.selectedRamosItem : '')).then(function(response) {
          console.log(response.data);
          $scope.progressStatus= false;
          return response.data.results;
        });
      }
    };
    self.querySearchProfesores = function(query) {
      return $http.get('profesores/autocomplete/?q=' + query).then(function(response) {
        return response.data.results;
      });
    };

    self.querySearchRamos = function(query) {
      return $http.get('ramos/autocomplete/?q=' + query).then(function(response) {
        return response.data.results;
      });
    };

    /**
     * Supplies a function that will continue to operate until the
     * time is up.
     */
    function debounce(func, wait, context) {
      var timer;

      return function debounced() {
        var context = $scope,
            args = Array.prototype.slice.call(arguments);
        $timeout.cancel(timer);
        timer = $timeout(function() {
          timer = undefined;
          func.apply(context, args);
        }, wait || 10);
      };
    }

    /**
     * Build handler to open/close a SideNav; when animation finishes
     * report completion in console
     */
    function buildDelayedToggler(navID) {
      return debounce(function() {
        // Component lookup should always be available since we are not using `ng-if`
        $mdSidenav(navID)
          .toggle()
          .then(function () {
            $log.debug("toggle " + navID + " is done");
          });
      }, 200);
    }

    function buildToggler(navID) {
      return function() {
        // Component lookup should always be available since we are not using `ng-if`
        $mdSidenav(navID)
          .toggle()
          .then(function () {
            $log.debug("toggle " + navID + " is done");
          });
      };
    }
  })
  .controller('LeftCtrl', function ($scope, $timeout, $mdSidenav, $log) {
    $scope.close = function () {
      // Component lookup should always be available since we are not using `ng-if`
      $mdSidenav('left').close()
        .then(function () {
          $log.debug("close LEFT is done");
        });

    };

  })
