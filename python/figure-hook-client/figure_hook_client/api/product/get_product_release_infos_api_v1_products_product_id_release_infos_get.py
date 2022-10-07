from typing import Any, Dict, List, Optional, Union

import httpx

from ...client import AuthenticatedClient
from ...models.http_validation_error import HTTPValidationError
from ...models.product_release_info_in_db import ProductReleaseInfoInDB
from ...types import Response


def _get_kwargs(
    product_id: int,
    *,
    client: AuthenticatedClient,
) -> Dict[str, Any]:
    url = "{}/api/v1/products/{product_id}/release-infos".format(client.base_url, product_id=product_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[HTTPValidationError, List[ProductReleaseInfoInDB]]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = ProductReleaseInfoInDB.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200
    if response.status_code == 422:
        response_422 = HTTPValidationError.from_dict(response.json())

        return response_422
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[HTTPValidationError, List[ProductReleaseInfoInDB]]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    product_id: int,
    *,
    client: AuthenticatedClient,
) -> Response[Union[HTTPValidationError, List[ProductReleaseInfoInDB]]]:
    """Get Product Release Infos

    Args:
        product_id (int):

    Returns:
        Response[Union[HTTPValidationError, List[ProductReleaseInfoInDB]]]
    """

    kwargs = _get_kwargs(
        product_id=product_id,
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    product_id: int,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[HTTPValidationError, List[ProductReleaseInfoInDB]]]:
    """Get Product Release Infos

    Args:
        product_id (int):

    Returns:
        Response[Union[HTTPValidationError, List[ProductReleaseInfoInDB]]]
    """

    return sync_detailed(
        product_id=product_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    product_id: int,
    *,
    client: AuthenticatedClient,
) -> Response[Union[HTTPValidationError, List[ProductReleaseInfoInDB]]]:
    """Get Product Release Infos

    Args:
        product_id (int):

    Returns:
        Response[Union[HTTPValidationError, List[ProductReleaseInfoInDB]]]
    """

    kwargs = _get_kwargs(
        product_id=product_id,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    product_id: int,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[HTTPValidationError, List[ProductReleaseInfoInDB]]]:
    """Get Product Release Infos

    Args:
        product_id (int):

    Returns:
        Response[Union[HTTPValidationError, List[ProductReleaseInfoInDB]]]
    """

    return (
        await asyncio_detailed(
            product_id=product_id,
            client=client,
        )
    ).parsed
