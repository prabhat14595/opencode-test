// Get elements
const board = document.getElementById('board');
const scoreSpan = document.getElementById('score');
const levelSpan = document.getElementById('level');
const targetSpan = document.getElementById('target');
const currentEquationDiv = document.getElementById('current-equation');

// Game variables
let score = 0;
let level = 1;
let target = 18;
let currentEquation = '';
let selectedTiles = [];

// Function to generate the game board
function generateBoard() {
    // Clear the board
    board.innerHTML = '';

    // Generate 5x5 grid of tiles
    for (let i = 0; i < 25; i++) {
        const tile = document.createElement('div');
        tile.classList.add('tile');
        tile.textContent = Math.floor(Math.random() * 10).toString();
        tile.onclick = selectTile;
        board.appendChild(tile);
    }
}

// Function to select a tile
function selectTile(event) {
    const tile = event.target;
    if (selectedTiles.includes(tile)) return;
    selectedTiles.push(tile);
    tile.style.background = 'lightblue';
    currentEquation += tile.textContent;
    currentEquationDiv.textContent = currentEquation;
}

// Function to submit the equation
function submitEquation() {
    // Check if the equation is correct
    if (eval(currentEquation) === target) {
        score += 10;
        level++;
        target = Math.floor(Math.random() * 100) + 1;
        scoreSpan.textContent = score;
        levelSpan.textContent = level;
        targetSpan.textContent = target;
        currentEquation = '';
        selectedTiles.forEach(tile => tile.style.background = 'white');
        selectedTiles = [];
    } else {
        alert('Incorrect equation!');
    }
}

// Function to reset the game
function resetGame() {
    score = 0;
    level = 1;
    target = 18;
    currentEquation = '';
    selectedTiles = [];
    scoreSpan.textContent = score;
    levelSpan.textContent = level;
    targetSpan.textContent = target;
    currentEquationDiv.textContent = '';
    generateBoard();
}

// Start the game
generateBoard();