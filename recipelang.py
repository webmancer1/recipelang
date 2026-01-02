#!/usr/bin/env python3
"""
RecipeLang Interpreter
A simple programming language for writing cooking recipes

Usage:
    python3 recipelang.py              # Interactive mode
    python3 recipelang.py recipe.rl    # Execute a recipe file
"""

import sys


class RecipeInterpreter:
    """Interpreter for the RecipeLang programming language"""
    
    def __init__(self):
        self.steps = []
        self.ingredients_used = set()
        self.valid_ingredients = {
            'flour', 'eggs', 'sugar', 'butter',
            'milk', 'salt', 'water', 'vanilla'
        }
        self.valid_actions = {'mix', 'bake', 'heat', 'cool', 'add'}
        self.valid_units = {'minutes', 'hours', 'seconds'}
    
    def interpret(self, command):
        """
        Parse and execute a RecipeLang command
        
        Args:
            command (str): The command to interpret
            
        Returns:
            str: Result message or error
        """
        # Strip whitespace and convert to lowercase
        command = command.strip().lower()
        
        # Skip empty lines and comments
        if not command or command.startswith('#'):
            return None
        
        tokens = command.split()
        
        if len(tokens) < 2:
            return "Error: Invalid command"
        
        action = tokens[0]
        
        # Validate action
        if action not in self.valid_actions:
            return f"Error: Unknown action '{action}'. Valid actions: {', '.join(sorted(self.valid_actions))}"
        
        # Handle "action ingredient1 and ingredient2" pattern
        if 'and' in tokens:
            return self._handle_ingredient_mixing(action, tokens)
        
        # Handle "action for number unit" pattern
        elif 'for' in tokens:
            return self._handle_timed_action(action, tokens)
        
        else:
            return "Error: Unknown command pattern. Use 'action ingredient and ingredient' or 'action for number unit'"
    
    def _handle_ingredient_mixing(self, action, tokens):
        """Handle commands like 'mix flour and eggs'"""
        if len(tokens) != 4:
            return "Error: Invalid mixing command. Use format 'action ingredient1 and ingredient2'"
        
        if tokens[2] != 'and':
            return "Error: Expected 'and' between ingredients"
        
        ingredient1 = tokens[1]
        ingredient2 = tokens[3]
        
        # Validate ingredients
        if ingredient1 not in self.valid_ingredients:
            return f"Error: Unknown ingredient '{ingredient1}'. Valid ingredients: {', '.join(sorted(self.valid_ingredients))}"
        
        if ingredient2 not in self.valid_ingredients:
            return f"Error: Unknown ingredient '{ingredient2}'. Valid ingredients: {', '.join(sorted(self.valid_ingredients))}"
        
        # Add to recipe
        self.ingredients_used.add(ingredient1)
        self.ingredients_used.add(ingredient2)
        step = f"Step {len(self.steps) + 1}: {action.capitalize()} {ingredient1} and {ingredient2}"
        self.steps.append(step)
        
        return f"✓ {step}"
    
    def _handle_timed_action(self, action, tokens):
        """Handle commands like 'bake for 30 minutes'"""
        if len(tokens) != 4:
            return "Error: Invalid timed command. Use format 'action for number unit'"
        
        if tokens[1] != 'for':
            return "Error: Expected 'for' after action"
        
        time = tokens[2]
        unit = tokens[3]
        
        # Validate time is numeric
        if not time.isdigit():
            return f"Error: Time must be a number, got '{time}'"
        
        # Validate unit
        if unit not in self.valid_units:
            return f"Error: Unknown time unit '{unit}'. Valid units: {', '.join(sorted(self.valid_units))}"
        
        # Add to recipe
        step = f"Step {len(self.steps) + 1}: {action.capitalize()} for {time} {unit}"
        self.steps.append(step)
        
        return f"✓ {step}"
    
    def get_recipe(self):
        """Generate formatted recipe output"""
        if not self.steps:
            return "No recipe steps yet!"
        
        output = "\n" + "=" * 50 + "\n"
        output += "           YOUR RECIPE\n"
        output += "=" * 50 + "\n\n"
        
        if self.ingredients_used:
            output += "INGREDIENTS:\n"
            output += "  " + ", ".join(sorted(self.ingredients_used)) + "\n\n"
        
        output += "INSTRUCTIONS:\n"
        for step in self.steps:
            output += f"  {step}\n"
        
        output += "\n" + "=" * 50 + "\n"
        return output
    
    def reset(self):
        """Clear the current recipe"""
        self.steps = []
        self.ingredients_used = set()


def print_help():
    """Print usage information"""
    print("""
RecipeLang - A Simple Recipe Programming Language
=================================================

COMMAND PATTERNS:
  1. Mix ingredients:  <action> <ingredient1> and <ingredient2>
  2. Timed actions:    <action> for <number> <unit>

VALID ACTIONS:
  mix, add, bake, heat, cool

VALID INGREDIENTS:
  flour, eggs, sugar, butter, milk, salt, water, vanilla

VALID TIME UNITS:
  minutes, hours, seconds

EXAMPLE COMMANDS:
  mix flour and eggs
  add sugar and butter
  bake for 30 minutes
  cool for 10 minutes

SPECIAL COMMANDS:
  help     - Show this help
  recipe   - Display current recipe
  clear    - Clear current recipe
  quit     - Exit the interpreter
""")


def interactive_mode():
    """Run the interpreter in interactive mode"""
    interpreter = RecipeInterpreter()
    
    print("=" * 50)
    print("  Welcome to RecipeLang Interactive Mode!")
    print("=" * 50)
    print("Type 'help' for commands, 'quit' to exit\n")
    
    while True:
        try:
            command = input("RecipeLang> ").strip()
            
            if not command:
                continue
            
            # Handle special commands
            if command.lower() == 'quit' or command.lower() == 'exit':
                print("\nHappy cooking! 👨‍🍳")
                break
            elif command.lower() == 'help':
                print_help()
                continue
            elif command.lower() == 'recipe':
                print(interpreter.get_recipe())
                continue
            elif command.lower() == 'clear':
                interpreter.reset()
                print("✓ Recipe cleared!")
                continue
            
            # Interpret the command
            result = interpreter.interpret(command)
            if result:
                print(result)
                
        except KeyboardInterrupt:
            print("\n\nHappy cooking! 👨‍🍳")
            break
        except EOFError:
            print("\n\nHappy cooking! 👨‍🍳")
            break


def file_mode(filename):
    """Execute commands from a file"""
    interpreter = RecipeInterpreter()
    
    try:
        with open(filename, 'r') as f:
            print(f"Executing recipe from: {filename}\n")
            
            for line_num, line in enumerate(f, 1):
                line = line.strip()
                
                # Skip empty lines and comments
                if not line or line.startswith('#'):
                    continue
                
                print(f"[Line {line_num}] {line}")
                result = interpreter.interpret(line)
                
                if result:
                    print(f"  → {result}")
                    
                    # Stop on errors
                    if result.startswith("Error"):
                        print(f"\nExecution stopped at line {line_num}")
                        return
            
            # Display final recipe
            print(interpreter.get_recipe())
            
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found")
        sys.exit(1)
    except Exception as e:
        print(f"Error reading file: {e}")
        sys.exit(1)


def main():
    """Main entry point"""
    if len(sys.argv) > 1:
        # File mode
        file_mode(sys.argv[1])
    else:
        # Interactive mode
        interactive_mode()


if __name__ == "__main__":
    main()



