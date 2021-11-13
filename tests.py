from main import numv, calculate_points
from parameterized import parameterized
import unittest


class TestCalculation(unittest.TestCase):
    @parameterized.expand([
        ["play_1", [['X'], [9, '/'], [5, '/'], [7, 2], ['X'], ['X'], ['X'], [9, 0], [8, '/'], [9, '/', 'X']],
         [20, 35, 52, 61, 91, 120, 139, 148, 167, 187]],
        ["play_2", [[1, 4], [4, 5], [6, '/'], [5, '/'], ['X'], [0, 1], [7, '/'], [6, '/'], ['X'], [2, '/', 6]],
         [5, 14, 29, 49, 60, 61, 77, 97, 117, 133]],
        ["play_3", [['X'], ['X'], ['X'], ['X'], ['X'], ['X'], ['X'], ['X'], ['X'], ['X', 'X', 'X']],
         [30, 60, 90, 120, 150, 180, 210, 240, 270, 300]],
        ["play_4", [['X'], [7, '/'], [7, 2], [9, '/'], ['X'], ['X'], ['X'], [2, 3], [6, '/'], [7, '/', 3]],
         [20, 37, 46, 66, 96, 118, 133, 138, 155, 168]],
    ])
    def test_calculate_points(self, name, game, points):
        self.assertEqual(calculate_points(game), points)


class TestConversion(unittest.TestCase):
    @parameterized.expand([
        ["digit", '5', 5],
        ["number", '51', 51],
        ["character", 'x', 'x'],
        ["string", "ananas", "ananas"],
    ])
    def test_numv(self, name, charin, charout):
        self.assertEqual(numv(charin), charout)
