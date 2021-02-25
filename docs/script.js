// Global Variables
var cupLayout = 10; 
var ctx;
var json;

function main() {
    var c = document.getElementById("c");
    ctx = c.getContext("2d");
    ctx.fillStyle = "red";
    ctx.fillRect(0, 0, c.width, c.height);
    console.log(qTable)
}

function dropMenu() {
    document.getElementById("myDropdown").classList.toggle("show");
  }

function selectCupLayout(newCupLayout) {
    console.log("Clicked Button\n");
    cupLayout = newCupLayout;
}