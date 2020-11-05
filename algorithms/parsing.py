from ast_algorithms.data_structures.tree import BaseTree as Tree
from ast_algorithms.algorithms.utility import (
    all_function_declarations_generator
)
from ast_algorithms.algorithms.__parsing__ import (
    __parse_function__
)

from typing import List, Any, Generator
from clang import cindex


def get_translation_unit_index(path_to_file: str, **kwargs) -> cindex.TranslationUnit:
    return cindex.Index.create().parse(path_to_file, **kwargs)


def parse_translation_unit_generator(unit: cindex.TranslationUnit) -> Generator[Tree, Any, None]:
    for function_declaration in all_function_declarations_generator(unit.cursor):
        yield __parse_function__(function_declaration)


def parse_translation_unit(unit: cindex.TranslationUnit) -> List[Tree]:
    return list(parse_translation_unit_generator(unit))
