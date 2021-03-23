from maze import Maze
from unittest.mock import MagicMock, patch
from dir_consts import *
import unittest
import tkinter


class TestMaze(unittest.TestCase):
    @patch('tkinter.PhotoImage')
    def setUp(self, MockPhotoImage):
        self.app = MagicMock()
        self.maze = Maze(self.app, 800, 600)
        self.MockPhotoImage = MockPhotoImage

    def test_run(self):
        self.assertFalse(self.maze.is_movable_direction(1, 1, DIR_UP))
        self.assertTrue(self.maze.is_movable_direction(1, 1, DIR_DOWN))
        self.assertFalse(self.maze.is_movable_direction(1, 1, DIR_LEFT))
        self.assertTrue(self.maze.is_movable_direction(1, 1, DIR_RIGHT))

    def test_eat_dot(self):
        self.assertTrue(self.maze.has_dot_at(1, 1))
        self.maze.eat_dot_at(1, 1)
        self.assertFalse(self.maze.has_dot_at(1, 1))
