from __future__ import annotations

import sys

from wit_world import exports
import wit_world.exports.itf0_tmmdqdfhit as itf0_tmmdqdfhit

# componentize-py may resolve this module by top-level name.
sys.modules.setdefault("itf0_tmmdqdfhit", itf0_tmmdqdfhit)


class Handle(itf0_tmmdqdfhit.Handle):
    _storage: dict[str, str] = {}
    _seq: int = 0

    def __init__(self, path: str) -> None:
        self._path = path
        Handle._storage.setdefault(self._path, "")
        print(f"[dbg] py: handle.__init__ path={self._path}")

    def append(self, data: str) -> None:
        print(f"[dbg] py: handle.append begin path={self._path} data={data}")
        Handle._storage[self._path] = Handle._storage.get(self._path, "") + data
        print(
            f"[dbg] py: handle.append end path={self._path} size={len(Handle._storage[self._path])}"
        )


class Itf0Tmmdqdfhit(exports.Itf0Tmmdqdfhit):
    def open_temp(self) -> Handle:
        print("[dbg] py: open_temp begin")
        Handle._seq += 1
        h = Handle(f"mem://h-{Handle._seq}")
        print(f"[dbg] py: open_temp end path={h._path}")
        return h


class Run(exports.Run):
    def run(self) -> None:
        print("[dbg] py: run begin")
        api = Itf0Tmmdqdfhit()
        print("[dbg] py: run open_temp")
        h = api.open_temp()
        print("[dbg] py: run append")
        h.append("|py-run|")
        print("[dbg] py: run end")
        return None
