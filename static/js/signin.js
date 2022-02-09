$('[name="flag"]').change(function () {
   var end = this.value;
   if (end == 'Other'){
       $('[name="otherInstitute"]').show();
   }
   else {
       $('[name="otherInstitute"]').hide();
   }
}


//  $('div_id_flag').onchange (function (e) {
//      var optionSelected = $("option:selected", this)
//      var valueSelected = this.value;

//      if (valueSelected === 1){
//          $('div_categories_verified').hide();
//      } else {
//          $('div_categories_verified').show();
//      }
//  });


   //  alert("Hi!");
// $(document).ready(function() {
// 	$("#div_id_flag").change(function() {

// 		var selectedVal = $("#myselect option:selected").text();
// 		var selectedVal = $("#div_id_flag option:selected").val();
// 		alert("Hi, your favorite programming language is " + selectedVal);

// 	})
// });

// {'onchange': "myFunction(this.value);"}
// myFunction(value) {
// 	console.log(value)
// }

alert("hello");
