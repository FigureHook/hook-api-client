import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApplicationInDB")


@attr.s(auto_attribs=True)
class ApplicationInDB:
    """
    Attributes:
        name (str):
        id (str):
        token (str):
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
        last_seen_at (Union[Unset, None, datetime.datetime]):
    """

    name: str
    id: str
    token: str
    created_at: datetime.datetime
    updated_at: datetime.datetime
    last_seen_at: Union[Unset, None, datetime.datetime] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        id = self.id
        token = self.token
        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        last_seen_at: Union[Unset, None, str] = UNSET
        if not isinstance(self.last_seen_at, Unset):
            last_seen_at = self.last_seen_at.isoformat() if self.last_seen_at else None

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "id": id,
                "token": token,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )
        if last_seen_at is not UNSET:
            field_dict["last_seen_at"] = last_seen_at

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name")

        id = d.pop("id")

        token = d.pop("token")

        created_at = isoparse(d.pop("created_at"))

        updated_at = isoparse(d.pop("updated_at"))

        _last_seen_at = d.pop("last_seen_at", UNSET)
        last_seen_at: Union[Unset, None, datetime.datetime]
        if _last_seen_at is None:
            last_seen_at = None
        elif isinstance(_last_seen_at, Unset):
            last_seen_at = UNSET
        else:
            last_seen_at = isoparse(_last_seen_at)

        application_in_db = cls(
            name=name,
            id=id,
            token=token,
            created_at=created_at,
            updated_at=updated_at,
            last_seen_at=last_seen_at,
        )

        application_in_db.additional_properties = d
        return application_in_db

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
