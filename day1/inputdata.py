import sys
from helpers import usage

class InputData:
    inputfile_path = ""
    inputfile_lines = []
    int_list = []
    num_of_increases = 0

    def __init__(self, inputfile_path):
        self.inputfile_path = inputfile_path

    def read_input(self):
        try:
            with open(self.inputfile_path) as f:
                self.inputfile_lines = f.readlines()
        except OSError as err:
            usage("{0}".format(err))
            raise
        if len(self.inputfile_lines) == 0:
          error = "The input file is empty."
          usage(error)
          raise ValueError(error)


    def inputfile_lines_to_int_list(self):
        for i, val in enumerate(self.inputfile_lines):
            try:
                self.int_list.append(int(val))
            except ValueError as err:
                error = "Could not convert data at line {0} to an integer.".format(i)
                usage(error)
                raise


    def calc_num_of_increases(self):
        length = len(self.int_list)
        # the first value is skipped, since there is no previous value to compare with
        for i in range (1, length,1):
            if self.int_list[i] > self.int_list[i-1]: 
                self.num_of_increases += 1
