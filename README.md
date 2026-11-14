# AlgoPlay — Interactive Algorithm Visualizer & Learning Engine

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10%2B-blue?style=for-the-badge&logo=python&logoColor=white" alt="Python 3.10+" />
  <img src="https://img.shields.io/badge/GUI-Tkinter-informational?style=for-the-badge&logo=python" alt="Tkinter GUI" />
  <img src="https://img.shields.io/badge/Dependencies-Zero%20(Stdlib)-success?style=for-the-badge" alt="Zero Dependencies" />
  <img src="https://img.shields.io/badge/Platform-Windows%20%7C%20macOS%20%7C%20Linux-lightgrey?style=for-the-badge" alt="Cross Platform" />
  <img src="https://img.shields.io/github/actions/workflow/status/phulreaditi/AlgoPlay/ci.yml?branch=main&style=for-the-badge&label=CI" alt="CI Status" />
  <img src="https://img.shields.io/badge/License-MIT-green?style=for-the-badge" alt="License" />
</p>

An interactive, responsive desktop algorithm visualizer designed to make data structures and algorithms intuitive, visual, and engaging — built **purely with Python and Tkinter** with **zero external dependencies**.

AlgoPlay combines real-time canvas animations with live pseudocode synchronization, step-by-step coaching, pre-flight algorithmic complexity briefings, head-to-head algorithm racing, and a gamified XP prediction engine.

---

## Table of Contents

- [Key Features](#-key-features)
- [Supported Algorithms](#-supported-algorithms)
- [Color System & Visual Legend](#-color-system--visual-legend)
- [Keyboard Shortcuts](#-keyboard-shortcuts)
- [Quick Start](#-quick-start)
- [Project Architecture](#-project-architecture)
- [Running Unit Tests](#-running-unit-tests)
- [Contributing](#-contributing)
- [License](#-license)

---

## ✨ Key Features

### 1. Dual Canvas Visualization
- **Sorting Mode**: Vertical bars with proportional height scaling, top cap highlights, in-bar action badges (`⇄`, `CMP`, `P`), relational comparison arches (`v1 > v2`), and subtle partition tints behind sorted elements.
- **Searching Mode**: Centered array cards with probe badges, active search range brackets (`[low … high]`), target match pulsing rings, and diagonal strikethroughs across eliminated candidates.

### 2. Synchronized Pseudocode & Step Coach
- **Live Pseudocode**: Displays accurate implementation steps with instant line-highlighting synchronized to the active generator yield.
- **Interactive Coach**: Plain-English explanations describing *what* just happened, *what to watch next*, and an expandable **"Why?"** breakdown explaining the underlying algorithm invariant.

### 3. Pre-Flight Concept & Complexity Briefing
- Before executing any sort or search, view a pre-flight modal summarizing:
  - Core algorithmic intuition & strategy
  - Real-world conceptual analogies (e.g., sorting playing cards, looking up a word in a dictionary)
  - Time & Space Complexity breakdown (Best $\Omega$, Average $\Theta$, Worst $O$, Auxiliary Space)

### 4. Head-to-Head Race Mode
- Launch a split-canvas window pitting any two sorting algorithms against one another on the exact same dataset.
- Real-time comparison/swap counters, progress metrics, and celebration particle confetti upon completion.

### 5. Benchmark Performance Comparison
- Run all five sorting algorithms concurrently on the active dataset to generate an instant comparative bar chart tracking exact operation counts.

### 6. Gamified Quiz & Story Mode
- **Predict-Next-Step Engine**: Inline challenges prompt learners to forecast algorithm decisions (e.g., "Will these elements swap?"), awarding XP and tracking answer streaks.
- **Story Mode**: 8 narrative chapters led by 7 algorithm companion mascots, complete with dialogue bubbles, level progression, and 14 unlockable achievements saved locally.

### 7. Dual Modern Themes
- Switch seamlessly between a high-contrast dark theme (ink-black surfaces, vibrant cobalt/amber/rose data bars) and a crisp light theme with an observer-driven palette update across all widgets.

---

## 📊 Supported Algorithms

| Algorithm | Category | Best Case | Average Case | Worst Case | Space | Stable |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: |
| **Bubble Sort** | Sorting | $\Omega(n)$ | $\Theta(n^2)$ | $O(n^2)$ | $O(1)$ | Yes |
| **Insertion Sort** | Sorting | $\Omega(n)$ | $\Theta(n^2)$ | $O(n^2)$ | $O(1)$ | Yes |
| **Selection Sort** | Sorting | $\Omega(n^2)$ | $\Theta(n^2)$ | $O(n^2)$ | $O(1)$ | No |
| **Merge Sort** | Sorting | $\Omega(n \log n)$ | $\Theta(n \log n)$ | $O(n \log n)$ | $O(n)$ | Yes |
| **Quick Sort** | Sorting | $\Omega(n \log n)$ | $\Theta(n \log n)$ | $O(n^2)$ | $O(\log n)$ | No |
| **Linear Search** | Searching | $\Omega(1)$ | $\Theta(n)$ | $O(n)$ | $O(1)$ | N/A |
| **Binary Search** | Searching | $\Omega(1)$ | $\Theta(\log n)$ | $O(\log n)$ | $O(1)$ | N/A |
| **Jump Search** | Searching | $\Omega(1)$ | $\Theta(\sqrt{n})$ | $O(\sqrt{n})$ | $O(1)$ | N/A |
| **Interpolation Search** | Searching | $\Omega(1)$ | $\Theta(\log \log n)$ | $O(n)$ | $O(1)$ | N/A |
| **Exponential Search** | Searching | $\Omega(1)$ | $\Theta(\log n)$ | $O(\log n)$ | $O(1)$ | N/A |
| **Ternary Search** | Searching | $\Omega(1)$ | $\Theta(\log_3 n)$ | $O(\log_3 n)$ | $O(1)$ | N/A |

---

## 🎨 Color System & Visual Legend

| State | Dark Theme | Light Theme | Meaning |
| :--- | :---: | :---: | :--- |
| **Default** | `#2563EB` | `#3B82F6` | Unsorted / unvisited element |
| **Comparing** | `#F59E0B` | `#D97706` | Active comparison probe |
| **Swapping** | `#F43F5E` | `#E11D48` | Elements actively being swapped or shifted |
| **Sorted** | `#10B981` | `#059669` | Element confirmed in its final position |
| **Pivot** | `#06B6D4` | `#0891B2` | Quick Sort partition pivot line / marker |
| **Target** | `#818CF8` | `#6366F1` | Active search target |
| **Eliminated** | `#16161E` | `#E5E5EF` | Candidate excluded from search space |

---

## ⌨️ Keyboard Shortcuts

| Key | Action |
| :--- | :--- |
| <kbd>Space</kbd> / <kbd>→</kbd> | Step forward one algorithmic state |
| <kbd>Enter</kbd> | Start continuous animation |
| <kbd>P</kbd> | Pause / Resume animation |
| <kbd>R</kbd> | Reset dataset to initial state |
| <kbd>S</kbd> | Shuffle / generate new random array |

---

## 🚀 Quick Start

### Prerequisites
- **Python 3.10 or higher**
- **Tkinter** (included by default on standard Python installations on Windows and macOS; on Linux, run `sudo apt-get install python3-tk`)

### 1. Clone the repository
```bash
git clone https://github.com/phulreaditi/AlgoPlay.git
cd AlgoPlay
```

### 2. Launch AlgoPlay

- **On Windows**: Double-click `run.bat` or run:
  ```bash
  python main.py
  ```
- **On macOS & Linux**: Run:
  ```bash
  chmod +x run.sh && ./run.sh
  ```
  *(or `python3 main.py`)*

- **Run as a module**:
  ```bash
  python -m AlgoPlay
  ```

- **Install via pip (optional)**:
  ```bash
  pip install -e .
  algoplay
  ```

---

## 🏛️ Project Architecture

AlgoPlay is structured with clean separation of concerns and modular component boundaries:

- **Strategy Pattern (`algorithm_base.py`)**: Abstract base classes decouple algorithm logic from visualization.
- **Python Generators & Non-Blocking Event Loop**: Algorithms yield `AlgorithmStep` frames. Tkinter's `root.after()` ticks drive animations smoothly without freezing the GUI.
- **Observer Pattern (`theme.py`)**: `ThemeManager` notifies registered widgets on theme switches.
- **State Persistence (`game_state.py`)**: XP, streaks, and achievements serialize to `saves/progress.json`.

```
AlgoPlay/
├── main.py              # Application shell, tab coordinator, and event loop
├── __main__.py          # Module execution entry point
├── run.bat              # Windows one-click launcher
├── run.sh               # macOS / Linux launcher
├── pyproject.toml       # Python package configuration
├── visualizer.py        # Canvas rendering engine (bars, cards, arches, confetti)
├── algorithm_base.py    # AlgorithmBase abstract class and AlgorithmStep dataclass
├── sorting.py           # Bubble, Insertion, Selection, Merge, Quick Sort generators
├── searching.py         # Linear, Binary, Jump, Interpolation, Exponential, Ternary Search
├── concept_briefing.py  # Pre-flight algorithm concept & complexity modal
├── concept_data.py      # Detailed pedagogical explanations & complexity data
├── coach.py             # Step-by-step explainer & "Why?" invariant guide
├── controls.py          # Controls, sliders, custom array entry, and complexity cards
├── hint_engine.py       # Predict-next-step interactive quiz modal
├── progress_hud.py      # Completion percentage HUD & learning tip ticker
├── race_window.py       # Head-to-head algorithm race window
├── quiz.py              # Gamified algorithm trivia window
├── story_tab.py         # Story Mode tab controller
├── story.py             # Narrative chapters, level data, and boss challenges
├── mascots.py           # 7 algorithm companion mascots
├── badges.py            # Achievement badges and unlock logic
├── stats.py             # Performance metric counters (comparisons, swaps, accesses)
├── theme.py             # Dark & light theme color palettes and observer manager
├── widgets.py           # Custom Tkinter widget helpers (FlatButton, Card, etc.)
├── saves/               # Persistent progress and XP storage
│   └── progress.json
└── tests/               # Unit and GUI test suite
    ├── test_algorithms.py
    └── test_gui.py
```

---

## 🧪 Running Unit Tests

Run the complete test suite verifying all algorithm generators, search logic, game state, and GUI components:

```bash
python -m unittest discover tests
```

---

## 🤝 Contributing

Contributions are warmly welcome! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines on adding new algorithms and visualizer themes.

---

## 📄 License

Distributed under the MIT License. See [LICENSE](LICENSE) for more details.
