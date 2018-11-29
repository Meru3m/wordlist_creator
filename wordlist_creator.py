# %/usr/bin/env python

"""
Wordlist Creator is a simple tool which purpose is to produce all the combinations
of words starting from a pattern.

-d pattern: Valid patterns are 'alphabet', 'numbers'

For example:

giving as first argument -> alder%%n (Each % will be substituted with the second arg)
and as second argument -> alphabet (in order to serially substitute each % with one letter of the alphabet).

Which will produce the following output:
alderaan
alderabn
alderacn
........
........
alderzzn
"""

from __future__ import print_function
import os
import sys
import string
import argparse
import itertools

alphabet = string.ascii_lowercase
numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9']


# to do: add check on dictionary, in order to increase the input combinations (custom dictionaries, etc)
#		decide how to manage when a word has non-contiguous placeholders %

def main(arguments):
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('wordPattern', help="Input word")
    parser.add_argument('-d', '--dictionary', help="Dictionary set or file", default="alphabet")

    args = parser.parse_args()
    combinations = produceList(args)
    if booleanQuery("Do you want to print all the combinations?"):
        print(combinations)


def produceList(arguments):
    outcome = []
    if (arguments.dictionary == "alphabet"):
        for letters in itertools.product(alphabet, repeat=placeHolderCounter(arguments.wordPattern)):
            outcome.append(substituter(arguments.wordPattern, letters))
    # here some code to save or print the result
    elif (arguments.dictionary == "numbers"):
        for number in itertools.product(numbers, repeat=placeHolderCounter(arguments.wordPattern)):
            outcome.append(substituter(arguments.wordPattern, number))
    else:
        try:
            file = open(arguments.dictionary) #os.path.realpath(__file__)
            for letters in itertools.product(file.read(), repeat=placeHolderCounter(arguments.wordPattern)):
                outcome.append(substituter(arguments.wordPattern, letters))
        except:
            print("Input is not a file, exit execution.")
            exit(1)
    return outcome


def substituter(*args):
    occorrence = 1
    result = str(args[0])
    for letter in args[1]:
        result = result.replace('%', letter, occorrence)
        occorrence += 1
    return result


def placeHolderCounter(word):
    return word.count('%')


def booleanQuery(question, default="no"):
    """Ask a yes/no question via input() and return their answer.

    "question" is a string that is presented to the user.
    "default" is the presumed answer if the user just hits <Enter>.
        It must be "yes" (the default), "no" or None (meaning
        an answer is required of the user).

    The "answer" return value is True for "yes" or False for "no".
    """

    valid = {"yes": True, "y": True, "ye": True,
             "no": False, "n": False}
    if default is None:
        prompt = " [y/n] "
    elif default == "yes":
        prompt = " [Y/n] "
    elif default == "no":
        prompt = " [y/N] "
    else:
        raise ValueError("invalid default answer: '%s'" % default)

    while True:
        sys.stdout.write(question + prompt)
        choice = input().lower()
        if default is not None and choice == '':
            return valid[default]
        elif choice in valid:
            return valid[choice]
        else:
            sys.stdout.write("Please respond with 'yes' or 'no' "
                             "(or 'y' or 'n').\n")


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
