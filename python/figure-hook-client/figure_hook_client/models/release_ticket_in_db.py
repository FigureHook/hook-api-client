import datetime
from typing import Any, Dict, List, Type, TypeVar

import attr
from dateutil.parser import isoparse

T = TypeVar("T", bound="ReleaseTicketInDB")


@attr.s(auto_attribs=True)
class ReleaseTicketInDB:
    """
    Attributes:
        id (str):
        purpose (str):
        created_at (datetime.datetime):
    """

    id: str
    purpose: str
    created_at: datetime.datetime
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        purpose = self.purpose
        created_at = self.created_at.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "purpose": purpose,
                "created_at": created_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        purpose = d.pop("purpose")

        created_at = isoparse(d.pop("created_at"))

        release_ticket_in_db = cls(
            id=id,
            purpose=purpose,
            created_at=created_at,
        )

        release_ticket_in_db.additional_properties = d
        return release_ticket_in_db

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
