import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.category_in_db import CategoryInDB
from ..models.company_in_db import CompanyInDB
from ..models.product_official_image_in_db import ProductOfficialImageInDB
from ..models.series_in_db import SeriesInDB
from ..models.worker_in_db import WorkerInDB
from ..types import UNSET, Unset

T = TypeVar("T", bound="ProductInDBRich")


@attr.s(auto_attribs=True)
class ProductInDBRich:
    """
    Attributes:
        id (int):
        name (str):
        rerelease (bool):
        url (str):
        checksum (str):
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
        series (SeriesInDB):
        category (CategoryInDB):
        manufacturer (CompanyInDB):
        official_images (List[ProductOfficialImageInDB]):
        size (Union[Unset, None, int]):
        scale (Union[Unset, None, int]):
        adult (Union[Unset, bool]):
        copyright_ (Union[Unset, str]):
        jan (Union[Unset, None, str]):
        order_period_start (Union[Unset, None, datetime.datetime]): This value should be an UTC timestamp.
        order_period_end (Union[Unset, None, datetime.datetime]): This value should be an UTC timestamp.
        releaser (Union[Unset, None, CompanyInDB]):
        distributer (Union[Unset, None, CompanyInDB]):
        sculptors (Union[Unset, List[WorkerInDB]]):
        paintworks (Union[Unset, List[WorkerInDB]]):
    """

    id: int
    name: str
    rerelease: bool
    url: str
    checksum: str
    created_at: datetime.datetime
    updated_at: datetime.datetime
    series: SeriesInDB
    category: CategoryInDB
    manufacturer: CompanyInDB
    official_images: List[ProductOfficialImageInDB]
    size: Union[Unset, None, int] = UNSET
    scale: Union[Unset, None, int] = UNSET
    adult: Union[Unset, bool] = False
    copyright_: Union[Unset, str] = UNSET
    jan: Union[Unset, None, str] = UNSET
    order_period_start: Union[Unset, None, datetime.datetime] = UNSET
    order_period_end: Union[Unset, None, datetime.datetime] = UNSET
    releaser: Union[Unset, None, CompanyInDB] = UNSET
    distributer: Union[Unset, None, CompanyInDB] = UNSET
    sculptors: Union[Unset, List[WorkerInDB]] = UNSET
    paintworks: Union[Unset, List[WorkerInDB]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        name = self.name
        rerelease = self.rerelease
        url = self.url
        checksum = self.checksum
        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        series = self.series.to_dict()

        category = self.category.to_dict()

        manufacturer = self.manufacturer.to_dict()

        official_images = []
        for official_images_item_data in self.official_images:
            official_images_item = official_images_item_data.to_dict()

            official_images.append(official_images_item)

        size = self.size
        scale = self.scale
        adult = self.adult
        copyright_ = self.copyright_
        jan = self.jan
        order_period_start: Union[Unset, None, str] = UNSET
        if not isinstance(self.order_period_start, Unset):
            order_period_start = self.order_period_start.isoformat() if self.order_period_start else None

        order_period_end: Union[Unset, None, str] = UNSET
        if not isinstance(self.order_period_end, Unset):
            order_period_end = self.order_period_end.isoformat() if self.order_period_end else None

        releaser: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.releaser, Unset):
            releaser = self.releaser.to_dict() if self.releaser else None

        distributer: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.distributer, Unset):
            distributer = self.distributer.to_dict() if self.distributer else None

        sculptors: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.sculptors, Unset):
            sculptors = []
            for sculptors_item_data in self.sculptors:
                sculptors_item = sculptors_item_data.to_dict()

                sculptors.append(sculptors_item)

        paintworks: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.paintworks, Unset):
            paintworks = []
            for paintworks_item_data in self.paintworks:
                paintworks_item = paintworks_item_data.to_dict()

                paintworks.append(paintworks_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "rerelease": rerelease,
                "url": url,
                "checksum": checksum,
                "created_at": created_at,
                "updated_at": updated_at,
                "series": series,
                "category": category,
                "manufacturer": manufacturer,
                "official_images": official_images,
            }
        )
        if size is not UNSET:
            field_dict["size"] = size
        if scale is not UNSET:
            field_dict["scale"] = scale
        if adult is not UNSET:
            field_dict["adult"] = adult
        if copyright_ is not UNSET:
            field_dict["copyright"] = copyright_
        if jan is not UNSET:
            field_dict["jan"] = jan
        if order_period_start is not UNSET:
            field_dict["order_period_start"] = order_period_start
        if order_period_end is not UNSET:
            field_dict["order_period_end"] = order_period_end
        if releaser is not UNSET:
            field_dict["releaser"] = releaser
        if distributer is not UNSET:
            field_dict["distributer"] = distributer
        if sculptors is not UNSET:
            field_dict["sculptors"] = sculptors
        if paintworks is not UNSET:
            field_dict["paintworks"] = paintworks

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        name = d.pop("name")

        rerelease = d.pop("rerelease")

        url = d.pop("url")

        checksum = d.pop("checksum")

        created_at = isoparse(d.pop("created_at"))

        updated_at = isoparse(d.pop("updated_at"))

        series = SeriesInDB.from_dict(d.pop("series"))

        category = CategoryInDB.from_dict(d.pop("category"))

        manufacturer = CompanyInDB.from_dict(d.pop("manufacturer"))

        official_images = []
        _official_images = d.pop("official_images")
        for official_images_item_data in _official_images:
            official_images_item = ProductOfficialImageInDB.from_dict(official_images_item_data)

            official_images.append(official_images_item)

        size = d.pop("size", UNSET)

        scale = d.pop("scale", UNSET)

        adult = d.pop("adult", UNSET)

        copyright_ = d.pop("copyright", UNSET)

        jan = d.pop("jan", UNSET)

        _order_period_start = d.pop("order_period_start", UNSET)
        order_period_start: Union[Unset, None, datetime.datetime]
        if _order_period_start is None:
            order_period_start = None
        elif isinstance(_order_period_start, Unset):
            order_period_start = UNSET
        else:
            order_period_start = isoparse(_order_period_start)

        _order_period_end = d.pop("order_period_end", UNSET)
        order_period_end: Union[Unset, None, datetime.datetime]
        if _order_period_end is None:
            order_period_end = None
        elif isinstance(_order_period_end, Unset):
            order_period_end = UNSET
        else:
            order_period_end = isoparse(_order_period_end)

        _releaser = d.pop("releaser", UNSET)
        releaser: Union[Unset, None, CompanyInDB]
        if _releaser is None:
            releaser = None
        elif isinstance(_releaser, Unset):
            releaser = UNSET
        else:
            releaser = CompanyInDB.from_dict(_releaser)

        _distributer = d.pop("distributer", UNSET)
        distributer: Union[Unset, None, CompanyInDB]
        if _distributer is None:
            distributer = None
        elif isinstance(_distributer, Unset):
            distributer = UNSET
        else:
            distributer = CompanyInDB.from_dict(_distributer)

        sculptors = []
        _sculptors = d.pop("sculptors", UNSET)
        for sculptors_item_data in _sculptors or []:
            sculptors_item = WorkerInDB.from_dict(sculptors_item_data)

            sculptors.append(sculptors_item)

        paintworks = []
        _paintworks = d.pop("paintworks", UNSET)
        for paintworks_item_data in _paintworks or []:
            paintworks_item = WorkerInDB.from_dict(paintworks_item_data)

            paintworks.append(paintworks_item)

        product_in_db_rich = cls(
            id=id,
            name=name,
            rerelease=rerelease,
            url=url,
            checksum=checksum,
            created_at=created_at,
            updated_at=updated_at,
            series=series,
            category=category,
            manufacturer=manufacturer,
            official_images=official_images,
            size=size,
            scale=scale,
            adult=adult,
            copyright_=copyright_,
            jan=jan,
            order_period_start=order_period_start,
            order_period_end=order_period_end,
            releaser=releaser,
            distributer=distributer,
            sculptors=sculptors,
            paintworks=paintworks,
        )

        product_in_db_rich.additional_properties = d
        return product_in_db_rich

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
