document.addEventListener("DOMContentLoaded",function() {

localStorage.setItem("counter", 1)
var counter = localStorage.getItem("counter")



submitCounter = "submit".concat(counter.toString());
submit = document.getElementById("submit1");
//submit.innerHTML = submitCounter;
submit.addEventListener('click', next)

function next(){
    counter ++
    var input_fields = document.getElementsByClassName("input_field")
    for (i=0, len=Object.keys(input_fields).length; i<len; i++){
        console.log(i)
        localStorage.setItem(input_fields[i].name, input_fields[i].value)

    };
    /*var paragraph = document.createElement("p")
    paragraph.textContent = "test"
    document.body.appendChild(paragraph)*/

};

function back(){
};
});

