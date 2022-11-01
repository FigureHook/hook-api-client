from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.webhook_currency import WebhookCurrency
from ..models.webhook_lang import WebhookLang
from ..types import UNSET, Unset

T = TypeVar("T", bound="WebhookCreate")


@attr.s(auto_attribs=True)
class WebhookCreate:
    """
    Attributes:
        id (str):
        token (str):
        channel_id (str):
        guild_id (str):
        is_nsfw (Union[Unset, bool]):  Default: True.
        lang (Union[Unset, WebhookLang]): An enumeration. Default: WebhookLang.EN.
        currency (Union[Unset, WebhookCurrency]): An enumeration. Default: WebhookCurrency.JPY.
    """

    id: str
    token: str
    channel_id: str
    guild_id: str
    is_nsfw: Union[Unset, bool] = True
    lang: Union[Unset, WebhookLang] = WebhookLang.EN
    currency: Union[Unset, WebhookCurrency] = WebhookCurrency.JPY
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        token = self.token
        channel_id = self.channel_id
        guild_id = self.guild_id
        is_nsfw = self.is_nsfw
        lang: Union[Unset, str] = UNSET
        if not isinstance(self.lang, Unset):
            lang = self.lang.value

        currency: Union[Unset, str] = UNSET
        if not isinstance(self.currency, Unset):
            currency = self.currency.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "token": token,
                "channel_id": channel_id,
                "guild_id": guild_id,
            }
        )
        if is_nsfw is not UNSET:
            field_dict["is_nsfw"] = is_nsfw
        if lang is not UNSET:
            field_dict["lang"] = lang
        if currency is not UNSET:
            field_dict["currency"] = currency

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        token = d.pop("token")

        channel_id = d.pop("channel_id")

        guild_id = d.pop("guild_id")

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

        webhook_create = cls(
            id=id,
            token=token,
            channel_id=channel_id,
            guild_id=guild_id,
            is_nsfw=is_nsfw,
            lang=lang,
            currency=currency,
        )

        webhook_create.additional_properties = d
        return webhook_create

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
