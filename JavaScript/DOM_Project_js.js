function myFunction() {
    document.getElementById("result").innerHTML = "Hello World!";
    document.getElementById("demo").firstChild.nodeValue = "This is how we can control HTML using external JavaScript files."; 
    document.getElementById("demo").style.color = "blue";
    document.getElementById("result1").innerHTML = "This text is added using JavaScript.";
    document.getElementById("demo").childNodes[0].nodeValue = "JavaScript can change HTML content.";

}