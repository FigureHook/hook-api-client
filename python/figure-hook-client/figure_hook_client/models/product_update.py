import datetime
from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="ProductUpdate")


@attr.s(auto_attribs=True)
class ProductUpdate:
    """
    Attributes:
        name (str):
        manufacturer (str):
        category (str):
        url (str):
        checksum (str):
        rerelease (bool):
        adult (Union[Unset, bool]):
        size (Union[Unset, None, int]):
        scale (Union[Unset, None, int]):
        order_period_start (Union[Unset, None, datetime.datetime]): This value should be an UTC timestamp.
        order_period_end (Union[Unset, None, datetime.datetime]): This value should be an UTC timestamp.
        series (Union[Unset, None, str]):
        copyright_ (Union[Unset, None, str]):
        jan (Union[Unset, None, str]):
        releaser (Union[Unset, None, str]):
        distributer (Union[Unset, None, str]):
        sculptors (Union[Unset, List[str]]):
        paintworks (Union[Unset, List[str]]):
    """

    name: str
    manufacturer: str
    category: str
    url: str
    checksum: str
    rerelease: bool
    adult: Union[Unset, bool] = False
    size: Union[Unset, None, int] = UNSET
    scale: Union[Unset, None, int] = UNSET
    order_period_start: Union[Unset, None, datetime.datetime] = UNSET
    order_period_end: Union[Unset, None, datetime.datetime] = UNSET
    series: Union[Unset, None, str] = UNSET
    copyright_: Union[Unset, None, str] = UNSET
    jan: Union[Unset, None, str] = UNSET
    releaser: Union[Unset, None, str] = UNSET
    distributer: Union[Unset, None, str] = UNSET
    sculptors: Union[Unset, List[str]] = UNSET
    paintworks: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        manufacturer = self.manufacturer
        category = self.category
        url = self.url
        checksum = self.checksum
        rerelease = self.rerelease
        adult = self.adult
        size = self.size
        scale = self.scale
        order_period_start: Union[Unset, None, str] = UNSET
        if not isinstance(self.order_period_start, Unset):
            order_period_start = self.order_period_start.isoformat() if self.order_period_start else None

        order_period_end: Union[Unset, None, str] = UNSET
        if not isinstance(self.order_period_end, Unset):
            order_period_end = self.order_period_end.isoformat() if self.order_period_end else None

        series = self.series
        copyright_ = self.copyright_
        jan = self.jan
        releaser = self.releaser
        distributer = self.distributer
        sculptors: Union[Unset, List[str]] = UNSET
        if not isinstance(self.sculptors, Unset):
            sculptors = self.sculptors

        paintworks: Union[Unset, List[str]] = UNSET
        if not isinstance(self.paintworks, Unset):
            paintworks = self.paintworks

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "manufacturer": manufacturer,
                "category": category,
                "url": url,
                "checksum": checksum,
                "rerelease": rerelease,
            }
        )
        if adult is not UNSET:
            field_dict["adult"] = adult
        if size is not UNSET:
            field_dict["size"] = size
        if scale is not UNSET:
            field_dict["scale"] = scale
        if order_period_start is not UNSET:
            field_dict["order_period_start"] = order_period_start
        if order_period_end is not UNSET:
            field_dict["order_period_end"] = order_period_end
        if series is not UNSET:
            field_dict["series"] = series
        if copyright_ is not UNSET:
            field_dict["copyright"] = copyright_
        if jan is not UNSET:
            field_dict["jan"] = jan
        if releaser is not UNSET:
            field_dict["releaser"] = releaser
        if distributer is not UNSET:
            field_dict["distributer"] = distributer
        if sculptors is not UNSET:
            field_dict["sculptors"] = sculptors
        if paintworks is not UNSET:
            field_dict["paintworks"] = paintworks

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name")

        manufacturer = d.pop("manufacturer")

        category = d.pop("category")

        url = d.pop("url")

        checksum = d.pop("checksum")

        rerelease = d.pop("rerelease")

        adult = d.pop("adult", UNSET)

        size = d.pop("size", UNSET)

        scale = d.pop("scale", UNSET)

        _order_period_start = d.pop("order_period_start", UNSET)
        order_period_start: Union[Unset, None, datetime.datetime]
        if _order_period_start is None:
            order_period_start = None
        elif isinstance(_order_period_start, Unset):
            order_period_start = UNSET
        else:
            order_period_start = isoparse(_order_period_start)

        _order_period_end = d.pop("order_period_end", UNSET)
        order_period_end: Union[Unset, None, datetime.datetime]
        if _order_period_end is None:
            order_period_end = None
        elif isinstance(_order_period_end, Unset):
            order_period_end = UNSET
        else:
            order_period_end = isoparse(_order_period_end)

        series = d.pop("series", UNSET)

        copyright_ = d.pop("copyright", UNSET)

        jan = d.pop("jan", UNSET)

        releaser = d.pop("releaser", UNSET)

        distributer = d.pop("distributer", UNSET)

        sculptors = cast(List[str], d.pop("sculptors", UNSET))

        paintworks = cast(List[str], d.pop("paintworks", UNSET))

        product_update = cls(
            name=name,
            manufacturer=manufacturer,
            category=category,
            url=url,
            checksum=checksum,
            rerelease=rerelease,
            adult=adult,
            size=size,
            scale=scale,
            order_period_start=order_period_start,
            order_period_end=order_period_end,
            series=series,
            copyright_=copyright_,
            jan=jan,
            releaser=releaser,
            distributer=distributer,
            sculptors=sculptors,
            paintworks=paintworks,
        )

        product_update.additional_properties = d
        return product_update

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
