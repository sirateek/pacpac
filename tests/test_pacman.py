from unittest.mock import MagicMock, patch
from dir_consts import *
from main import Pacman
import unittest


class TestPacman(unittest.TestCase):

    @patch("tkinter.PhotoImage")
    def setUp(self, MockPhotoImage):
        self.app = MagicMock()
        self.maze = MagicMock()

        self.maze.piece_center.return_value = (20, 60)
        self.pacman = Pacman(self.app, self.maze, 1, 1)

    def test_eat_dot(self):
        maze = self.maze
        maze.is_at_center.return_value = True
        maze.xy_to_rc.return_value = (1, 1)
        maze.has_dot_at.return_value = True
        self.pacman.update()

        self.assertTrue(maze.eat_dot_at.called)

    def test_eat_no_dot(self):
        maze = self.maze
        maze.is_at_center.return_value = True
        maze.xy_to_rc.return_value = (1, 1)
        maze.has_dot_at.return_value = False
        self.pacman.update()

        self.assertFalse(maze.eat_dot_at.called)
