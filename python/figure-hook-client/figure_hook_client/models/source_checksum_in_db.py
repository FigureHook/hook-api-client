import datetime
from typing import Any, Dict, List, Type, TypeVar

import attr
from dateutil.parser import isoparse

T = TypeVar("T", bound="SourceChecksumInDB")


@attr.s(auto_attribs=True)
class SourceChecksumInDB:
    """
    Attributes:
        source (str):
        checksum (str):
        checked_at (datetime.datetime):
        id (int):
    """

    source: str
    checksum: str
    checked_at: datetime.datetime
    id: int
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        source = self.source
        checksum = self.checksum
        checked_at = self.checked_at.isoformat()

        id = self.id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "source": source,
                "checksum": checksum,
                "checked_at": checked_at,
                "id": id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        source = d.pop("source")

        checksum = d.pop("checksum")

        checked_at = isoparse(d.pop("checked_at"))

        id = d.pop("id")

        source_checksum_in_db = cls(
            source=source,
            checksum=checksum,
            checked_at=checked_at,
            id=id,
        )

        source_checksum_in_db.additional_properties = d
        return source_checksum_in_db

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
