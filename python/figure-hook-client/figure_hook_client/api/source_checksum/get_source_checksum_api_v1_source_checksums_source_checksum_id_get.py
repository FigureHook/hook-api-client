from typing import Any, Dict, Optional, Union

import httpx

from ...client import AuthenticatedClient
from ...models.http_validation_error import HTTPValidationError
from ...models.source_checksum_in_db import SourceChecksumInDB
from ...types import Response


def _get_kwargs(
    source_checksum_id: int,
    *,
    client: AuthenticatedClient,
) -> Dict[str, Any]:
    url = "{}/api/v1/source-checksums/{source_checksum_id}".format(
        client.base_url, source_checksum_id=source_checksum_id
    )

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[HTTPValidationError, SourceChecksumInDB]]:
    if response.status_code == 200:
        response_200 = SourceChecksumInDB.from_dict(response.json())

        return response_200
    if response.status_code == 422:
        response_422 = HTTPValidationError.from_dict(response.json())

        return response_422
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[HTTPValidationError, SourceChecksumInDB]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    source_checksum_id: int,
    *,
    client: AuthenticatedClient,
) -> Response[Union[HTTPValidationError, SourceChecksumInDB]]:
    """Get Source Checksum

    Args:
        source_checksum_id (int):

    Returns:
        Response[Union[HTTPValidationError, SourceChecksumInDB]]
    """

    kwargs = _get_kwargs(
        source_checksum_id=source_checksum_id,
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    source_checksum_id: int,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[HTTPValidationError, SourceChecksumInDB]]:
    """Get Source Checksum

    Args:
        source_checksum_id (int):

    Returns:
        Response[Union[HTTPValidationError, SourceChecksumInDB]]
    """

    return sync_detailed(
        source_checksum_id=source_checksum_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    source_checksum_id: int,
    *,
    client: AuthenticatedClient,
) -> Response[Union[HTTPValidationError, SourceChecksumInDB]]:
    """Get Source Checksum

    Args:
        source_checksum_id (int):

    Returns:
        Response[Union[HTTPValidationError, SourceChecksumInDB]]
    """

    kwargs = _get_kwargs(
        source_checksum_id=source_checksum_id,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    source_checksum_id: int,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[HTTPValidationError, SourceChecksumInDB]]:
    """Get Source Checksum

    Args:
        source_checksum_id (int):

    Returns:
        Response[Union[HTTPValidationError, SourceChecksumInDB]]
    """

    return (
        await asyncio_detailed(
            source_checksum_id=source_checksum_id,
            client=client,
        )
    ).parsed
