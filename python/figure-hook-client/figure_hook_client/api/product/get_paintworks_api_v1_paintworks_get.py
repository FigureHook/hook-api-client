from typing import Any, Dict, Optional, Union

import httpx

from ...client import AuthenticatedClient
from ...models.http_validation_error import HTTPValidationError
from ...models.page_worker_in_db import PageWorkerInDB
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: AuthenticatedClient,
    page: Union[Unset, None, int] = 1,
    size: Union[Unset, None, int] = 50,
) -> Dict[str, Any]:
    url = "{}/api/v1/paintworks/".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["page"] = page

    params["size"] = size

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[HTTPValidationError, PageWorkerInDB]]:
    if response.status_code == 200:
        response_200 = PageWorkerInDB.from_dict(response.json())

        return response_200
    if response.status_code == 422:
        response_422 = HTTPValidationError.from_dict(response.json())

        return response_422
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[HTTPValidationError, PageWorkerInDB]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    page: Union[Unset, None, int] = 1,
    size: Union[Unset, None, int] = 50,
) -> Response[Union[HTTPValidationError, PageWorkerInDB]]:
    """Get Paintworks

    Args:
        page (Union[Unset, None, int]):  Default: 1.
        size (Union[Unset, None, int]):  Default: 50.

    Returns:
        Response[Union[HTTPValidationError, PageWorkerInDB]]
    """

    kwargs = _get_kwargs(
        client=client,
        page=page,
        size=size,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: AuthenticatedClient,
    page: Union[Unset, None, int] = 1,
    size: Union[Unset, None, int] = 50,
) -> Optional[Union[HTTPValidationError, PageWorkerInDB]]:
    """Get Paintworks

    Args:
        page (Union[Unset, None, int]):  Default: 1.
        size (Union[Unset, None, int]):  Default: 50.

    Returns:
        Response[Union[HTTPValidationError, PageWorkerInDB]]
    """

    return sync_detailed(
        client=client,
        page=page,
        size=size,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    page: Union[Unset, None, int] = 1,
    size: Union[Unset, None, int] = 50,
) -> Response[Union[HTTPValidationError, PageWorkerInDB]]:
    """Get Paintworks

    Args:
        page (Union[Unset, None, int]):  Default: 1.
        size (Union[Unset, None, int]):  Default: 50.

    Returns:
        Response[Union[HTTPValidationError, PageWorkerInDB]]
    """

    kwargs = _get_kwargs(
        client=client,
        page=page,
        size=size,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    page: Union[Unset, None, int] = 1,
    size: Union[Unset, None, int] = 50,
) -> Optional[Union[HTTPValidationError, PageWorkerInDB]]:
    """Get Paintworks

    Args:
        page (Union[Unset, None, int]):  Default: 1.
        size (Union[Unset, None, int]):  Default: 50.

    Returns:
        Response[Union[HTTPValidationError, PageWorkerInDB]]
    """

    return (
        await asyncio_detailed(
            client=client,
            page=page,
            size=size,
        )
    ).parsed
