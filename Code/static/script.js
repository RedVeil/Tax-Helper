document.addEventListener("DOMContentLoaded",function() {

localStorage.setItem("counter", 1)


//test
var finanzamt = document.getElementById("finanzamt")
var userValue = localStorage.getItem("finanzamt")
if (userValue !== ""){
    finanzamt.setAttribute("value", userValue)
}



//test end

submit = document.getElementById("submit");
submit.addEventListener('click', next)

function next(){
    counter ++
    var input_fields = document.getElementsByClassName("input_field")
    for (i=0, len=Object.keys(input_fields).length; i<len; i++){
        localStorage.setItem(input_fields[i].name, input_fields[i].value)

    };
    /*var paragraph = document.createElement("p")
    paragraph.textContent = "test"
    document.body.appendChild(paragraph)*/

};

function back(){
};
});

