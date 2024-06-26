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


class UserEmpty(TLObject):  # type: ignore
    """This object is a constructor of the base type :obj:`~pyrogram.raw.base.User`.

    Details:
        - Layer: ``140``
        - ID: ``0xd3bc4b7a``

    Parameters:
        id: ``int`` ``64-bit``

    See Also:
        This object can be returned by 4 methods:

        .. hlist::
            :columns: 2

            - :obj:`account.UpdateProfile <pyrogram.raw.functions.account.UpdateProfile>`
            - :obj:`account.UpdateUsername <pyrogram.raw.functions.account.UpdateUsername>`
            - :obj:`account.ChangePhone <pyrogram.raw.functions.account.ChangePhone>`
            - :obj:`users.GetUsers <pyrogram.raw.functions.users.GetUsers>`
    """

    __slots__: List[str] = ["id"]

    ID = 0xd3bc4b7a
    QUALNAME = "types.UserEmpty"

    def __init__(self, *, id: int) -> None:
        self.id = id  # long

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UserEmpty":
        # No flags
        
        id = Long.read(b)
        
        return UserEmpty(id=id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Long(self.id))
        
        return b.getvalue()
