import datetime
from typing import Any, Dict, List, Type, TypeVar

import attr
from dateutil.parser import isoparse

T = TypeVar("T", bound="SourceChecksumCreate")


@attr.s(auto_attribs=True)
class SourceChecksumCreate:
    """
    Attributes:
        source (str):
        checksum (str):
        checked_at (datetime.datetime):
    """

    source: str
    checksum: str
    checked_at: datetime.datetime
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        source = self.source
        checksum = self.checksum
        checked_at = self.checked_at.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "source": source,
                "checksum": checksum,
                "checked_at": checked_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        source = d.pop("source")

        checksum = d.pop("checksum")

        checked_at = isoparse(d.pop("checked_at"))

        source_checksum_create = cls(
            source=source,
            checksum=checksum,
            checked_at=checked_at,
        )

        source_checksum_create.additional_properties = d
        return source_checksum_create

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
