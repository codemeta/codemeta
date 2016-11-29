app = app || {};

var appView = new app.CheckView({ el: $("#search_container") });

requirejs.config({
 //By default load any module IDs from js/lib
 baseUrl: 'lib',
 //except, if the module ID starts with "app",
 //load it from the js/app directory. paths
 //config is relative to the baseUrl, and
 //never includes a ".js" extension since
 //the paths config could be for a directory.
 paths: {
     ajv: '../ajv/ajv.min'
 }
});
