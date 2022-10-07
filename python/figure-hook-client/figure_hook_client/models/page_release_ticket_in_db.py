from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.page_info import PageInfo
from ..models.release_ticket_in_db import ReleaseTicketInDB

T = TypeVar("T", bound="PageReleaseTicketInDB")


@attr.s(auto_attribs=True)
class PageReleaseTicketInDB:
    """
    Attributes:
        info (PageInfo):
        results (List[ReleaseTicketInDB]):
    """

    info: PageInfo
    results: List[ReleaseTicketInDB]
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        info = self.info.to_dict()

        results = []
        for results_item_data in self.results:
            results_item = results_item_data.to_dict()

            results.append(results_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "info": info,
                "results": results,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        info = PageInfo.from_dict(d.pop("info"))

        results = []
        _results = d.pop("results")
        for results_item_data in _results:
            results_item = ReleaseTicketInDB.from_dict(results_item_data)

            results.append(results_item)

        page_release_ticket_in_db = cls(
            info=info,
            results=results,
        )

        page_release_ticket_in_db.additional_properties = d
        return page_release_ticket_in_db

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
