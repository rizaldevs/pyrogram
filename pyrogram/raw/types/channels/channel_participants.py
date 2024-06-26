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


class ChannelParticipants(TLObject):  # type: ignore
    """This object is a constructor of the base type :obj:`~pyrogram.raw.base.channels.ChannelParticipants`.

    Details:
        - Layer: ``140``
        - ID: ``0x9ab0feaf``

    Parameters:
        count: ``int`` ``32-bit``
        participants: List of :obj:`ChannelParticipant <pyrogram.raw.base.ChannelParticipant>`
        chats: List of :obj:`Chat <pyrogram.raw.base.Chat>`
        users: List of :obj:`User <pyrogram.raw.base.User>`

    See Also:
        This object can be returned by 1 method:

        .. hlist::
            :columns: 2

            - :obj:`channels.GetParticipants <pyrogram.raw.functions.channels.GetParticipants>`
    """

    __slots__: List[str] = ["count", "participants", "chats", "users"]

    ID = 0x9ab0feaf
    QUALNAME = "types.channels.ChannelParticipants"

    def __init__(self, *, count: int, participants: List["raw.base.ChannelParticipant"], chats: List["raw.base.Chat"], users: List["raw.base.User"]) -> None:
        self.count = count  # int
        self.participants = participants  # Vector<ChannelParticipant>
        self.chats = chats  # Vector<Chat>
        self.users = users  # Vector<User>

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ChannelParticipants":
        # No flags
        
        count = Int.read(b)
        
        participants = TLObject.read(b)
        
        chats = TLObject.read(b)
        
        users = TLObject.read(b)
        
        return ChannelParticipants(count=count, participants=participants, chats=chats, users=users)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Int(self.count))
        
        b.write(Vector(self.participants))
        
        b.write(Vector(self.chats))
        
        b.write(Vector(self.users))
        
        return b.getvalue()
