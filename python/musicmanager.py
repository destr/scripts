#!/usr/bin/env python

import os
import sys

from argparse import ArgumentParser


def main():
    parser = ArgumentParser(description="Options")
    parser.add_argument('-V', dest='various', help="Various artists")

    args = parser.parse_args()


if __name__ == "__main__":
    main()
