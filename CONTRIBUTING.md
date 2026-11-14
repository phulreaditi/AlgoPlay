# Contributing to AlgoPlay

Thank you for your interest in contributing to **AlgoPlay**! We welcome bug reports, new algorithm additions, visualizer themes, and documentation enhancements.

## Development Setup

1. Fork and clone the repository:
   ```bash
   git clone https://github.com/phulreaditi/AlgoPlay.git
   cd AlgoPlay
   ```

2. AlgoPlay uses **only Python's Standard Library** (zero third-party dependencies). Ensure you have Python 3.10 or newer installed with Tkinter:
   ```bash
   python -c "import tkinter; print(tkinter.TkVersion)"
   ```

3. Run the visualizer locally:
   ```bash
   python main.py
   ```

4. Run the unit test suite before submitting PRs:
   ```bash
   python -m unittest discover tests
   ```

## Adding a New Algorithm

To add a new sorting or searching algorithm:
1. Subclass `AlgorithmBase` in `algorithm_base.py`.
2. Implement the generator method `run(data: List[int])` yielding `AlgorithmStep` instances per comparison/swap/pivot.
3. Register the new algorithm in `sorting.py` (`SORTING_ALGORITHMS`) or `searching.py` (`SEARCHING_ALGORITHMS`).
4. Add complexity metrics and intuition briefing to `concept_data.py`.
5. Add unit tests for the algorithm in `tests/test_algorithms.py`.

## Code Style

- Write clean, documented Python adhering to PEP 8 standards.
- Keep the application free from non-standard library dependencies.
