// Global Variables
var numCups;
var ctx;
var cupLayout = new Array(16).fill(0);; 
var radiusOfShooting;
var minDimension;


function main() {
    var c = document.getElementById("c");
    c.width = visualViewport.width;
    c.height = 0.75 * visualViewport.height;
    ctx = c.getContext("2d");
    if (c.width / 7 < c.height / 4) {
        minDimension = c.width / 7;
    } else {
        minDimension = c.height / 4;
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
            [2, 6, 12].forEach(i => cupLayout[i] = 1);
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
    ctx.clearRect(0, 0, c.width, c.height);
    // This function is going to do all the canvas stuff for showing cups and calculating values
    var cupValues = getCupValues();
    // cupValues.length
    var cupsSpacesPerRow = [1, 3, 5, 7];
    var i = 0; //This is going to index the cupValues and cupLayout array
    for (let rowIndex = 0; rowIndex < cupsSpacesPerRow.length; rowIndex++) {
        var cupSpacesInThisRow = cupsSpacesPerRow[rowIndex];
        // Do some math to figure out the starting pixel values for the first cup in each row
        var cupPositionX = c.width / 2 - ((Math.floor(cupSpacesInThisRow / 2)) * c.width / 7);
        var cupPositionY = c.height / 4 * (rowIndex + 0.5);
        for (var cupSpace = 0; cupSpace < cupSpacesInThisRow; cupSpace++) {
            ctx.strokeStyle = "black";
            boxX = cupPositionX - (c.width / 14);
            boxY = cupPositionY - (c.height / 8);
            boxHeight = c.height / 4;
            boxWidth = c.width / 7;
            //Draw box
            ctx.strokeRect(boxX, boxY, boxWidth, boxHeight);
            // console.log("Drew rectangle at: (" + boxX + ", " + boxY + ")")
            if (cupLayout[i] == 1) {
                // console.log("Draw cup at " + i);
                ctx.fillStyle = cupValues[i];
                ctx.beginPath();
                radius = 0.5 * minDimension;
                ctx.arc(cupPositionX, cupPositionY, radius, 0, 2 * Math.PI);
                ctx.fill();
            } else {
                ctx.fillStyle = "black";
                ctx.fillRect(boxX, boxY, boxWidth, boxHeight);
            }
            //increment variables
            cupPositionX += c.width / 7;
            i++;
        }
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
    console.log("Toggling index" + index);
    if (cupLayout[index] == 1) {
        cupLayout[index] = 0;
        numCups -= 1;
        return true;
    } else {
        if (numCups < 10) {
            cupLayout[index] = 1;
            numCups += 1;
            return true;
        }
        return false;
    }
}

function manageClick(event) {
    var xClick = event.offsetX || event.layer;
    var yClick = event.offsetY || event.layerY;
    // Figure out where the user clicked and toggle that cup
    var row = Math.floor(yClick / c.height * 4);
    var column = Math.floor(xClick / c.width * 7);
    var index = -1;
    console.log("Clicked at [" + row + ", " + column + "]");
    if (row == 0 && column == 3) {
        index = 0;
    } else if (row == 1 && (column >= 2 && column <= 4)) {
        index = column - 1;
    } else if (row == 2 && (column >= 1 && column <= 5)) {
        index = column + 3;
    } else if (row == 3) {
        index = column + 9;
    }
    if (index >= 0) {
        if (toggleCup(index)) {
            renderCups();
        }
    }
}


// Just for show
function dropMenu() {
    document.getElementById("myDropdown").classList.toggle("show");
  }