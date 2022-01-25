import unittest
import helpers 
from inputdata import InputData


class TestHelpers(unittest.TestCase):


    def test_read_input_valid_data(self):
        input_data = InputData("./test_files/valid_input.txt")
        input_data.read_input()
        self.assertEqual(input_data.inputfile_lines[0], "1\n")

    def test_read_input_invalid_path(self):
        input_data = InputData("./test_files/invalid_path.txt")
        with self.assertRaises(Exception):
           input_data.read_input()

    def test_read_input_empty_file(self):
        input_data = InputData("./test_files/empty_input.txt")
        with self.assertRaises(Exception):
           input_data.read_input()

    def test_inputfile_lines_to_int_list_valid_data(self):
        input_data = InputData("./test_files/valid_input.txt")
        input_data.read_input()
        input_data.inputfile_lines_to_int_list()
        self.assertEqual(input_data.int_list[0], 1)

    def test_inputfile_lines_to_int_list_invalid_input(self):
        input_data = InputData("./test_files/invalid_input.txt")
        input_data.read_input()
        with self.assertRaises(Exception):
            input_data.inputfile_lines_to_int_list()

    def test_inputfile_lines_to_int_list_empty_input(self):
        input_data = InputData("./test_files/empty_input.txt")
        with self.assertRaises(Exception):
            input_data.read_input()

    def test_calc_num_of_increases_0(self):
        input_data = InputData("./test_files/empty_input.txt")
        # Mock the data
        input_data.int_list = [3, 2, 1]
        input_data.calc_num_of_increases()
        self.assertEqual(input_data.num_of_increases, 0)

    def test_calc_num_of_increases_2(self):
        input_data = InputData("./test_files/empty_input.txt")
        # Mock the data
        input_data.int_list = [1, 2, 1, 3]
        input_data.calc_num_of_increases()
        self.assertEqual(input_data.num_of_increases, 2)


if __name__ == '__main__':
    unittest.main()
