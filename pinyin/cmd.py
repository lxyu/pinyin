import argparse
from pinyin import get

from pinyin import compat


def pinyin():
    parser = argparse.ArgumentParser()
    parser.add_argument("chars", help="Input chinese words")
    args = parser.parse_args()

    if not args.chars:
        parser.print_help()
        return

    print(get(compat.u(args.chars)))
