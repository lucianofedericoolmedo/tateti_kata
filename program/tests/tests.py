import unittest
from program.models.CustomExceptions import PositionAlreadyTakenException, PlayerMovedTwiceInARowException
from program.models.Lines import row, slash_diagonal, column, backSlash_diagonal
from program.models.Tateti import Tateti
from unittest.case import TestCase


class TaTeTiTests(TestCase):

    def setUp(self):
        self.game = Tateti()

    def tearDown(self):
        self.game = Tateti()


    def test_given_an_empty_board_when_i_put_a_cross_on_a_given_position_then_I_check_the_position_of_the_cross_is_the__given_one(
            self):
        self.game.put_cross(row(1)[1])
        self.assertTrue(self.game.board.contains_cross_in_position(row(1)[1]))

    def test_given_an_empty_board_when_i_put_a_circle_on_a_given_position_then_I_check_the_position_of_the_circle_is_the__given_one(
            self):
        self.game.put_circle(row(1)[1])
        self.assertTrue(self.game.board.contains_circle_in_position(row(1)[1]))

    def test_given_a_board_with_an_element_in_a_position_when_i_try_to_put_another_element_in_the_same_place_it_raise_PositionAlreadyTakenException(self):
        self.game.put_cross(row(1)[1])
        with self.assertRaises(PositionAlreadyTakenException):
            self.game.put_circle(row(1)[1])

    def test_given_a_game_when_a_player_try_to_move_twice_in_a_row_it_raise_PlayerMovedTwiceInARowException(self):
        self.game.put_cross(row(1)[1])
        with self.assertRaises(PlayerMovedTwiceInARowException):
            self.game.put_cross(row(1)[2])

    def test_given_a_player_that_put_circles_in_a_board_when_check_if_someone_make_diagonal_win_then_it_assert_cross_wins(self):
        self.game.put_cross(slash_diagonal()[0])
        self.game.put_circle(row(1)[2])
        self.game.put_cross(slash_diagonal()[1])
        self.game.put_circle(column(1)[2])
        self.game.put_cross(slash_diagonal()[2])

        self.assertTrue(self.game.cross_make_diagonal_winner)

    def test_given_a_player_that_put_circles_in_a_board_when_check_if_someone_make_diagonal_win_then_it_assert_circle_wins(self):
        self.game.put_circle(slash_diagonal()[0])
        self.game.put_cross(row(1)[2])
        self.game.put_circle(slash_diagonal()[1])
        self.game.put_cross(column(1)[2])
        self.game.put_circle(slash_diagonal()[2])

        self.assertTrue(self.game.circle_make_diagonal_winner)

    def test_given_a_player_that_put_circles_in_a_board_when_check_if_someone_make_inverse_diagonal_win_then_it_assert_cross_wins(self):
        self.game.put_cross(backSlash_diagonal()[0])
        self.game.put_circle(row(0)[1])
        self.game.put_cross(backSlash_diagonal()[1])
        self.game.put_circle(row(2)[1])
        self.game.put_cross(backSlash_diagonal()[2])

        self.assertTrue(self.game.cross_make_diagonal_winner)

    def test_given_a_player_that_put_circles_in_a_board_when_check_if_someone_make_inverse_diagonal_win_then_it_assert_circle_wins(self):
        self.game.put_circle(backSlash_diagonal()[0])
        self.game.put_cross(row(1)[0])
        self.game.put_circle(backSlash_diagonal()[1])
        self.game.put_cross(row(2)[0])
        self.game.put_circle(backSlash_diagonal()[2])

        self.assertTrue(self.game.circle_make_diagonal_winner)


    def test_given_a_player_that_put_cross_in_a_board_when_check_if_someone_make_horizontal_win_then_it_assert_cross_wins(self):

        self.game.put_cross(row(1)[0])
        self.game.put_circle(row(2)[1])
        self.game.put_cross(row(1)[1])
        self.game.put_circle(row(2)[2])
        self.game.put_cross(row(1)[2])

        self.assertTrue(self.game.cross_make_horizontal_win())

    def test_given_a_player_that_put_circle_in_a_board_when_check_if_someone_make_horizontal_win_then_it_assert_circle_wins(self):

        self.game.put_circle(row(1)[0])
        self.game.put_cross(row(2)[1])
        self.game.put_circle(row(1)[1])
        self.game.put_cross(row(2)[2])
        self.game.put_circle(row(1)[2])

        self.assertTrue(self.game.circle_make_horizontal_win())


    def test_given_a_player_that_put_cross_in_a_board_when_check_if_someone_make_vertical_win_then_it_assert_cross_wins(self):

        self.game.put_cross(column(0)[0])
        self.game.put_circle(row(1)[2])
        self.game.put_cross(column(0)[1])
        self.game.put_circle(row(2)[2])
        self.game.put_cross(column(0)[2])

        self.assertTrue(self.game.cross_make_vertical_win())

    def test_given_a_player_that_put_circle_in_a_board_when_check_if_someone_make_vertical_win_then_it_assert_circle_wins(self):

        self.game.put_circle(column(0)[0])
        self.game.put_cross(row(1)[2])
        self.game.put_circle(column(0)[1])
        self.game.put_cross(row(2)[2])
        self.game.put_circle(column(0)[2])

        self.assertTrue(self.game.circle_make_vertical_win())

    def test_given_a_player_that_put_a_final_circle_in_the_board_when_check_if_someone_wins_the_it_asserts_it(self):
        self.game.put_circle(row(0)[0])
        self.game.put_cross(column(1)[1])
        self.game.put_circle(row(0)[1])
        self.game.put_cross(column(2)[2])
        self.game.put_circle(row(0)[2])

        self.assertTrue(self.game.someone_win())

  
def main(self): 
    unittest.main()

if __name__ == '__main__':
    main()

