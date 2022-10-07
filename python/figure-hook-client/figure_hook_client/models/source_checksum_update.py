import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="SourceChecksumUpdate")


@attr.s(auto_attribs=True)
class SourceChecksumUpdate:
    """
    Attributes:
        source (Union[Unset, None, str]):
        checksum (Union[Unset, None, str]):
        checked_at (Union[Unset, None, datetime.datetime]):
    """

    source: Union[Unset, None, str] = UNSET
    checksum: Union[Unset, None, str] = UNSET
    checked_at: Union[Unset, None, datetime.datetime] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        source = self.source
        checksum = self.checksum
        checked_at: Union[Unset, None, str] = UNSET
        if not isinstance(self.checked_at, Unset):
            checked_at = self.checked_at.isoformat() if self.checked_at else None

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if source is not UNSET:
            field_dict["source"] = source
        if checksum is not UNSET:
            field_dict["checksum"] = checksum
        if checked_at is not UNSET:
            field_dict["checked_at"] = checked_at

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        source = d.pop("source", UNSET)

        checksum = d.pop("checksum", UNSET)

        _checked_at = d.pop("checked_at", UNSET)
        checked_at: Union[Unset, None, datetime.datetime]
        if _checked_at is None:
            checked_at = None
        elif isinstance(_checked_at, Unset):
            checked_at = UNSET
        else:
            checked_at = isoparse(_checked_at)

        source_checksum_update = cls(
            source=source,
            checksum=checksum,
            checked_at=checked_at,
        )

        source_checksum_update.additional_properties = d
        return source_checksum_update

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
