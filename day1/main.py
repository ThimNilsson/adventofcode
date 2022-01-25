import sys
import helpers 
from inputdata import InputData

def main():
    print("This application is desinged to solve this problem:\nhttps://adventofcode.com/2021/day/1\n")

    # Verify that an argument is passed
    if len(sys.argv) < 2:
        error = "missing argument"
        helpers.usage(error)
        raise OSError(2, 'No such file or directory', '')

    inputfile_path = sys.argv[1]
    input_data = InputData(inputfile_path)
    input_data.read_input()
    input_data.inputfile_lines_to_int_list()
    input_data.calc_num_of_increases()

    print('The number of increases are {0}\n'.format(input_data.num_of_increases))

if __name__ == "__main__":
    main()
