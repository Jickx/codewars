# Algorithms & Codewars Solutions

This repository collects algorithm practice and Codewars kata solutions. It is organized by kata difficulty and topic to keep solutions small, testable, and easy to review.

## Contents
- Solutions grouped by difficulty (e.g. `8_kyu/`, `7_kyu/`, `6_kyu/`, `5_kyu/`, `4_kyu/`)  
- Tests and example scripts next to implementations or in a `tests/` folder  
- Notes and scratch files for problem analysis

## Languages
Primarily Python.

## Repository layout (example)
- 4_kyu/
  - snail.py
- 5_kyu/
- tests/
- README.md  <- this file

## How to run
- Python solutions: run the file directly or import the function in a script or REPL.
  - Example:
    ```
    from 4_kyu.snail import snail  # adjust import path as needed
    print(snail([[1,2,3],[4,5,6],[7,8,9]]))
    ```
- Tests: use pytest (preferred) or unittest.
  - Install pytest: `pip install pytest`
  - Run tests: `pytest` from the repository root.

## Examples
Input:
```
[
 [1,2,3],
 [4,5,6],
 [7,8,9]
]
```
Output (snail pattern):
```
[1,2,3,6,9,8,7,4,5]
```

## Contribution guidelines
- Keep each solution focused on a single kata.
- Add unit tests for new or updated solutions.
- Include brief comments or a short README in subfolders explaining approach and complexity.
- Open a pull request for review; prefer small, incremental changes.

## Testing & CI
- Prefer pytest for automated tests.
- Add CI (GitHub Actions) if desired to run tests on push/PR.

