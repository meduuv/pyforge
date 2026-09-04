"""General-purpose helpers with no third-party dependencies."""

from collections.abc import Iterable, Iterator, Sequence
from typing import TypeVar

T = TypeVar("T")


def clamp(value: T, minimum: T, maximum: T) -> T:
    if minimum > maximum:
        raise ValueError("minimum cannot exceed maximum")
    return max(minimum, min(value, maximum))


def chunks(items: Sequence[T], size: int) -> Iterator[Sequence[T]]:
    if size <= 0:
        raise ValueError("size must be positive")
    for index in range(0, len(items), size):
        yield items[index:index + size]


def flatten(groups: Iterable[Iterable[T]]) -> list[T]:
    return [item for group in groups for item in group]
