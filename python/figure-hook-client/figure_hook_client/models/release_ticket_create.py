import datetime
from typing import Any, Dict, List, Type, TypeVar

import attr
from dateutil.parser import isoparse

T = TypeVar("T", bound="ReleaseTicketCreate")


@attr.s(auto_attribs=True)
class ReleaseTicketCreate:
    """
    Attributes:
        from_ (datetime.datetime):
        created_for (str):
    """

    from_: datetime.datetime
    created_for: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from_ = self.from_.isoformat()

        created_for = self.created_for

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "from": from_,
                "created_for": created_for,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        from_ = isoparse(d.pop("from"))

        created_for = d.pop("created_for")

        release_ticket_create = cls(
            from_=from_,
            created_for=created_for,
        )

        release_ticket_create.additional_properties = d
        return release_ticket_create

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
