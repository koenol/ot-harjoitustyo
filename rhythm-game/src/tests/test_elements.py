import unittest
from ..elements import Button

class TestButton(unittest.TestCase):
    def setUp(self):
        self.play_button = Button(0, 0, 200, 100, "Play", "play")

    def test_button_text(self):
        self.assertEqual(self.play_button.text, "Play")

    def test_button_action(self):
        self.assertEqual(self.play_button.action, "play")