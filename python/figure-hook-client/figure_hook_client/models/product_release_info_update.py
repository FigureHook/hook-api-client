import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="ProductReleaseInfoUpdate")


@attr.s(auto_attribs=True)
class ProductReleaseInfoUpdate:
    """
    Attributes:
        price (Union[Unset, None, int]):
        tax_including (Union[Unset, None, bool]):
        initial_release_date (Union[Unset, None, datetime.date]):
        adjusted_release_date (Union[Unset, None, datetime.date]):
        announced_at (Union[Unset, None, datetime.date]):
        shipped_at (Union[Unset, None, datetime.date]):
    """

    price: Union[Unset, None, int] = UNSET
    tax_including: Union[Unset, None, bool] = UNSET
    initial_release_date: Union[Unset, None, datetime.date] = UNSET
    adjusted_release_date: Union[Unset, None, datetime.date] = UNSET
    announced_at: Union[Unset, None, datetime.date] = UNSET
    shipped_at: Union[Unset, None, datetime.date] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        price = self.price
        tax_including = self.tax_including
        initial_release_date: Union[Unset, None, str] = UNSET
        if not isinstance(self.initial_release_date, Unset):
            initial_release_date = self.initial_release_date.isoformat() if self.initial_release_date else None

        adjusted_release_date: Union[Unset, None, str] = UNSET
        if not isinstance(self.adjusted_release_date, Unset):
            adjusted_release_date = self.adjusted_release_date.isoformat() if self.adjusted_release_date else None

        announced_at: Union[Unset, None, str] = UNSET
        if not isinstance(self.announced_at, Unset):
            announced_at = self.announced_at.isoformat() if self.announced_at else None

        shipped_at: Union[Unset, None, str] = UNSET
        if not isinstance(self.shipped_at, Unset):
            shipped_at = self.shipped_at.isoformat() if self.shipped_at else None

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if price is not UNSET:
            field_dict["price"] = price
        if tax_including is not UNSET:
            field_dict["tax_including"] = tax_including
        if initial_release_date is not UNSET:
            field_dict["initial_release_date"] = initial_release_date
        if adjusted_release_date is not UNSET:
            field_dict["adjusted_release_date"] = adjusted_release_date
        if announced_at is not UNSET:
            field_dict["announced_at"] = announced_at
        if shipped_at is not UNSET:
            field_dict["shipped_at"] = shipped_at

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        price = d.pop("price", UNSET)

        tax_including = d.pop("tax_including", UNSET)

        _initial_release_date = d.pop("initial_release_date", UNSET)
        initial_release_date: Union[Unset, None, datetime.date]
        if _initial_release_date is None:
            initial_release_date = None
        elif isinstance(_initial_release_date, Unset):
            initial_release_date = UNSET
        else:
            initial_release_date = isoparse(_initial_release_date).date()

        _adjusted_release_date = d.pop("adjusted_release_date", UNSET)
        adjusted_release_date: Union[Unset, None, datetime.date]
        if _adjusted_release_date is None:
            adjusted_release_date = None
        elif isinstance(_adjusted_release_date, Unset):
            adjusted_release_date = UNSET
        else:
            adjusted_release_date = isoparse(_adjusted_release_date).date()

        _announced_at = d.pop("announced_at", UNSET)
        announced_at: Union[Unset, None, datetime.date]
        if _announced_at is None:
            announced_at = None
        elif isinstance(_announced_at, Unset):
            announced_at = UNSET
        else:
            announced_at = isoparse(_announced_at).date()

        _shipped_at = d.pop("shipped_at", UNSET)
        shipped_at: Union[Unset, None, datetime.date]
        if _shipped_at is None:
            shipped_at = None
        elif isinstance(_shipped_at, Unset):
            shipped_at = UNSET
        else:
            shipped_at = isoparse(_shipped_at).date()

        product_release_info_update = cls(
            price=price,
            tax_including=tax_including,
            initial_release_date=initial_release_date,
            adjusted_release_date=adjusted_release_date,
            announced_at=announced_at,
            shipped_at=shipped_at,
        )

        product_release_info_update.additional_properties = d
        return product_release_info_update

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
