import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.webhook_currency import WebhookCurrency
from ..models.webhook_lang import WebhookLang
from ..types import UNSET, Unset

T = TypeVar("T", bound="DecryptedWebhookInDB")


@attr.s(auto_attribs=True)
class DecryptedWebhookInDB:
    """
    Attributes:
        id (str):
        token (str):
        channel_id (str):
        guild_id (str):
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
        decrypted_token (str):
        is_nsfw (Union[Unset, bool]):  Default: True.
        lang (Union[Unset, WebhookLang]): An enumeration. Default: WebhookLang.EN.
        currency (Union[Unset, WebhookCurrency]): An enumeration. Default: WebhookCurrency.JPY.
        is_existed (Union[Unset, None, bool]):
    """

    id: str
    token: str
    channel_id: str
    guild_id: str
    created_at: datetime.datetime
    updated_at: datetime.datetime
    decrypted_token: str
    is_nsfw: Union[Unset, bool] = True
    lang: Union[Unset, WebhookLang] = WebhookLang.EN
    currency: Union[Unset, WebhookCurrency] = WebhookCurrency.JPY
    is_existed: Union[Unset, None, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        token = self.token
        channel_id = self.channel_id
        guild_id = self.guild_id
        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        decrypted_token = self.decrypted_token
        is_nsfw = self.is_nsfw
        lang: Union[Unset, str] = UNSET
        if not isinstance(self.lang, Unset):
            lang = self.lang.value

        currency: Union[Unset, str] = UNSET
        if not isinstance(self.currency, Unset):
            currency = self.currency.value

        is_existed = self.is_existed

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "token": token,
                "channel_id": channel_id,
                "guild_id": guild_id,
                "created_at": created_at,
                "updated_at": updated_at,
                "decrypted_token": decrypted_token,
            }
        )
        if is_nsfw is not UNSET:
            field_dict["is_nsfw"] = is_nsfw
        if lang is not UNSET:
            field_dict["lang"] = lang
        if currency is not UNSET:
            field_dict["currency"] = currency
        if is_existed is not UNSET:
            field_dict["is_existed"] = is_existed

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        token = d.pop("token")

        channel_id = d.pop("channel_id")

        guild_id = d.pop("guild_id")

        created_at = isoparse(d.pop("created_at"))

        updated_at = isoparse(d.pop("updated_at"))

        decrypted_token = d.pop("decrypted_token")

        is_nsfw = d.pop("is_nsfw", UNSET)

        _lang = d.pop("lang", UNSET)
        lang: Union[Unset, WebhookLang]
        if isinstance(_lang, Unset):
            lang = UNSET
        else:
            lang = WebhookLang(_lang)

        _currency = d.pop("currency", UNSET)
        currency: Union[Unset, WebhookCurrency]
        if isinstance(_currency, Unset):
            currency = UNSET
        else:
            currency = WebhookCurrency(_currency)

        is_existed = d.pop("is_existed", UNSET)

        decrypted_webhook_in_db = cls(
            id=id,
            token=token,
            channel_id=channel_id,
            guild_id=guild_id,
            created_at=created_at,
            updated_at=updated_at,
            decrypted_token=decrypted_token,
            is_nsfw=is_nsfw,
            lang=lang,
            currency=currency,
            is_existed=is_existed,
        )

        decrypted_webhook_in_db.additional_properties = d
        return decrypted_webhook_in_db

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
