const button =document.getElementById("submit-button");

function submit () {
    let name =document.getElementById("name").value;
    let question = document.getElementById("question").value;
    alert("hello, your name is " + name +" and your question is " + question);
    //console.log("y");
    //window.open("https://www.example.com")
}

button.addEventListener("click", submit);