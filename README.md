# RecipeLang 🍰

A simple programming language for writing cooking recipes in natural language.

## Installation

**Requirements:** Python 3.6+

```bash
# Clone the repository
git clone https://github.com/yourusername/recipelang.git
cd recipelang

# Make executable (optional)
chmod +x recipelang.py
```

## Quick Start

```bash
# Run interactive mode
python3 recipelang.py

# Or execute a recipe file
python3 recipelang.py my_recipe.rl
```

## Project Structure

```
recipelang/
├── recipelang.py          # Main interpreter
├── README.md              # This file
└── examples/              # Example recipe files
    ├── cake.rl
    ├── beverage.rl
    └── pancakes.rl
```

## Syntax

### Two Command Types

**1. Mix ingredients:**
```
mix flour and eggs
add sugar and butter
```

**2. Timed actions:**
```
bake for 30 minutes
heat for 5 minutes
```

### Valid Keywords

**Actions:** `mix`, `add`, `bake`, `heat`, `cool`

**Ingredients:** `flour`, `eggs`, `sugar`, `butter`, `milk`, `salt`, `water`, `vanilla`

**Time Units:** `seconds`, `minutes`, `hours`

## Example Recipe

**File:** `cake.rl`
```
# Simple cake recipe
mix flour and eggs
add sugar and butter
bake for 30 minutes
cool for 10 minutes
```

**Run:**
```bash
python3 recipelang.py cake.rl
```

**Output:**
```
==================================================
           YOUR RECIPE
==================================================

INGREDIENTS:
  butter, eggs, flour, sugar

INSTRUCTIONS:
  Step 1: Mix flour and eggs
  Step 2: Add sugar and butter
  Step 3: Bake for 30 minutes
  Step 4: Cool for 10 minutes

==================================================
```

## Interactive Mode

```bash
python3 recipelang.py
```

**Commands:**
- `help` - Show help
- `recipe` - Display current recipe
- `clear` - Clear recipe
- `quit` - Exit

## Grammar (BNF)

```bnf
<statement> ::= <action> <ingredient> "and" <ingredient>
              | <action> "for" <time> <unit>
              
<action>     ::= "mix" | "bake" | "heat" | "cool" | "add"
<ingredient> ::= "flour" | "eggs" | "sugar" | "butter" | "milk" | "salt" | "water" | "vanilla"
<unit>       ::= "minutes" | "hours" | "seconds"
```

## License

MIT License
