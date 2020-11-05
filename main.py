from clangast import get_translation_unit_index, parse_translation_unit_generator


def main(path_to_file: str) -> None:
    unit = get_translation_unit_index(path_to_file)
    with open("output_trees.txt", 'w') as output_file:
        for tree in parse_translation_unit_generator(unit):
            tree.show(output_file)


if __name__ == "__main__":
    main("/home/dmitri/CLionProjects/pie_light/filter/udp/udp.c")
