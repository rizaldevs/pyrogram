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


class SponsoredMessage(TLObject):  # type: ignore
    """This object is a constructor of the base type :obj:`~pyrogram.raw.base.SponsoredMessage`.

    Details:
        - Layer: ``140``
        - ID: ``0x3a836df8``

    Parameters:
        random_id: ``bytes``
        message: ``str``
        from_id (optional): :obj:`Peer <pyrogram.raw.base.Peer>`
        chat_invite (optional): :obj:`ChatInvite <pyrogram.raw.base.ChatInvite>`
        chat_invite_hash (optional): ``str``
        channel_post (optional): ``int`` ``32-bit``
        start_param (optional): ``str``
        entities (optional): List of :obj:`MessageEntity <pyrogram.raw.base.MessageEntity>`
    """

    __slots__: List[str] = ["random_id", "message", "from_id", "chat_invite", "chat_invite_hash", "channel_post", "start_param", "entities"]

    ID = 0x3a836df8
    QUALNAME = "types.SponsoredMessage"

    def __init__(self, *, random_id: bytes, message: str, from_id: "raw.base.Peer" = None, chat_invite: "raw.base.ChatInvite" = None, chat_invite_hash: Optional[str] = None, channel_post: Optional[int] = None, start_param: Optional[str] = None, entities: Optional[List["raw.base.MessageEntity"]] = None) -> None:
        self.random_id = random_id  # bytes
        self.message = message  # string
        self.from_id = from_id  # flags.3?Peer
        self.chat_invite = chat_invite  # flags.4?ChatInvite
        self.chat_invite_hash = chat_invite_hash  # flags.4?string
        self.channel_post = channel_post  # flags.2?int
        self.start_param = start_param  # flags.0?string
        self.entities = entities  # flags.1?Vector<MessageEntity>

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "SponsoredMessage":
        
        flags = Int.read(b)
        
        random_id = Bytes.read(b)
        
        from_id = TLObject.read(b) if flags & (1 << 3) else None
        
        chat_invite = TLObject.read(b) if flags & (1 << 4) else None
        
        chat_invite_hash = String.read(b) if flags & (1 << 4) else None
        channel_post = Int.read(b) if flags & (1 << 2) else None
        start_param = String.read(b) if flags & (1 << 0) else None
        message = String.read(b)
        
        entities = TLObject.read(b) if flags & (1 << 1) else []
        
        return SponsoredMessage(random_id=random_id, message=message, from_id=from_id, chat_invite=chat_invite, chat_invite_hash=chat_invite_hash, channel_post=channel_post, start_param=start_param, entities=entities)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 3) if self.from_id is not None else 0
        flags |= (1 << 4) if self.chat_invite is not None else 0
        flags |= (1 << 4) if self.chat_invite_hash is not None else 0
        flags |= (1 << 2) if self.channel_post is not None else 0
        flags |= (1 << 0) if self.start_param is not None else 0
        flags |= (1 << 1) if self.entities else 0
        b.write(Int(flags))
        
        b.write(Bytes(self.random_id))
        
        if self.from_id is not None:
            b.write(self.from_id.write())
        
        if self.chat_invite is not None:
            b.write(self.chat_invite.write())
        
        if self.chat_invite_hash is not None:
            b.write(String(self.chat_invite_hash))
        
        if self.channel_post is not None:
            b.write(Int(self.channel_post))
        
        if self.start_param is not None:
            b.write(String(self.start_param))
        
        b.write(String(self.message))
        
        if self.entities:
            b.write(Vector(self.entities))
        
        return b.getvalue()
