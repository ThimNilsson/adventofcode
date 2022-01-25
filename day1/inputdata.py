import sys
from helpers import usage

class InputData:
    path = ""
    lines = []
    int_list = []
    num_of_increases = 0

    def __init__(self, path):
        self.path = path

    def read_input(self):
        try:
            with open(self.path) as f:
                self.lines = f.readlines()
        except OSError as err:
            usage("{0}".format(err))
            raise
        if len(self.lines) == 0:
          error = "The input file is empty."
          usage(error)
          raise ValueError(error)


    def populate_int_list_from_lines(self):
        for i, val in enumerate(self.lines):
            try:
                self.int_list.append(int(val))
            except ValueError as err:
                error = "Could not convert data at line {0} to an integer.".format(i)
                usage(error)
                raise


    def calc_num_of_increases(self):
        for i, val in enumerate(self.int_list):
            if i > 0 and self.int_list[i] > self.int_list[i-1]: 
                self.num_of_increases += 1