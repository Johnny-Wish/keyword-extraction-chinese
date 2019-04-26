import os
import argparse


def split(file, starting_index, name_pattern):
    with open(file) as fin:
        for idx, line in enumerate(fin.readlines()):
            with open(name_pattern.format(idx + starting_index), "w") as fout:
                fout.write(line)


if __name__ == '__main__':
    description = "a tool that splits a file into lines and stores them in individual files"
    default_fin = os.path.join("keywords", "concat-keywords")
    default_fout_pattern = os.path.join("keywords", "keywords{}.txt")

    parser = argparse.ArgumentParser(description=description)
    parser.add_argument("--fin", default=default_fin, help="input file")
    parser.add_argument("--fout-pattern", default=default_fout_pattern, help="output filename pattern")
    parser.add_argument("--starting-index", default=1, type=int, help="starting index")
    args = parser.parse_args()

    split(file=args.fin, starting_index=args.starting_index, name_pattern=args.fout_pattern)
