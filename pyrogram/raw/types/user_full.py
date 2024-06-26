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


class UserFull(TLObject):  # type: ignore
    """This object is a constructor of the base type :obj:`~pyrogram.raw.base.UserFull`.

    Details:
        - Layer: ``140``
        - ID: ``0x8c72ea81``

    Parameters:
        id: ``int`` ``64-bit``
        settings: :obj:`PeerSettings <pyrogram.raw.base.PeerSettings>`
        notify_settings: :obj:`PeerNotifySettings <pyrogram.raw.base.PeerNotifySettings>`
        common_chats_count: ``int`` ``32-bit``
        blocked (optional): ``bool``
        phone_calls_available (optional): ``bool``
        phone_calls_private (optional): ``bool``
        can_pin_message (optional): ``bool``
        has_scheduled (optional): ``bool``
        video_calls_available (optional): ``bool``
        about (optional): ``str``
        profile_photo (optional): :obj:`Photo <pyrogram.raw.base.Photo>`
        bot_info (optional): :obj:`BotInfo <pyrogram.raw.base.BotInfo>`
        pinned_msg_id (optional): ``int`` ``32-bit``
        folder_id (optional): ``int`` ``32-bit``
        ttl_period (optional): ``int`` ``32-bit``
        theme_emoticon (optional): ``str``
        private_forward_name (optional): ``str``
        bot_group_admin_rights (optional): :obj:`ChatAdminRights <pyrogram.raw.base.ChatAdminRights>`
        bot_broadcast_admin_rights (optional): :obj:`ChatAdminRights <pyrogram.raw.base.ChatAdminRights>`
    """

    __slots__: List[str] = ["id", "settings", "notify_settings", "common_chats_count", "blocked", "phone_calls_available", "phone_calls_private", "can_pin_message", "has_scheduled", "video_calls_available", "about", "profile_photo", "bot_info", "pinned_msg_id", "folder_id", "ttl_period", "theme_emoticon", "private_forward_name", "bot_group_admin_rights", "bot_broadcast_admin_rights"]

    ID = 0x8c72ea81
    QUALNAME = "types.UserFull"

    def __init__(self, *, id: int, settings: "raw.base.PeerSettings", notify_settings: "raw.base.PeerNotifySettings", common_chats_count: int, blocked: Optional[bool] = None, phone_calls_available: Optional[bool] = None, phone_calls_private: Optional[bool] = None, can_pin_message: Optional[bool] = None, has_scheduled: Optional[bool] = None, video_calls_available: Optional[bool] = None, about: Optional[str] = None, profile_photo: "raw.base.Photo" = None, bot_info: "raw.base.BotInfo" = None, pinned_msg_id: Optional[int] = None, folder_id: Optional[int] = None, ttl_period: Optional[int] = None, theme_emoticon: Optional[str] = None, private_forward_name: Optional[str] = None, bot_group_admin_rights: "raw.base.ChatAdminRights" = None, bot_broadcast_admin_rights: "raw.base.ChatAdminRights" = None) -> None:
        self.id = id  # long
        self.settings = settings  # PeerSettings
        self.notify_settings = notify_settings  # PeerNotifySettings
        self.common_chats_count = common_chats_count  # int
        self.blocked = blocked  # flags.0?true
        self.phone_calls_available = phone_calls_available  # flags.4?true
        self.phone_calls_private = phone_calls_private  # flags.5?true
        self.can_pin_message = can_pin_message  # flags.7?true
        self.has_scheduled = has_scheduled  # flags.12?true
        self.video_calls_available = video_calls_available  # flags.13?true
        self.about = about  # flags.1?string
        self.profile_photo = profile_photo  # flags.2?Photo
        self.bot_info = bot_info  # flags.3?BotInfo
        self.pinned_msg_id = pinned_msg_id  # flags.6?int
        self.folder_id = folder_id  # flags.11?int
        self.ttl_period = ttl_period  # flags.14?int
        self.theme_emoticon = theme_emoticon  # flags.15?string
        self.private_forward_name = private_forward_name  # flags.16?string
        self.bot_group_admin_rights = bot_group_admin_rights  # flags.17?ChatAdminRights
        self.bot_broadcast_admin_rights = bot_broadcast_admin_rights  # flags.18?ChatAdminRights

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UserFull":
        
        flags = Int.read(b)
        
        blocked = True if flags & (1 << 0) else False
        phone_calls_available = True if flags & (1 << 4) else False
        phone_calls_private = True if flags & (1 << 5) else False
        can_pin_message = True if flags & (1 << 7) else False
        has_scheduled = True if flags & (1 << 12) else False
        video_calls_available = True if flags & (1 << 13) else False
        id = Long.read(b)
        
        about = String.read(b) if flags & (1 << 1) else None
        settings = TLObject.read(b)
        
        profile_photo = TLObject.read(b) if flags & (1 << 2) else None
        
        notify_settings = TLObject.read(b)
        
        bot_info = TLObject.read(b) if flags & (1 << 3) else None
        
        pinned_msg_id = Int.read(b) if flags & (1 << 6) else None
        common_chats_count = Int.read(b)
        
        folder_id = Int.read(b) if flags & (1 << 11) else None
        ttl_period = Int.read(b) if flags & (1 << 14) else None
        theme_emoticon = String.read(b) if flags & (1 << 15) else None
        private_forward_name = String.read(b) if flags & (1 << 16) else None
        bot_group_admin_rights = TLObject.read(b) if flags & (1 << 17) else None
        
        bot_broadcast_admin_rights = TLObject.read(b) if flags & (1 << 18) else None
        
        return UserFull(id=id, settings=settings, notify_settings=notify_settings, common_chats_count=common_chats_count, blocked=blocked, phone_calls_available=phone_calls_available, phone_calls_private=phone_calls_private, can_pin_message=can_pin_message, has_scheduled=has_scheduled, video_calls_available=video_calls_available, about=about, profile_photo=profile_photo, bot_info=bot_info, pinned_msg_id=pinned_msg_id, folder_id=folder_id, ttl_period=ttl_period, theme_emoticon=theme_emoticon, private_forward_name=private_forward_name, bot_group_admin_rights=bot_group_admin_rights, bot_broadcast_admin_rights=bot_broadcast_admin_rights)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.blocked else 0
        flags |= (1 << 4) if self.phone_calls_available else 0
        flags |= (1 << 5) if self.phone_calls_private else 0
        flags |= (1 << 7) if self.can_pin_message else 0
        flags |= (1 << 12) if self.has_scheduled else 0
        flags |= (1 << 13) if self.video_calls_available else 0
        flags |= (1 << 1) if self.about is not None else 0
        flags |= (1 << 2) if self.profile_photo is not None else 0
        flags |= (1 << 3) if self.bot_info is not None else 0
        flags |= (1 << 6) if self.pinned_msg_id is not None else 0
        flags |= (1 << 11) if self.folder_id is not None else 0
        flags |= (1 << 14) if self.ttl_period is not None else 0
        flags |= (1 << 15) if self.theme_emoticon is not None else 0
        flags |= (1 << 16) if self.private_forward_name is not None else 0
        flags |= (1 << 17) if self.bot_group_admin_rights is not None else 0
        flags |= (1 << 18) if self.bot_broadcast_admin_rights is not None else 0
        b.write(Int(flags))
        
        b.write(Long(self.id))
        
        if self.about is not None:
            b.write(String(self.about))
        
        b.write(self.settings.write())
        
        if self.profile_photo is not None:
            b.write(self.profile_photo.write())
        
        b.write(self.notify_settings.write())
        
        if self.bot_info is not None:
            b.write(self.bot_info.write())
        
        if self.pinned_msg_id is not None:
            b.write(Int(self.pinned_msg_id))
        
        b.write(Int(self.common_chats_count))
        
        if self.folder_id is not None:
            b.write(Int(self.folder_id))
        
        if self.ttl_period is not None:
            b.write(Int(self.ttl_period))
        
        if self.theme_emoticon is not None:
            b.write(String(self.theme_emoticon))
        
        if self.private_forward_name is not None:
            b.write(String(self.private_forward_name))
        
        if self.bot_group_admin_rights is not None:
            b.write(self.bot_group_admin_rights.write())
        
        if self.bot_broadcast_admin_rights is not None:
            b.write(self.bot_broadcast_admin_rights.write())
        
        return b.getvalue()
