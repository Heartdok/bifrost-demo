# Tests for Bifrost Demo

This directory contains tests for the Bifrost Demo repository.

## Running Tests

You can run the tests using the following command:

```bash
python -m unittest discover tests
```

## Test Coverage

To get test coverage information, you can use the `coverage` package:

```bash
# Install coverage if you don't have it
pip install coverage

# Run tests with coverage
coverage run -m unittest discover tests

# Generate a coverage report
coverage report

# Generate an HTML report
coverage html
```

## Test Structure

- `test_utils.py`: Tests for the utility functions in the `utils.py` module
