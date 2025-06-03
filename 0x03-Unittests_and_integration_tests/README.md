# alx-backend-python

This repository contains Python projects and exercises focused on backend development, with an emphasis on understanding and implementing unit tests and integration tests. The content is aligned with the ALX Software Engineering curriculum.

## Directory Structure

- `0x03-Unittests_and_integration_tests/`: Main directory for this project.
  - `utils.py`: Utility functions including `access_nested_map`, `get_json`, and `memoize`.
  - `test_utils.py`: Unit tests for the utility functions using the `unittest` framework.
  - `README.md`: This file.

## Files

### `utils.py`

A generic utilities module that includes:

- `access_nested_map(nested_map: Mapping, path: Sequence) -> Any`: Accesses a value in a nested dictionary structure using a sequence of keys.
- `get_json(url: str) -> Dict`: Fetches JSON data from a remote URL.
- `memoize(fn: Callable) -> Callable`: A decorator to cache the result of a method call.

### `test_utils.py`

Unit tests for the `utils.py` module, specifically testing the `access_nested_map` function. The tests use the `unittest` framework along with `parameterized` to test multiple input cases.

## Requirements

All files are written to comply with the following:

- Python version: 3.7 (on Ubuntu 18.04 LTS)
- Pycodestyle version: 2.5
- All files end with a new line.
- All Python scripts have the shebang line: `#!/usr/bin/env python3`
- Full documentation and type annotations are included for all modules, classes, and functions.

## Running Tests

To execute the unit tests:

```bash
$ python -m unittest path/to/test_utils.py