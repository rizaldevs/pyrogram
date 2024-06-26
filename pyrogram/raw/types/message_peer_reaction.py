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


class MessagePeerReaction(TLObject):  # type: ignore
    """This object is a constructor of the base type :obj:`~pyrogram.raw.base.MessagePeerReaction`.

    Details:
        - Layer: ``140``
        - ID: ``0x51b67eff``

    Parameters:
        peer_id: :obj:`Peer <pyrogram.raw.base.Peer>`
        reaction: ``str``
        big (optional): ``bool``
        unread (optional): ``bool``
    """

    __slots__: List[str] = ["peer_id", "reaction", "big", "unread"]

    ID = 0x51b67eff
    QUALNAME = "types.MessagePeerReaction"

    def __init__(self, *, peer_id: "raw.base.Peer", reaction: str, big: Optional[bool] = None, unread: Optional[bool] = None) -> None:
        self.peer_id = peer_id  # Peer
        self.reaction = reaction  # string
        self.big = big  # flags.0?true
        self.unread = unread  # flags.1?true

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "MessagePeerReaction":
        
        flags = Int.read(b)
        
        big = True if flags & (1 << 0) else False
        unread = True if flags & (1 << 1) else False
        peer_id = TLObject.read(b)
        
        reaction = String.read(b)
        
        return MessagePeerReaction(peer_id=peer_id, reaction=reaction, big=big, unread=unread)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.big else 0
        flags |= (1 << 1) if self.unread else 0
        b.write(Int(flags))
        
        b.write(self.peer_id.write())
        
        b.write(String(self.reaction))
        
        return b.getvalue()
