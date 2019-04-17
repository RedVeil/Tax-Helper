document.addEventListener("DOMContentLoaded",function() {

var input_fields = document.getElementsByClassName("input_field")
for (i=0, len=Object.keys(input_fields).length; i<len; i++){
    input_fields[i].setAttribute("value", localStorage.getItem(input_fields[i].name))};



    
});



