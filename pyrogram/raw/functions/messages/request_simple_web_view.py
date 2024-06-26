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


class RequestSimpleWebView(TLObject):  # type: ignore
    """Telegram API method.

    Details:
        - Layer: ``140``
        - ID: ``0x6abb2f73``

    Parameters:
        bot: :obj:`InputUser <pyrogram.raw.base.InputUser>`
        url: ``str``
        theme_params (optional): :obj:`DataJSON <pyrogram.raw.base.DataJSON>`

    Returns:
        :obj:`SimpleWebViewResult <pyrogram.raw.base.SimpleWebViewResult>`
    """

    __slots__: List[str] = ["bot", "url", "theme_params"]

    ID = 0x6abb2f73
    QUALNAME = "functions.messages.RequestSimpleWebView"

    def __init__(self, *, bot: "raw.base.InputUser", url: str, theme_params: "raw.base.DataJSON" = None) -> None:
        self.bot = bot  # InputUser
        self.url = url  # string
        self.theme_params = theme_params  # flags.0?DataJSON

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "RequestSimpleWebView":
        
        flags = Int.read(b)
        
        bot = TLObject.read(b)
        
        url = String.read(b)
        
        theme_params = TLObject.read(b) if flags & (1 << 0) else None
        
        return RequestSimpleWebView(bot=bot, url=url, theme_params=theme_params)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.theme_params is not None else 0
        b.write(Int(flags))
        
        b.write(self.bot.write())
        
        b.write(String(self.url))
        
        if self.theme_params is not None:
            b.write(self.theme_params.write())
        
        return b.getvalue()
