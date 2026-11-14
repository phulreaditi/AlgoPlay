"""
Unit tests for AlgoPlay sorting, searching, and game state engines.
"""

import unittest
import os
import sys

# Add parent directory to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from sorting import SORTING_ALGORITHMS
from searching import SEARCHING_ALGORITHMS
from stats import StatsTracker
from game_state import GameState
from badges import BADGES


class TestSortingAlgorithms(unittest.TestCase):

    def setUp(self):
        self.test_cases = [
            [45, 12, 89, 34, 70, 23, 56, 91, 18, 67],
            [1, 2, 3, 4, 5, 6, 7, 8],
            [8, 7, 6, 5, 4, 3, 2, 1],
            [5, 1, 5, 3, 1, 9, 3, 5],
            [42],
            [99, 11]
        ]

    def test_all_sorting_algorithms(self):
        for name, algo in SORTING_ALGORITHMS.items():
            for case in self.test_cases:
                with self.subTest(algorithm=name, input=case):
                    arr = list(case)
                    stats = StatsTracker()
                    gen = algo.run(arr)
                    final_arr = list(arr)
                    for step in gen:
                        if hasattr(step, "array") and step.array:
                            final_arr = list(step.array)
                    self.assertEqual(final_arr, sorted(case), f"{name} failed on {case}")


class TestSearchingAlgorithms(unittest.TestCase):

    def setUp(self):
        self.sorted_data = [10, 15, 23, 34, 45, 56, 67, 78, 89, 92, 105, 120]

    def test_search_existing_elements(self):
        targets = [10, 56, 120]  # First, middle, last
        for name, algo in SEARCHING_ALGORITHMS.items():
            for target in targets:
                with self.subTest(algorithm=name, target=target):
                    stats = StatsTracker()
                    gen = algo.run(list(self.sorted_data), target=target)
                    found = False
                    for step in gen:
                        if getattr(step, "found_index", None) is not None:
                            found = True
                    self.assertTrue(found, f"{name} failed to find {target}")

    def test_search_missing_element(self):
        target = 999
        for name, algo in SEARCHING_ALGORITHMS.items():
            with self.subTest(algorithm=name, target=target):
                stats = StatsTracker()
                gen = algo.run(list(self.sorted_data), target=target)
                found = False
                for step in gen:
                    if getattr(step, "found_index", None) is not None:
                        found = True
                self.assertFalse(found, f"{name} incorrectly claimed to find {target}")


class TestGameStateAndBadges(unittest.TestCase):

    def test_game_state_xp_and_streak(self):
        state = GameState()
        initial_xp = state.xp
        state.add_xp(50)
        self.assertEqual(state.xp, initial_xp + 50)

        state.correct_answer()
        self.assertEqual(state.streak, 1)
        self.assertEqual(state.best_streak, 1)

        state.wrong_answer()
        self.assertEqual(state.streak, 0)
        self.assertEqual(state.best_streak, 1)

    def test_badge_definitions(self):
        self.assertGreater(len(BADGES), 0)
        for badge in BADGES:
            self.assertTrue(hasattr(badge, "name"))
            self.assertTrue(hasattr(badge, "description"))


if __name__ == "__main__":
    unittest.main()
