from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="ReleaseTicketInfo")


@attr.s(auto_attribs=True)
class ReleaseTicketInfo:
    """
    Attributes:
        id (str):
        release_count (int):
        purpose (str):
    """

    id: str
    release_count: int
    purpose: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        release_count = self.release_count
        purpose = self.purpose

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "release_count": release_count,
                "purpose": purpose,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        release_count = d.pop("release_count")

        purpose = d.pop("purpose")

        release_ticket_info = cls(
            id=id,
            release_count=release_count,
            purpose=purpose,
        )

        release_ticket_info.additional_properties = d
        return release_ticket_info

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
