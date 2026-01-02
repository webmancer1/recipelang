# RecipeLang

RecipeLang is a small, Python-based domain-specific language (DSL) and toolset for authoring, parsing, and processing structured cooking recipes. It aims to make recipes machine-readable so you can programmatically scale servings, convert units, generate shopping lists, and integrate recipes into applications.



## Features

- Human-friendly recipe DSL (author recipes in a simple, readable format)
- Parser that converts recipes into structured Python objects
- Utilities for scaling servings and converting units
- Export formats: JSON, YAML, and plain text
- Command-line interface (CLI) for parsing, validating, and transforming recipes

## Quick start

Requirements:
- Python 3.8+
- pip

Install dependencies (if the repo includes a requirements file):
```bash
pip install -r requirements.txt
```

If this project is packaged, you can install it locally:
```bash
pip install -e .
```

## Usage

Examples below assume a package or module named `recipelang`. Update module/command names as needed.

CLI
```bash
# Parse a recipe file and print JSON to stdout
python -m recipelang.cli parse path/to/recipe.rpl --format json

# Scale a recipe to 4 servings
python -m recipelang.cli scale path/to/recipe.rpl --servings 4 --output scaled.rpl
```

Python API
```python
from recipelang import parser, transformer, io

# Parse DSL text into a Recipe object
text = """
title: Pancakes
servings: 2

ingredients:
  - 1 cup flour
  - 1 cup milk
  - 1 egg

steps:
  - Mix ingredients.
  - Cook on a hot griddle for 2-3 minutes per side.
"""
recipe = parser.parse(text)

# Scale recipe
scaled = transformer.scale(recipe, servings=4)

# Export to JSON
print(io.to_json(scaled))
```

## Recipe DSL (example)

A simple example of the RecipeLang DSL (file extension: `.rpl` or `.recipelang`):

```
title: Classic Pancakes
servings: 2

ingredients:
  - 1 cup all-purpose flour
  - 1 cup milk
  - 1 large egg
  - 1 tbsp sugar
  - 1 tsp baking powder
  - pinch salt

steps:
  - Whisk together dry ingredients.
  - Add milk and egg; stir until combined.
  - Heat a skillet and pour 1/4 cup batter for each pancake.
  - Cook until bubbles form and edges set, flip and cook until golden.
```

## Project structure (suggested)

- recipelang/
  - parser.py — parses DSL into objects
  - model.py — Recipe, Ingredient, Step dataclasses
  - transformer.py — scaling, unit conversion helpers
  - cli.py — command-line entry points
  - io.py — import/export utilities (JSON/YAML)
- tests/ — unit and integration tests
- examples/ — sample recipes and usage examples
- requirements.txt
- README.md

Adjust the structure above to match your repository.

## Development

- Create a virtual environment:
  ```bash
  python -m venv .venv
  source .venv/bin/activate
  pip install -r requirements-dev.txt
  ```
- Run tests:
  ```bash
  pytest
  ```

## Contributing

Contributions are welcome. Typical workflow:

1. Fork the repository.
2. Create a feature branch: `git checkout -b feat/my-feature`
3. Add tests and documentation.
4. Open a pull request describing your changes.

Please follow the repository's coding style and add tests for new functionality.



## Contact

Maintainer: webmancer1  
Repo: https://github.com/webmancer1/recipelang

If you want, tell me whether the project has a CLI name or package import name I should reflect in this README and I’ll update the commands and examples to match.
