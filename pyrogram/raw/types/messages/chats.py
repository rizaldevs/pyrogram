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


class Chats(TLObject):  # type: ignore
    """This object is a constructor of the base type :obj:`~pyrogram.raw.base.messages.Chats`.

    Details:
        - Layer: ``140``
        - ID: ``0x64ff9fd5``

    Parameters:
        chats: List of :obj:`Chat <pyrogram.raw.base.Chat>`

    See Also:
        This object can be returned by 7 methods:

        .. hlist::
            :columns: 2

            - :obj:`messages.GetChats <pyrogram.raw.functions.messages.GetChats>`
            - :obj:`messages.GetCommonChats <pyrogram.raw.functions.messages.GetCommonChats>`
            - :obj:`messages.GetAllChats <pyrogram.raw.functions.messages.GetAllChats>`
            - :obj:`channels.GetChannels <pyrogram.raw.functions.channels.GetChannels>`
            - :obj:`channels.GetAdminedPublicChannels <pyrogram.raw.functions.channels.GetAdminedPublicChannels>`
            - :obj:`channels.GetLeftChannels <pyrogram.raw.functions.channels.GetLeftChannels>`
            - :obj:`channels.GetGroupsForDiscussion <pyrogram.raw.functions.channels.GetGroupsForDiscussion>`
    """

    __slots__: List[str] = ["chats"]

    ID = 0x64ff9fd5
    QUALNAME = "types.messages.Chats"

    def __init__(self, *, chats: List["raw.base.Chat"]) -> None:
        self.chats = chats  # Vector<Chat>

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "Chats":
        # No flags
        
        chats = TLObject.read(b)
        
        return Chats(chats=chats)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Vector(self.chats))
        
        return b.getvalue()
