import unittest
from entities.player import *

class TestPlayer(unittest.TestCase):
        def setUp(self):
            self.player = Player()

        def test_constructor(self):
            self.assertEqual(self.player.lives, 3)
            self.assertEqual(self.player.combo, 0)
            self.assertEqual(self.player.score, 0)
            self.assertEqual(self.player.best_combo, 0)
            self.assertEqual(self.player.name, "")
            self.assertEqual(self.player.game_state, False)
            self.assertEqual(self.player.final_score, 0)

        def test_calculate_final_score(self):
            self.player.increase_combo()
            self.player._save_longest_combo()
            self.player.increase_score_normal()
            self.player.increase_score_perfect()
            self.player.calculate_final_score()
            self.assertEqual(self.player.final_score, 303)

        def test_increase_combo(self):
             self.player.increase_combo()
             self.player.increase_combo()
             self.assertEqual(self.player.combo, 2)

        def test_increase_score_normal(self):
            self.player.increase_score_normal()
            self.player.increase_score_normal()
            self.assertEqual(self.player.score, 200)

        def test_increase_score_perfect(self):
            self.player.increase_score_perfect()
            self.player.increase_score_perfect()
            self.assertEqual(self.player.score, 400)

        def test_get_rank_a(self):
            self.player.final_score = 6250
            self.assertEqual(self.player.get_rank(), "A")
            self.player.final_score = 5625
            self.assertEqual(self.player.get_rank(), "A")

        def test_get_rank_b(self):
            self.player.final_score = 5624
            self.assertEqual(self.player.get_rank(), "B")
            self.player.final_score = 5000
            self.assertEqual(self.player.get_rank(), "B")

        def test_get_rank_c(self):
            self.player.final_score = 4999
            self.assertEqual(self.player.get_rank(), "C")
            self.player.final_score = 4375
            self.assertEqual(self.player.get_rank(), "C")

        def test_get_rank_d(self):
            self.player.final_score = 4374
            self.assertEqual(self.player.get_rank(), "D")
            self.player.final_score = 1
            self.assertEqual(self.player.get_rank(), "D")
            self.player.final_score = 0
            self.assertEqual(self.player.get_rank(), "D")

        def test_add_new_nickname(self):
            self.player.add_new_nickname("ASD")
            self.assertEqual(self.player.name, "ASD")

        def test_get_name(self):
            self.player.name = "DAS"
            self.assertEqual(self.player.get_name(), "DAS")

        def test_get_final_score(self):
            self.player.final_score = 10
            self.assertEqual(self.player.get_final_score(), 10)

        def test_get_lives(self):
            self.assertEqual(self.player.get_lives(), 3)
        
        def test_decrease_lives(self):
            self.player.decrease_lives()
            self.assertEqual(self.player.lives, 2)

        def test_get_score(self):
            self.player.score = 3
            self.assertEqual(self.player.get_score(), 3)

        def test_get_game_state(self):
            self.assertEqual(self.player.get_game_state(), False)

        def test_set_game_state_start(self):
            self.player.set_game_state_start()
            self.assertEqual(self.player.game_state, True)

        def test_set_game_state_end(self):
            self.player.set_game_state_start()
            self.player.set_game_state_end()
            self.assertEqual(self.player.game_state, False)

        def test_get_longest_combo(self):
            self.player.best_combo = 10
            self.assertEqual(self.player.get_longest_combo(), 10)

        def test_get_current_combo(self):
            self.player.combo = 5
            self.assertEqual(self.player.get_current_combo(), 5)

        def test_reset_combo(self):
            self.player.combo = 2
            self.player.reset_combo()
            self.assertEqual(self.player.best_combo, 2)
            self.assertEqual(self.player.combo, 0)