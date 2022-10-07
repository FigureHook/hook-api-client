from typing import Any, Dict, Optional, Union

import httpx

from ...client import AuthenticatedClient
from ...models.category_in_db import CategoryInDB
from ...models.http_validation_error import HTTPValidationError
from ...types import Response


def _get_kwargs(
    category_id: int,
    *,
    client: AuthenticatedClient,
) -> Dict[str, Any]:
    url = "{}/api/v1/categories/{category_id}".format(client.base_url, category_id=category_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[CategoryInDB, HTTPValidationError]]:
    if response.status_code == 200:
        response_200 = CategoryInDB.from_dict(response.json())

        return response_200
    if response.status_code == 422:
        response_422 = HTTPValidationError.from_dict(response.json())

        return response_422
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[CategoryInDB, HTTPValidationError]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    category_id: int,
    *,
    client: AuthenticatedClient,
) -> Response[Union[CategoryInDB, HTTPValidationError]]:
    """Get Category

    Args:
        category_id (int):

    Returns:
        Response[Union[CategoryInDB, HTTPValidationError]]
    """

    kwargs = _get_kwargs(
        category_id=category_id,
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    category_id: int,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[CategoryInDB, HTTPValidationError]]:
    """Get Category

    Args:
        category_id (int):

    Returns:
        Response[Union[CategoryInDB, HTTPValidationError]]
    """

    return sync_detailed(
        category_id=category_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    category_id: int,
    *,
    client: AuthenticatedClient,
) -> Response[Union[CategoryInDB, HTTPValidationError]]:
    """Get Category

    Args:
        category_id (int):

    Returns:
        Response[Union[CategoryInDB, HTTPValidationError]]
    """

    kwargs = _get_kwargs(
        category_id=category_id,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    category_id: int,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[CategoryInDB, HTTPValidationError]]:
    """Get Category

    Args:
        category_id (int):

    Returns:
        Response[Union[CategoryInDB, HTTPValidationError]]
    """

    return (
        await asyncio_detailed(
            category_id=category_id,
            client=client,
        )
    ).parsed
