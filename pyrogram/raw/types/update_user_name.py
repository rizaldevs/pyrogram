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


class UpdateUserName(TLObject):  # type: ignore
    """This object is a constructor of the base type :obj:`~pyrogram.raw.base.Update`.

    Details:
        - Layer: ``140``
        - ID: ``0xc3f202e0``

    Parameters:
        user_id: ``int`` ``64-bit``
        first_name: ``str``
        last_name: ``str``
        username: ``str``
    """

    __slots__: List[str] = ["user_id", "first_name", "last_name", "username"]

    ID = 0xc3f202e0
    QUALNAME = "types.UpdateUserName"

    def __init__(self, *, user_id: int, first_name: str, last_name: str, username: str) -> None:
        self.user_id = user_id  # long
        self.first_name = first_name  # string
        self.last_name = last_name  # string
        self.username = username  # string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UpdateUserName":
        # No flags
        
        user_id = Long.read(b)
        
        first_name = String.read(b)
        
        last_name = String.read(b)
        
        username = String.read(b)
        
        return UpdateUserName(user_id=user_id, first_name=first_name, last_name=last_name, username=username)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Long(self.user_id))
        
        b.write(String(self.first_name))
        
        b.write(String(self.last_name))
        
        b.write(String(self.username))
        
        return b.getvalue()
