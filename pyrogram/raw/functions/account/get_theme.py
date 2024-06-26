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


class GetTheme(TLObject):  # type: ignore
    """Telegram API method.

    Details:
        - Layer: ``140``
        - ID: ``0x8d9d742b``

    Parameters:
        format: ``str``
        theme: :obj:`InputTheme <pyrogram.raw.base.InputTheme>`
        document_id: ``int`` ``64-bit``

    Returns:
        :obj:`Theme <pyrogram.raw.base.Theme>`
    """

    __slots__: List[str] = ["format", "theme", "document_id"]

    ID = 0x8d9d742b
    QUALNAME = "functions.account.GetTheme"

    def __init__(self, *, format: str, theme: "raw.base.InputTheme", document_id: int) -> None:
        self.format = format  # string
        self.theme = theme  # InputTheme
        self.document_id = document_id  # long

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetTheme":
        # No flags
        
        format = String.read(b)
        
        theme = TLObject.read(b)
        
        document_id = Long.read(b)
        
        return GetTheme(format=format, theme=theme, document_id=document_id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(String(self.format))
        
        b.write(self.theme.write())
        
        b.write(Long(self.document_id))
        
        return b.getvalue()
