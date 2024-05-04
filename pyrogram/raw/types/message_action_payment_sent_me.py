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


class MessageActionPaymentSentMe(TLObject):  # type: ignore
    """This object is a constructor of the base type :obj:`~pyrogram.raw.base.MessageAction`.

    Details:
        - Layer: ``140``
        - ID: ``0x8f31b327``

    Parameters:
        currency: ``str``
        total_amount: ``int`` ``64-bit``
        payload: ``bytes``
        charge: :obj:`PaymentCharge <pyrogram.raw.base.PaymentCharge>`
        info (optional): :obj:`PaymentRequestedInfo <pyrogram.raw.base.PaymentRequestedInfo>`
        shipping_option_id (optional): ``str``
    """

    __slots__: List[str] = ["currency", "total_amount", "payload", "charge", "info", "shipping_option_id"]

    ID = 0x8f31b327
    QUALNAME = "types.MessageActionPaymentSentMe"

    def __init__(self, *, currency: str, total_amount: int, payload: bytes, charge: "raw.base.PaymentCharge", info: "raw.base.PaymentRequestedInfo" = None, shipping_option_id: Optional[str] = None) -> None:
        self.currency = currency  # string
        self.total_amount = total_amount  # long
        self.payload = payload  # bytes
        self.charge = charge  # PaymentCharge
        self.info = info  # flags.0?PaymentRequestedInfo
        self.shipping_option_id = shipping_option_id  # flags.1?string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "MessageActionPaymentSentMe":
        
        flags = Int.read(b)
        
        currency = String.read(b)
        
        total_amount = Long.read(b)
        
        payload = Bytes.read(b)
        
        info = TLObject.read(b) if flags & (1 << 0) else None
        
        shipping_option_id = String.read(b) if flags & (1 << 1) else None
        charge = TLObject.read(b)
        
        return MessageActionPaymentSentMe(currency=currency, total_amount=total_amount, payload=payload, charge=charge, info=info, shipping_option_id=shipping_option_id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.info is not None else 0
        flags |= (1 << 1) if self.shipping_option_id is not None else 0
        b.write(Int(flags))
        
        b.write(String(self.currency))
        
        b.write(Long(self.total_amount))
        
        b.write(Bytes(self.payload))
        
        if self.info is not None:
            b.write(self.info.write())
        
        if self.shipping_option_id is not None:
            b.write(String(self.shipping_option_id))
        
        b.write(self.charge.write())
        
        return b.getvalue()
