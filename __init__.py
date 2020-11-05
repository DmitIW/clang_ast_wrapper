from ast_algorithms.data_structures.node import BaseNode as Node
from ast_algorithms.data_structures.tree import BaseTree as Tree

from ast_algorithms.algorithms.parsing import (
    get_translation_unit_index, parse_translation_unit,
    parse_translation_unit_generator
)

from ast_algorithms.algorithms.__utility__ import __init_clang__

__default_path_to_library = "/usr/lib/libclang.so"

__init_clang__(__default_path_to_library)

__all__ = [
    "Node", "Tree",
    "get_translation_unit_index", "parse_translation_unit",
    "parse_translation_unit_generator"
]
