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


class FeaturedStickers(TLObject):  # type: ignore
    """This object is a constructor of the base type :obj:`~pyrogram.raw.base.messages.FeaturedStickers`.

    Details:
        - Layer: ``140``
        - ID: ``0x84c02310``

    Parameters:
        hash: ``int`` ``64-bit``
        count: ``int`` ``32-bit``
        sets: List of :obj:`StickerSetCovered <pyrogram.raw.base.StickerSetCovered>`
        unread: List of ``int`` ``64-bit``

    See Also:
        This object can be returned by 2 methods:

        .. hlist::
            :columns: 2

            - :obj:`messages.GetFeaturedStickers <pyrogram.raw.functions.messages.GetFeaturedStickers>`
            - :obj:`messages.GetOldFeaturedStickers <pyrogram.raw.functions.messages.GetOldFeaturedStickers>`
    """

    __slots__: List[str] = ["hash", "count", "sets", "unread"]

    ID = 0x84c02310
    QUALNAME = "types.messages.FeaturedStickers"

    def __init__(self, *, hash: int, count: int, sets: List["raw.base.StickerSetCovered"], unread: List[int]) -> None:
        self.hash = hash  # long
        self.count = count  # int
        self.sets = sets  # Vector<StickerSetCovered>
        self.unread = unread  # Vector<long>

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "FeaturedStickers":
        # No flags
        
        hash = Long.read(b)
        
        count = Int.read(b)
        
        sets = TLObject.read(b)
        
        unread = TLObject.read(b, Long)
        
        return FeaturedStickers(hash=hash, count=count, sets=sets, unread=unread)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Long(self.hash))
        
        b.write(Int(self.count))
        
        b.write(Vector(self.sets))
        
        b.write(Vector(self.unread, Long))
        
        return b.getvalue()
