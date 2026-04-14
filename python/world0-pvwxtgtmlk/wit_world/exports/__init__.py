from typing import TypeVar, Generic, Union, Optional, Protocol, Tuple, List, Any, Self
from types import TracebackType
from enum import Flag, Enum, auto
from dataclasses import dataclass
from abc import abstractmethod
import weakref

from ..types import Result, Ok, Err, Some
from ..exports import itf0_tmmdqdfhit

class Run(Protocol):

    @abstractmethod
    def run(self) -> None:
        """
        Run the program.
        
        Raises: `wit_world.types.Err(None)`
        """
        raise NotImplementedError


class Itf0Tmmdqdfhit(Protocol):

    @abstractmethod
    def open_temp(self) -> itf0_tmmdqdfhit.Handle:
        raise NotImplementedError


