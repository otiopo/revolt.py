from __future__ import annotations

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    from .member import Member
    from .user import User


__all__ = (
    "VosoFeature",
    "ApiInfo",
    "Autumn",
    "GetServerMembers",
)

class ApiFeature(TypedDict):
    enabled: bool
    url: str

class VosoFeature(ApiFeature):
    ws: str

class Features(TypedDict):
    email: bool
    invite_only: bool
    captcha: ApiFeature
    autumn: ApiFeature
    january: ApiFeature
    voso: VosoFeature

class ApiInfo(TypedDict):
    revolt: str
    features: Features
    ws: str
    app: str
    vapid: str

class Autumn(TypedDict):
    id: str

class GetServerMembers(TypedDict):
    members: list[Member]
    users: list[User]
