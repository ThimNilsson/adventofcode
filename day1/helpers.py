import sys

def usage(error_msg):
    print("\n" + error_msg + "\nusage: " + sys.argv[0] + " path_to_input_file\nthe inputfile must be a new-line separated list of integers.\n", file=sys.stderr)
