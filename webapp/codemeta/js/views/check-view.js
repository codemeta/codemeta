
var app = app || {};

	app.CheckView = Backbone.View.extend({

   initialize: function(){
       //this.render();
			 //var Validator = require('jsonschema').Validator;
				//var v = new Validator();
				//var instance = 4;
				//var schema = {"type": "number"};
				//console.log(v.validate(instance, schema));
   },
   render: function(){
       // Compile the template using underscore
       var template = _.template( $("#search_template").html(), {} );
       // Load the compiled HTML into the Backbone "el"
       this.$el.html( template );
   },
   events: {
       //"click input[type=button]": "doValidate"
       "click #validate_button": "doValidate",
       "click #clear_button": "doClear",
       //"click #copy_button": "doCopy"
   },
   doValidate: function( event ) {
		 console.log("doValidate")
		 var valid;
			 $("#results_container").css('visibility', 'visible')
			 try {
         data = JSON.parse($("#codemeta_document").val());
		   } catch (err) {
					 $("#check_result").html("Error parsing the CodeMeta document: " + err.message);
					 return
		   }

			   ajv = new Ajv();
				 try {
					 var valid = ajv.validate(codemetaSchema, data);
			   } catch (err) {
					 $("#check_result").html("Error validating the CodeMeta document: " + err.message);
					 return
  			 }

         if (valid) {
					 $("#check_result").html("The CodeMeta document is valid.");
				 } else {
					 $("#check_result").html("Error validating the CodeMeta document: " + ajv.errorsText());
				 }
		   //});
       //schema = JSON.parse(File.read('./lib/codemeta-json-schema.json'))
			 /*
			 require(['tv4'], function (tv4) {
					$("#results_container").css('visibility', 'visible')
					try {
			        valid = tv4.validate(JSON.parse(data), codemetaSchema);
				  } catch (err) {
					    $("#check_result").html("Error validating the CodeMeta document: " + err.message);
							return
					};
					if (valid) {
					    $("#check_result").html("The CodeMeta document is valid.");
					} else {
					  $("#check_result").html("The CodeMeta document is not valid. The following errors occured: " + tv4.error);
					};
       });
			 */
   },

	 doClear: function( event ) {
		 console.log("doClear")
		 $("#codemeta_document").val("");
		 $("#check_result").html("");
		 //$("#results_container").css('visibility', 'hidden')
	 },

	 doCopy: function( event ) {
		 alert("copy");
	 }

	 //isValidJson: function(json) {
    // try {
    //    JSON.parse(json);
    //    return true;
    //} catch (e) {
    //    return false;
    //}
  //}
});
