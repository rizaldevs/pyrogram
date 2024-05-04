#  Pyrogram - Telegram MTProto API Client Library for Python
#  Copyright (C) 2017-present Dan <https://github.com/delivrance>
#
#  This file is part of Pyrogram.
#
#  Pyrogram is free software: you can redistribute it and/or modify
#  it under the terms of the GNU Lesser General Public License as published
#  by the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  Pyrogram is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU Lesser General Public License for more details.
#
#  You should have received a copy of the GNU Lesser General Public License
#  along with Pyrogram.  If not, see <http://www.gnu.org/licenses/>.

from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any

# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #


class ReactionCount(TLObject):  # type: ignore
    """This object is a constructor of the base type :obj:`~pyrogram.raw.base.ReactionCount`.

    Details:
        - Layer: ``140``
        - ID: ``0x6fb250d1``

    Parameters:
        reaction: ``str``
        count: ``int`` ``32-bit``
        chosen (optional): ``bool``
    """

    __slots__: List[str] = ["reaction", "count", "chosen"]

    ID = 0x6fb250d1
    QUALNAME = "types.ReactionCount"

    def __init__(self, *, reaction: str, count: int, chosen: Optional[bool] = None) -> None:
        self.reaction = reaction  # string
        self.count = count  # int
        self.chosen = chosen  # flags.0?true

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ReactionCount":
        
        flags = Int.read(b)
        
        chosen = True if flags & (1 << 0) else False
        reaction = String.read(b)
        
        count = Int.read(b)
        
        return ReactionCount(reaction=reaction, count=count, chosen=chosen)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.chosen else 0
        b.write(Int(flags))
        
        b.write(String(self.reaction))
        
        b.write(Int(self.count))
        
        return b.getvalue()
