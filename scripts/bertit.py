import argparse
import sys
import os

from irtools.bertit import bertit


def parse_arguments():
    def int_comma(line):
        return [int(x) for x in str(line).split(',')]

    parser = argparse.ArgumentParser(description='')
    parser.add_argument(
        '-d', '--delimiter', default='\t', help='default to \\t')
    parser.add_argument(
        '-j',
        '--threads',
        type=int,
        default=os.cpu_count() // 2,
        help='number of threads, default to half of cpu count')
    parser.add_argument(
        '-f',
        '--field',
        type=int_comma,
        help='zero-based field index to process, e.g. 0,1,2,3.')

    return parser.parse_args()


def main():
    args = parse_arguments()
    lines = bertit(sys.stdin, args.threads, args.delimiter, args.field, '\n')
    sys.stdout.writelines(lines)


if __name__ == '__main__':
    main()