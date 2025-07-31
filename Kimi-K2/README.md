# Equation Builder

A terminal-based math puzzle game where you connect numbers and operators to build equations and reach target values.

## Game Overview

Connect adjacent tiles on a 5×5 grid to form valid mathematical equations that match the target value. Chain longer equations for higher scores and unlock power-ups!

## How to Play

### Basic Rules
- **Grid**: 5×5 board with numbers (1-9) and operators (+, -, ×, ÷)
- **Objective**: Connect tiles to form equations that equal the target value
- **Movement**: Connect adjacent tiles (horizontal, vertical, diagonal)
- **Validation**: Equations must be mathematically valid

### Scoring
- **Base**: Target value × number of tiles used
- **Bonus**: +50 points for using all 4 operators
- **Chain**: +100 points for equations using 8+ tiles
- **Perfect**: +200 points for clearing the entire board

### Game Modes
- **Timed**: 60 seconds to score as high as possible
- **Endless**: No time limit, progressive difficulty
- **Daily Challenge**: Same puzzle for everyone, compete globally

### Special Tiles
- **Prime Numbers**: Double points when used
- **Wildcards**: Can be any number 1-9
- **Multipliers**: 3× points for the equation

## Setup

```bash
# Clone and play
git clone <repo-url>
cd Kimi-K2
python3 equation_builder.py
```

## Controls
- **Arrow Keys**: Navigate the grid
- **Enter**: Select/deselect tile
- **Space**: Submit equation
- **R**: Reset current selection
- **Q**: Quit game

## Development

Built with Python 3.6+ using only standard library modules for maximum compatibility.

## License
MIT License - Feel free to fork and improve!