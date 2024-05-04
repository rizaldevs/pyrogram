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


class PaymentForm(TLObject):  # type: ignore
    """This object is a constructor of the base type :obj:`~pyrogram.raw.base.payments.PaymentForm`.

    Details:
        - Layer: ``140``
        - ID: ``0x1694761b``

    Parameters:
        form_id: ``int`` ``64-bit``
        bot_id: ``int`` ``64-bit``
        invoice: :obj:`Invoice <pyrogram.raw.base.Invoice>`
        provider_id: ``int`` ``64-bit``
        url: ``str``
        users: List of :obj:`User <pyrogram.raw.base.User>`
        can_save_credentials (optional): ``bool``
        password_missing (optional): ``bool``
        native_provider (optional): ``str``
        native_params (optional): :obj:`DataJSON <pyrogram.raw.base.DataJSON>`
        saved_info (optional): :obj:`PaymentRequestedInfo <pyrogram.raw.base.PaymentRequestedInfo>`
        saved_credentials (optional): :obj:`PaymentSavedCredentials <pyrogram.raw.base.PaymentSavedCredentials>`

    See Also:
        This object can be returned by 1 method:

        .. hlist::
            :columns: 2

            - :obj:`payments.GetPaymentForm <pyrogram.raw.functions.payments.GetPaymentForm>`
    """

    __slots__: List[str] = ["form_id", "bot_id", "invoice", "provider_id", "url", "users", "can_save_credentials", "password_missing", "native_provider", "native_params", "saved_info", "saved_credentials"]

    ID = 0x1694761b
    QUALNAME = "types.payments.PaymentForm"

    def __init__(self, *, form_id: int, bot_id: int, invoice: "raw.base.Invoice", provider_id: int, url: str, users: List["raw.base.User"], can_save_credentials: Optional[bool] = None, password_missing: Optional[bool] = None, native_provider: Optional[str] = None, native_params: "raw.base.DataJSON" = None, saved_info: "raw.base.PaymentRequestedInfo" = None, saved_credentials: "raw.base.PaymentSavedCredentials" = None) -> None:
        self.form_id = form_id  # long
        self.bot_id = bot_id  # long
        self.invoice = invoice  # Invoice
        self.provider_id = provider_id  # long
        self.url = url  # string
        self.users = users  # Vector<User>
        self.can_save_credentials = can_save_credentials  # flags.2?true
        self.password_missing = password_missing  # flags.3?true
        self.native_provider = native_provider  # flags.4?string
        self.native_params = native_params  # flags.4?DataJSON
        self.saved_info = saved_info  # flags.0?PaymentRequestedInfo
        self.saved_credentials = saved_credentials  # flags.1?PaymentSavedCredentials

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "PaymentForm":
        
        flags = Int.read(b)
        
        can_save_credentials = True if flags & (1 << 2) else False
        password_missing = True if flags & (1 << 3) else False
        form_id = Long.read(b)
        
        bot_id = Long.read(b)
        
        invoice = TLObject.read(b)
        
        provider_id = Long.read(b)
        
        url = String.read(b)
        
        native_provider = String.read(b) if flags & (1 << 4) else None
        native_params = TLObject.read(b) if flags & (1 << 4) else None
        
        saved_info = TLObject.read(b) if flags & (1 << 0) else None
        
        saved_credentials = TLObject.read(b) if flags & (1 << 1) else None
        
        users = TLObject.read(b)
        
        return PaymentForm(form_id=form_id, bot_id=bot_id, invoice=invoice, provider_id=provider_id, url=url, users=users, can_save_credentials=can_save_credentials, password_missing=password_missing, native_provider=native_provider, native_params=native_params, saved_info=saved_info, saved_credentials=saved_credentials)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 2) if self.can_save_credentials else 0
        flags |= (1 << 3) if self.password_missing else 0
        flags |= (1 << 4) if self.native_provider is not None else 0
        flags |= (1 << 4) if self.native_params is not None else 0
        flags |= (1 << 0) if self.saved_info is not None else 0
        flags |= (1 << 1) if self.saved_credentials is not None else 0
        b.write(Int(flags))
        
        b.write(Long(self.form_id))
        
        b.write(Long(self.bot_id))
        
        b.write(self.invoice.write())
        
        b.write(Long(self.provider_id))
        
        b.write(String(self.url))
        
        if self.native_provider is not None:
            b.write(String(self.native_provider))
        
        if self.native_params is not None:
            b.write(self.native_params.write())
        
        if self.saved_info is not None:
            b.write(self.saved_info.write())
        
        if self.saved_credentials is not None:
            b.write(self.saved_credentials.write())
        
        b.write(Vector(self.users))
        
        return b.getvalue()
