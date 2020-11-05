from clangast import get_translation_unit_index, parse_translation_unit_generator

from clangast.algorithms.utility import get_available_token_kinds

from clangast.algorithms.__parsing__ import __MainGenerator__


def main(path_to_file: str) -> None:
    unit = get_translation_unit_index(path_to_file)
    with open("output_trees.txt", 'w') as output_file:
        for tree in parse_translation_unit_generator(unit):
            tree.show(output_file)


if __name__ == "__main__":
    t = __MainGenerator__((
        ind for ind in range(1, 10)
    ))
    print(next(t))
    print(next(t))
    print(next(t))
    for i in t:
        print(i)
    print(next(t))
    main("/home/dmitri/CLionProjects/pie_light/filter/udp/udp.c")
