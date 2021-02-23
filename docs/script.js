// Global Variables
var cupLayout = 10; 

function main() {
    var c = document.getElementById("c");
    var ctx = c.getContext("2d");
    ctx.fillStyle = "#FF0000";
    ctx.fillRect(0, 0, c.width, c.height);
}

function dropMenu() {
    document.getElementById("myDropdown").classList.toggle("show");
  }

function selectCupLayout() {
    console.log("Clicked Button\n");
}