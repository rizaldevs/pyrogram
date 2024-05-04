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


class ValidateRequestedInfo(TLObject):  # type: ignore
    """Telegram API method.

    Details:
        - Layer: ``140``
        - ID: ``0xdb103170``

    Parameters:
        peer: :obj:`InputPeer <pyrogram.raw.base.InputPeer>`
        msg_id: ``int`` ``32-bit``
        info: :obj:`PaymentRequestedInfo <pyrogram.raw.base.PaymentRequestedInfo>`
        save (optional): ``bool``

    Returns:
        :obj:`payments.ValidatedRequestedInfo <pyrogram.raw.base.payments.ValidatedRequestedInfo>`
    """

    __slots__: List[str] = ["peer", "msg_id", "info", "save"]

    ID = 0xdb103170
    QUALNAME = "functions.payments.ValidateRequestedInfo"

    def __init__(self, *, peer: "raw.base.InputPeer", msg_id: int, info: "raw.base.PaymentRequestedInfo", save: Optional[bool] = None) -> None:
        self.peer = peer  # InputPeer
        self.msg_id = msg_id  # int
        self.info = info  # PaymentRequestedInfo
        self.save = save  # flags.0?true

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ValidateRequestedInfo":
        
        flags = Int.read(b)
        
        save = True if flags & (1 << 0) else False
        peer = TLObject.read(b)
        
        msg_id = Int.read(b)
        
        info = TLObject.read(b)
        
        return ValidateRequestedInfo(peer=peer, msg_id=msg_id, info=info, save=save)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.save else 0
        b.write(Int(flags))
        
        b.write(self.peer.write())
        
        b.write(Int(self.msg_id))
        
        b.write(self.info.write())
        
        return b.getvalue()
