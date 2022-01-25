import sys
def usage(error):
    print("\n" + error + "\nusage: " + sys.argv[0] + " path_to_input_file\nthe inputfile must be a new-line separated list of integers.\n", file=sys.stderr)
