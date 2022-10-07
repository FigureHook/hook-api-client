from typing import Any, Dict, List, Optional, Union

import httpx

from ...client import AuthenticatedClient
from ...models.http_validation_error import HTTPValidationError
from ...models.source_checksum_in_db import SourceChecksumInDB
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: AuthenticatedClient,
    skip: Union[Unset, None, int] = 0,
    limit: Union[Unset, None, int] = 100,
    source: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:
    url = "{}/api/v1/source-checksums/".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["skip"] = skip

    params["limit"] = limit

    params["source"] = source

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[HTTPValidationError, List[SourceChecksumInDB]]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = SourceChecksumInDB.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200
    if response.status_code == 422:
        response_422 = HTTPValidationError.from_dict(response.json())

        return response_422
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[HTTPValidationError, List[SourceChecksumInDB]]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    skip: Union[Unset, None, int] = 0,
    limit: Union[Unset, None, int] = 100,
    source: Union[Unset, None, str] = UNSET,
) -> Response[Union[HTTPValidationError, List[SourceChecksumInDB]]]:
    """Get Source Checksums

    Args:
        skip (Union[Unset, None, int]):
        limit (Union[Unset, None, int]):  Default: 100.
        source (Union[Unset, None, str]):

    Returns:
        Response[Union[HTTPValidationError, List[SourceChecksumInDB]]]
    """

    kwargs = _get_kwargs(
        client=client,
        skip=skip,
        limit=limit,
        source=source,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: AuthenticatedClient,
    skip: Union[Unset, None, int] = 0,
    limit: Union[Unset, None, int] = 100,
    source: Union[Unset, None, str] = UNSET,
) -> Optional[Union[HTTPValidationError, List[SourceChecksumInDB]]]:
    """Get Source Checksums

    Args:
        skip (Union[Unset, None, int]):
        limit (Union[Unset, None, int]):  Default: 100.
        source (Union[Unset, None, str]):

    Returns:
        Response[Union[HTTPValidationError, List[SourceChecksumInDB]]]
    """

    return sync_detailed(
        client=client,
        skip=skip,
        limit=limit,
        source=source,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    skip: Union[Unset, None, int] = 0,
    limit: Union[Unset, None, int] = 100,
    source: Union[Unset, None, str] = UNSET,
) -> Response[Union[HTTPValidationError, List[SourceChecksumInDB]]]:
    """Get Source Checksums

    Args:
        skip (Union[Unset, None, int]):
        limit (Union[Unset, None, int]):  Default: 100.
        source (Union[Unset, None, str]):

    Returns:
        Response[Union[HTTPValidationError, List[SourceChecksumInDB]]]
    """

    kwargs = _get_kwargs(
        client=client,
        skip=skip,
        limit=limit,
        source=source,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    skip: Union[Unset, None, int] = 0,
    limit: Union[Unset, None, int] = 100,
    source: Union[Unset, None, str] = UNSET,
) -> Optional[Union[HTTPValidationError, List[SourceChecksumInDB]]]:
    """Get Source Checksums

    Args:
        skip (Union[Unset, None, int]):
        limit (Union[Unset, None, int]):  Default: 100.
        source (Union[Unset, None, str]):

    Returns:
        Response[Union[HTTPValidationError, List[SourceChecksumInDB]]]
    """

    return (
        await asyncio_detailed(
            client=client,
            skip=skip,
            limit=limit,
            source=source,
        )
    ).parsed
