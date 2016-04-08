import unittest

from models.Board import Board
from models.CustomExceptions import PlayerMovedTwiceInARowException,PositionAlreadyTakenException
from models.Tateti import Tateti
from models.Token import Cross,Circle


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.board = Board()
        self.game = Tateti()
        self.cross = Cross()
        self.circle = Circle()
        self.first_diagonal = [(1, 1) , (2, 2), (3, 3)]
        self.second_diagonal = [(1,3), (2,2), (3,1)]

        self.first_row_first_column = (1, 1)
        self.first_row_second_column = (1, 2)
        self.second_row_second_column = (2, 2)
        self.second_row_third_column = (2, 3)
        self.third_row_first_column = (3, 1)



    def test_given_an_empty_board_when_i_put_a_cross_on_a_given_position_then_I_check_the_position_of_the_cross_is_the__given_one(
            self):
        self.game.put_cross(self.first_row_first_column)
        self.assertTrue(self.game.board.contains_cross_in_position(self.first_row_first_column))

    def test_given_an_empty_board_when_i_put_a_circle_on_a_given_position_then_I_check_the_position_of_the_circle_is_the__given_one(
            self):
        self.game.put_circle(self.first_row_first_column)
        self.assertTrue(self.game.board.contains_circle_in_position(self.first_row_first_column))

    def test_given_a_board_with_an_element_in_a_position_when_i_try_to_put_another_element_in_the_same_place_it_raise_PositionAlreadyTakenException(self):
        self.game.put_cross(self.first_row_first_column)
        with self.assertRaises(PositionAlreadyTakenException):
            self.game.put_circle(self.first_row_first_column)

    def test_given_a_game_when_a_player_try_to_move_twice_in_a_row_it_raise_PlayerMovedTwiceInARowException(self):
        self.game.put_cross(self.first_row_first_column)
        with self.assertRaises(PlayerMovedTwiceInARowException):
            self.game.put_cross(self.first_row_second_column)

    def test_given_a_player_that_put_circles_in_a_board_when_check_if_someone_make_diagonal_win_then_it_assert_cross_wins(self):
        self.game.put_cross(self.first_diagonal[0])
        self.game.put_circle(self.first_row_second_column)
        self.game.put_cross(self.first_diagonal[1])
        self.game.put_circle(self.second_row_third_column)
        self.game.put_cross(self.first_diagonal[2])

        self.assertTrue(self.game.cross_make_diagonal_winner)

    def test_given_a_player_that_put_circles_in_a_board_when_check_if_someone_make_diagonal_win_then_it_assert_circle_wins(self):
        self.game.put_circle(self.first_diagonal[0])
        self.game.put_cross(self.first_row_second_column)
        self.game.put_circle(self.first_diagonal[1])
        self.game.put_cross(self.second_row_third_column)
        self.game.put_circle(self.first_diagonal[2])

        self.assertTrue(self.game.circle_make_diagonal_winner)

    def test_given_a_player_that_put_circles_in_a_board_when_check_if_someone_make_inverse_diagonal_win_then_it_assert_cross_wins(self):
        self.game.put_cross(self.second_diagonal[0])
        self.game.put_circle(self.first_row_second_column)
        self.game.put_cross(self.second_diagonal[1])
        self.game.put_circle(self.second_row_third_column)
        self.game.put_cross(self.second_diagonal[2])

        self.assertTrue(self.game.cross_make_diagonal_winner)

    def test_given_a_player_that_put_circles_in_a_board_when_check_if_someone_make_inverse_diagonal_win_then_it_assert_circle_wins(self):
        self.game.put_circle(self.second_diagonal[0])
        self.game.put_cross(self.first_row_second_column)
        self.game.put_circle(self.second_diagonal[1])
        self.game.put_cross(self.second_row_third_column)
        self.game.put_circle(self.second_diagonal[2])

        self.assertTrue(self.game.circle_make_diagonal_winner)


    def test_given_a_player_that_put_cross_in_a_board_when_check_if_someone_make_horizontal_win_then_it_assert_cross_wins(self):

        self.game.put_cross(self.first_row_first_column)
        self.game.put_circle((2, 1))
        self.game.put_cross((1, 2))
        self.game.put_circle(self.second_row_second_column)
        self.game.put_cross(self.third_row_first_column)

        self.assertTrue(self.game.cross_make_horizontal_win())

    def test_given_a_player_that_put_circle_in_a_board_when_check_if_someone_make_horizontal_win_then_it_assert_circle_wins(self):

        self.game.put_circle(self.first_row_first_column)
        self.game.put_cross((2, 1))
        self.game.put_circle((1, 2))
        self.game.put_cross(self.second_row_second_column)
        self.game.put_circle((1, 3))

        self.assertTrue(self.game.circle_make_horizontal_win())


    def test_given_a_player_that_put_cross_in_a_board_when_check_if_someone_make_vertical_win_then_it_assert_cross_wins(self):

        self.game.put_cross(self.first_row_first_column)
        self.game.put_circle((1, 2))
        self.game.put_cross((2, 1))
        self.game.put_circle(self.second_row_second_column)
        self.game.put_cross(self.third_row_first_column)

        self.assertTrue(self.game.cross_make_vertical_win())

    def test_given_a_player_that_put_circle_in_a_board_when_check_if_someone_make_vertical_win_then_it_assert_circle_wins(self):

        self.game.put_circle(self.first_row_first_column)
        self.game.put_cross((1, 2))
        self.game.put_circle((2, 1))
        self.game.put_cross(self.second_row_second_column)
        self.game.put_circle(self.third_row_first_column)

        self.assertTrue(self.game.circle_make_vertical_win())

    def test_given_a_player_that_put_a_final_circle_in_the_board_when_check_if_someone_wins_the_it_asserts_it(self):
        self.game.put_circle(self.first_row_first_column)
        self.game.put_cross((1, 2))
        self.game.put_circle((2, 1))
        self.game.put_cross(self.second_row_second_column)
        self.game.put_circle(self.third_row_first_column)

        self.assertTrue(self.game.someone_win())



if __name__ == '__main__':
    unittest.main()

