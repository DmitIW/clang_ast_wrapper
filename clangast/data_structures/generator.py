from typing import Any, NoReturn, Deque, Iterator, Iterable

from collections import deque

DEBUG = True


class EndlessPipeline(object):
    def __init__(self, source: Iterable[Any]):
        self.pipeline = source

    def __next__(self) -> Any:
        for element in self.pipeline:
            return element

    def __iter__(self) -> Any:
        t = next(self)
        while t is not None:
            yield t
            t = next(self)

    def pop(self) -> Any:
        return next(self)


class DefaultStack(object):
    def __init__(self):
        self.collection: Deque[Any] = deque()

    def __len__(self) -> int:
        return len(self.collection)

    def __next__(self) -> Any:
        while len(self) != 0:
            return self.collection.pop()

    def __iadd__(self, other: Any):
        self.collection.append(other)
        return self


class StackingPipeline(EndlessPipeline):

    @staticmethod
    def _debug(method):
        global DEBUG

        def _log(_self, *args, **kwargs):
            if not DEBUG:
                return method(_self, *args, **kwargs)

            result = method(_self, *args, **kwargs)
            _self._logger.append(result)
            return result

        return _log

    def __init__(self, source: Iterable[Any], stacking_container: Iterator[Any] = None):
        super(StackingPipeline, self).__init__(source)
        if stacking_container is None:
            stacking_container = DefaultStack()
        self.stack = stacking_container
        self._logger = []

    @_debug.__get__(object)
    def __next__(self) -> Any:
        while len(self.stack) != 0:
            return next(self.stack)
        return super(StackingPipeline, self).__next__()

    @_debug.__get__(object)
    def __iter__(self) -> Any:
        t = next(self)
        while t is not None:
            yield t
            t = next(self)

    def __add__(self, other: Any):
        if type(self.pipeline) == StackingPipeline:
            self.pipeline += other
        else:
            self.stack += other
        return self

    def __iadd__(self, other: Any):
        if type(self.pipeline) == StackingPipeline:
            self.pipeline += other
        else:
            self.stack += other
        return self

    @_debug.__get__(object)
    def pop(self) -> Any:
        return next(self)
