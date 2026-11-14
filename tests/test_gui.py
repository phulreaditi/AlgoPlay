"""
GUI integration tests for AlgoPlay Tkinter windows.
"""

import unittest
import os
import sys
import tkinter as tk

# Add parent directory to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from main import AlgoPlayApp
from race_window import RaceWindow
from quiz import QuizWindow
from theme import theme_manager


class TestAlgoPlayGUI(unittest.TestCase):

    def setUp(self):
        self.root = tk.Tk()
        self.root.withdraw()  # Hide window during test
        self.app = AlgoPlayApp(self.root)
        self.root.update()

    def tearDown(self):
        try:
            self.root.destroy()
        except Exception:
            pass

    def test_app_initialization(self):
        self.assertIsNotNone(self.app)
        self.assertEqual(self.app.tab_idx, 0)
        self.assertFalse(self.app.is_running)

    def test_tab_switching(self):
        # Switch to Searching tab (index 1)
        self.app._switch_tab(1)
        self.root.update()
        self.assertEqual(self.app.tab_idx, 1)

        # Switch to Story tab (index 2)
        self.app._switch_tab(2)
        self.root.update()
        self.assertEqual(self.app.tab_idx, 2)

        # Switch back to Sorting tab (index 0)
        self.app._switch_tab(0)
        self.root.update()
        self.assertEqual(self.app.tab_idx, 0)

    def test_sorting_selection_and_step(self):
        self.app.select_sort("Merge Sort")
        self.root.update()
        self.assertEqual(self.app.cur_sort, "Merge Sort")
        self.app.action_step()
        self.root.update()

    def test_searching_selection_and_step(self):
        self.app._switch_tab(1)
        self.app.select_search("Binary Search")
        self.root.update()
        self.assertEqual(self.app.cur_search, "Binary Search")
        self.app.action_step()
        self.root.update()

    def test_theme_toggle(self):
        current_theme = theme_manager.current_theme
        self.app.toggle_theme()
        self.root.update()
        new_theme = theme_manager.current_theme
        self.assertNotEqual(current_theme, new_theme)
        # Toggle back
        self.app.toggle_theme()
        self.root.update()
        self.assertEqual(theme_manager.current_theme, current_theme)

    def test_race_window_creation(self):
        race_win = RaceWindow(self.root, [10, 20, 30, 40])
        self.root.update()
        race_win.destroy()

    def test_quiz_window_creation(self):
        quiz_win = QuizWindow(self.root)
        self.root.update()
        quiz_win.destroy()


if __name__ == "__main__":
    unittest.main()
