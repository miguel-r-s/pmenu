#! /usr/bin/python3

import sys
import argparse

def parse_options(args):

    input_file = sys.stdin if args.input_file == 'stdin' else open(args.input_file)
    return input_file.readlines()

def display_options(options):

    # Hijack stdout
    sys.stdout = open('/dev/tty', 'w')

    for n, inpt in enumerate(options):
        print(f'{n}. {inpt.strip()}')

def pick(options):

    # Hijack stdin
    sys.stdin = open('/dev/tty')
    return [options[int(c)] for c in input('choice: ').split()]

def output_options(choices):

    with open('/dev/stdout', 'w') as f_out:
        for choice in choices:
            f_out.write(choice)

def parse_cli_args():

    parser = argparse.ArgumentParser(
            description='pmenu: a cli tool inspired by suckless\' dmenu')
    parser.add_argument('--input_file', '-f', default='stdin')
    return parser.parse_args()

def pmenu():
   
    cli_args = parse_cli_args()
    options  = parse_options(cli_args)
    display_options(options)
    output_options(pick(options))

if __name__ == "__main__":
    pmenu()
