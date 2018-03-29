import argparse
import sys
import time

# Commandline interface
parser = argparse.ArgumentParser()


parser.add_argument("-n", "--new",
                    action='store_true')


parser.add_argument("-u", "--update",
                    action='store_true')


parser.add_argument("-g", "--grab",
                    type=str,
                    help=None,
                    nargs="?",
                    default=".gitignore")


parser.add_argument("-f", "--file",
                    type=str,
                    help="",
                    default=None,
                    nargs="?")


parser.add_argument("-e", "--ext",
                    type=str,
                    help="",
                    default=None,
                    nargs="?")


args = parser.parse_args()

# print(vars(args))

if __name__ == '__main__':

    print(vars(args)["new"])
