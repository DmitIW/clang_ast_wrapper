from clangast import parse_file
import argparse


def main(path_to_file: str) -> None:
    parsed_unit = parse_file(path_to_file)
    with open("output_trees.txt", 'w') as output_file:
        parsed_unit.show(output_file)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("file", type=str, help='path to source code file')
    args = parser.parse_args()

    path_to_file = args.file
    main(path_to_file)
