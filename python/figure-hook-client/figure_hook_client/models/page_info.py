from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="PageInfo")


@attr.s(auto_attribs=True)
class PageInfo:
    """
    Attributes:
        page (int):
        total_pages (int):
        total_results (int):
    """

    page: int
    total_pages: int
    total_results: int
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        page = self.page
        total_pages = self.total_pages
        total_results = self.total_results

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "page": page,
                "total_pages": total_pages,
                "total_results": total_results,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        page = d.pop("page")

        total_pages = d.pop("total_pages")

        total_results = d.pop("total_results")

        page_info = cls(
            page=page,
            total_pages=total_pages,
            total_results=total_results,
        )

        page_info.additional_properties = d
        return page_info

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
