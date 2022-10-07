import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="ReleaseFeed")


@attr.s(auto_attribs=True)
class ReleaseFeed:
    """
    Attributes:
        product_id (int):
        release_info_id (int):
        name (str):
        source_url (str):
        is_nsfw (bool):
        is_rerelease (bool):
        series (str):
        manufacturer (str):
        image_url (str):
        size (Union[Unset, None, int]):
        scale (Union[Unset, None, int]):
        price (Union[Unset, None, int]):
        release_date (Union[Unset, None, datetime.date]):
        manufacturer_logo (Union[Unset, None, str]):
    """

    product_id: int
    release_info_id: int
    name: str
    source_url: str
    is_nsfw: bool
    is_rerelease: bool
    series: str
    manufacturer: str
    image_url: str
    size: Union[Unset, None, int] = UNSET
    scale: Union[Unset, None, int] = UNSET
    price: Union[Unset, None, int] = UNSET
    release_date: Union[Unset, None, datetime.date] = UNSET
    manufacturer_logo: Union[Unset, None, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        product_id = self.product_id
        release_info_id = self.release_info_id
        name = self.name
        source_url = self.source_url
        is_nsfw = self.is_nsfw
        is_rerelease = self.is_rerelease
        series = self.series
        manufacturer = self.manufacturer
        image_url = self.image_url
        size = self.size
        scale = self.scale
        price = self.price
        release_date: Union[Unset, None, str] = UNSET
        if not isinstance(self.release_date, Unset):
            release_date = self.release_date.isoformat() if self.release_date else None

        manufacturer_logo = self.manufacturer_logo

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "product_id": product_id,
                "release_info_id": release_info_id,
                "name": name,
                "source_url": source_url,
                "is_nsfw": is_nsfw,
                "is_rerelease": is_rerelease,
                "series": series,
                "manufacturer": manufacturer,
                "image_url": image_url,
            }
        )
        if size is not UNSET:
            field_dict["size"] = size
        if scale is not UNSET:
            field_dict["scale"] = scale
        if price is not UNSET:
            field_dict["price"] = price
        if release_date is not UNSET:
            field_dict["release_date"] = release_date
        if manufacturer_logo is not UNSET:
            field_dict["manufacturer_logo"] = manufacturer_logo

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        product_id = d.pop("product_id")

        release_info_id = d.pop("release_info_id")

        name = d.pop("name")

        source_url = d.pop("source_url")

        is_nsfw = d.pop("is_nsfw")

        is_rerelease = d.pop("is_rerelease")

        series = d.pop("series")

        manufacturer = d.pop("manufacturer")

        image_url = d.pop("image_url")

        size = d.pop("size", UNSET)

        scale = d.pop("scale", UNSET)

        price = d.pop("price", UNSET)

        _release_date = d.pop("release_date", UNSET)
        release_date: Union[Unset, None, datetime.date]
        if _release_date is None:
            release_date = None
        elif isinstance(_release_date, Unset):
            release_date = UNSET
        else:
            release_date = isoparse(_release_date).date()

        manufacturer_logo = d.pop("manufacturer_logo", UNSET)

        release_feed = cls(
            product_id=product_id,
            release_info_id=release_info_id,
            name=name,
            source_url=source_url,
            is_nsfw=is_nsfw,
            is_rerelease=is_rerelease,
            series=series,
            manufacturer=manufacturer,
            image_url=image_url,
            size=size,
            scale=scale,
            price=price,
            release_date=release_date,
            manufacturer_logo=manufacturer_logo,
        )

        release_feed.additional_properties = d
        return release_feed

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
