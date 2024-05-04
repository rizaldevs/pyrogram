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


class ProlongWebView(TLObject):  # type: ignore
    """Telegram API method.

    Details:
        - Layer: ``140``
        - ID: ``0xd22ad148``

    Parameters:
        peer: :obj:`InputPeer <pyrogram.raw.base.InputPeer>`
        bot: :obj:`InputUser <pyrogram.raw.base.InputUser>`
        query_id: ``int`` ``64-bit``
        silent (optional): ``bool``
        reply_to_msg_id (optional): ``int`` ``32-bit``

    Returns:
        ``bool``
    """

    __slots__: List[str] = ["peer", "bot", "query_id", "silent", "reply_to_msg_id"]

    ID = 0xd22ad148
    QUALNAME = "functions.messages.ProlongWebView"

    def __init__(self, *, peer: "raw.base.InputPeer", bot: "raw.base.InputUser", query_id: int, silent: Optional[bool] = None, reply_to_msg_id: Optional[int] = None) -> None:
        self.peer = peer  # InputPeer
        self.bot = bot  # InputUser
        self.query_id = query_id  # long
        self.silent = silent  # flags.5?true
        self.reply_to_msg_id = reply_to_msg_id  # flags.0?int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ProlongWebView":
        
        flags = Int.read(b)
        
        silent = True if flags & (1 << 5) else False
        peer = TLObject.read(b)
        
        bot = TLObject.read(b)
        
        query_id = Long.read(b)
        
        reply_to_msg_id = Int.read(b) if flags & (1 << 0) else None
        return ProlongWebView(peer=peer, bot=bot, query_id=query_id, silent=silent, reply_to_msg_id=reply_to_msg_id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 5) if self.silent else 0
        flags |= (1 << 0) if self.reply_to_msg_id is not None else 0
        b.write(Int(flags))
        
        b.write(self.peer.write())
        
        b.write(self.bot.write())
        
        b.write(Long(self.query_id))
        
        if self.reply_to_msg_id is not None:
            b.write(Int(self.reply_to_msg_id))
        
        return b.getvalue()
