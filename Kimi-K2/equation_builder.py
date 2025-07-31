#!/usr/bin/env python3
"""
Equation Builder - Terminal Math Puzzle Game
Connect numbers and operators to build equations and reach target values.
"""

import random
import os
import sys
import time
from typing import List, Tuple, Optional

class GameBoard:
    def __init__(self, size: int = 5):
        self.size = size
        self.board = []
        self.selected = []
        self.score = 0
        self.level = 1
        self.target = 0
        self.game_mode = "endless"
        self.time_left = 60
        self.generate_board()
        self.generate_target()
    
    def generate_board(self):
        """Generate a 5x5 grid with numbers and operators."""
        numbers = list(range(1, 10))
        operators = ['+', '-', '*', '/']
        
        self.board = []
        for i in range(self.size):
            row = []
            for j in range(self.size):
                if random.random() < 0.7:  # 70% chance for number
                    row.append(str(random.choice(numbers)))
                else:
                    row.append(random.choice(operators))
            self.board.append(row)
    
    def generate_target(self):
        """Generate a target value based on current level."""
        self.target = random.randint(10, 20 + self.level * 5)
    
    def display_board(self):
        """Display the game board with ASCII art."""
        os.system('clear' if os.name == 'posix' else 'cls')
        
        print(f"Equation Builder - Level {self.level}")
        print(f"Target: {self.target} | Score: {self.score}")
        if self.game_mode == "timed":
            print(f"Time: {self.time_left}s")
        print()
        
        # Column numbers
        print("   ", end="")
        for i in range(self.size):
            print(f" {i} ", end="")
        print("\n")
        
        for i, row in enumerate(self.board):
            print(f"{i}  ", end="")
            for j, cell in enumerate(row):
                if (i, j) in self.selected:
                    print(f"[{cell}]", end="")
                else:
                    print(f" {cell} ", end="")
            print()
        
        print("\nControls: Arrow keys to move, Enter to select, Space to submit, R to reset, Q to quit")
    
    def is_valid_position(self, x: int, y: int) -> bool:
        """Check if position is within board bounds."""
        return 0 <= x < self.size and 0 <= y < self.size
    
    def is_adjacent(self, pos1: Tuple[int, int], pos2: Tuple[int, int]) -> bool:
        """Check if two positions are adjacent (including diagonals)."""
        x1, y1 = pos1
        x2, y2 = pos2
        return abs(x1 - x2) <= 1 and abs(y1 - y2) <= 1
    
    def can_add_to_selection(self, x: int, y: int) -> bool:
        """Check if a tile can be added to the current selection."""
        if not self.selected:
            return True
        
        last_x, last_y = self.selected[-1]
        return self.is_adjacent((x, y), (last_x, last_y)) and (x, y) not in self.selected
    
    def validate_equation(self, equation: str) -> Optional[float]:
        """Validate if the equation is mathematically correct."""
        try:
            # Replace × with * for evaluation
            equation = equation.replace('×', '*').replace('÷', '/')
            result = eval(equation)
            return float(result)
        except:
            return None
    
    def check_equation(self) -> bool:
        """Check if the selected tiles form a valid equation."""
        if len(self.selected) < 3:
            return False
        
        # Build equation from selected tiles
        equation = ""
        for x, y in self.selected:
            equation += self.board[x][y]
        
        result = self.validate_equation(equation)
        return result is not None and abs(result - self.target) < 0.001
    
    def calculate_score(self) -> int:
        """Calculate score for the current equation."""
        base_score = self.target * len(self.selected)
        
        # Bonus for using operators
        operators_used = set()
        for x, y in self.selected:
            if self.board[x][y] in ['+', '-', '*', '/']:
                operators_used.add(self.board[x][y])
        
        if len(operators_used) >= 3:
            base_score += 50
        
        if len(self.selected) >= 8:
            base_score += 100
        
        return base_score
    
    def clear_selection(self):
        """Clear the current selection."""
        self.selected = []
    
    def submit_equation(self) -> bool:
        """Submit the current equation for validation."""
        if self.check_equation():
            self.score += self.calculate_score()
            self.level += 1
            self.generate_board()
            self.generate_target()
            self.clear_selection()
            return True
        return False
    
    def reset_level(self):
        """Reset the current level."""
        self.clear_selection()
        self.generate_board()
        self.generate_target()

class GameController:
    def __init__(self):
        self.game = GameBoard()
        self.cursor_x = 0
        self.cursor_y = 0
    
    def handle_input(self, key: str) -> bool:
        """Handle user input."""
        if key.lower() == 'q':
            return False
        elif key.lower() == 'r':
            self.game.clear_selection()
        elif key == ' ':
            if self.game.submit_equation():
                print("Correct! Well done!")
                time.sleep(1)
        elif key == '\r':  # Enter key
            pos = (self.cursor_y, self.cursor_x)
            if pos not in self.game.selected and self.game.can_add_to_selection(self.cursor_y, self.cursor_x):
                self.game.selected.append(pos)
        elif key == '\x1b':  # Arrow keys (simplified)
            return True
        
        return True
    
    def move_cursor(self, dx: int, dy: int):
        """Move the cursor."""
        new_x = max(0, min(self.game.size - 1, self.cursor_x + dx))
        new_y = max(0, min(self.game.size - 1, self.cursor_y + dy))
        self.cursor_x = new_x
        self.cursor_y = new_y
    
    def run(self):
        """Main game loop."""
        print("Equation Builder - Loading...")
        time.sleep(1)
        
        while True:
            self.game.display_board()
            
            # Show current selection as equation
            if self.game.selected:
                equation = ""
                for x, y in self.game.selected:
                    equation += self.game.board[x][y]
                print(f"Current: {equation}")
            
            try:
                key = input("Move: ").lower()
                if not self.handle_input(key):
                    break
            except KeyboardInterrupt:
                break
        
        print(f"\nGame Over! Final Score: {self.game.score}")

if __name__ == "__main__":
    game = GameController()
    game.run()