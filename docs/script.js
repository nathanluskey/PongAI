// Global Variables
var numCups;
var ctx;
var cupLayout = new Array(16).fill(0);; 
var radiusOfShooting;
var minDimension;

function main() {
    var c = document.getElementById("c");
    ctx = c.getContext("2d");
    if (c.width < c.height) {
        minDimension = c.width;
    } else {
        minDimension = c.height;
    }
    modifyRadius();
    selectCupLayout(10); //Create default cup layout
    // console.log(qTable)
}

function modifyRadius() {
    var numericValue = document.getElementById("radius").value;
    radiusOfShooting = Number(numericValue).toFixed(2);
    // console.log("radius is " + radiusOfShooting);
    renderCups();
}

function selectCupLayout(newNumCups) {
    switch (newNumCups) {
        case 10:
            cupLayout = new Array(16).fill(0);
            [0, 1, 3, 4, 6, 8, 9, 11, 13, 15].forEach(i => cupLayout[i] = 1);
            numCups = newNumCups;
            break;
        case 6:
            cupLayout = new Array(16).fill(0);
            [2, 5, 7, 10, 12, 14].forEach(i => cupLayout[i] = 1);
            numCups = newNumCups;
            break;
        case 4:
            cupLayout = new Array(16).fill(0);
            [5, 6, 11, 12].forEach(i => cupLayout[i] = 1);
            numCups = newNumCups;
            break;
        case 3:
            cupLayout = new Array(16).fill(0);
            [6, 11, 13].forEach(i => cupLayout[i] = 1);
            numCups = newNumCups;
            break;
        case 2:
            cupLayout = new Array(16).fill(0);
            [6, 12].forEach(i => cupLayout[i] = 1);
            numCups = newNumCups;
            break;
    }
    console.log("cupLayout = " + cupLayout);
    renderCups();
}

function renderCups() {
    // This function is going to do all the canvas stuff for showing cups and calculating values
    var cupValues = getCupValues();
    // cupValues.length
    for (let i = 0; i < 1; i++) {
        // TODO: Write the full code for drawing the pyramid
        ctx.strokeStyle = "red";
        x = c.width / 2;
        y = c.height / 2;
        width = minDimension * 0.3;
        height = minDimension * 0.3;
        ctx.strokeRect(x, y, width, height);
    }
}

function getCupValues() {
    // Given the cupsLayout and shooting radius return the array of cup values
    
    // First hash the array
    var indexInQTable = 0;
    for (let i = 0; i < cupLayout.length; i++) {
        if (cupLayout[i] == 1) {
            indexInQTable += Math.pow(2, i);
        }
    }
    // console.log("indexInQTable is " + indexInQTable);
    var output = qTable[radiusOfShooting][indexInQTable];
    // console.log("cupValues are " + output);
    return output
}

function toggleCup(index) {
    if (numCups < 10) {
        if (cupLayout[index] == 1) {
            cupLayout[index] = 0;
            numCups -= 1;
        } else {
            cupLayout[index] = 1;
            numCups += 1;
        }
        return true;
    } else {
        return false;
    }
}

function manageClick() {
    // Figure out where the user clicked and toggle that cup
}


// Just for show
function dropMenu() {
    document.getElementById("myDropdown").classList.toggle("show");
  }