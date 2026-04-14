from typing import TypeVar, Generic, Union, Optional, Protocol, Tuple, List, Any, Self
from types import TracebackType
from enum import Flag, Enum, auto
from dataclasses import dataclass
from abc import abstractmethod
import weakref

from ..types import Result, Ok, Err, Some


class Handle(Protocol):
    
    @abstractmethod
    def __init__(self, path: str) -> None:
        raise NotImplementedError

    @abstractmethod
    def append(self, data: str) -> None:
        raise NotImplementedError


