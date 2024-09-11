# Sparse Matrix Operations

## Overview

This project provides a Python implementation of sparse matrix operations using a dictionary of dictionaries. It supports reading sparse matrices from files and performing addition, subtraction, and multiplication.

## File Structure
/DSA/sparse_matrix/
    ├── src
    │    └── sparse_matrix.py
    ├── sample_inputs/
    └── sample_results/

## Requirements
- Python 3.x

## Usage
### Running the Script
Navigate to the directory containing `sparse_matrix.py` and run:
python sparse_matrix.py

### User Interaction
The script prompts for:
1. **Operation**: `add`, `subtract`, or `multiply`
2. **First Matrix File Path**
3. **Second Matrix File Path**

### Input File Format
rows=<number_of_rows>
cols=<number_of_columns>
(<row_index>, <col_index>, <value>)

### Output
Results are saved in `sample_results` directory with filenames based on input files and operation.

## SparseMatrix Class
- **Attributes**: `rows`, `cols`, `data`
- **Methods**:
  - `__init__(rows, cols)`
  - `from_file(file_path)`
  - `get_element(row, col)`
  - `set_element(row, col, value)`
  - `add(matrix)`
  - `subtract(matrix)`
  - `multiply(matrix)`
  - `__str__()`

## Error Handling
- Raises `ValueError` for incorrect file formats.
- General exceptions are caught and printed.

### AUTHOR
Afsa Umutoniwase