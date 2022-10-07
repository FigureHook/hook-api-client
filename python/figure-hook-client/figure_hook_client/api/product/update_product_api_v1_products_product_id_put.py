from typing import Any, Dict, Optional, Union

import httpx

from ...client import AuthenticatedClient
from ...models.http_validation_error import HTTPValidationError
from ...models.product_in_db_rich import ProductInDBRich
from ...models.product_update import ProductUpdate
from ...types import Response


def _get_kwargs(
    product_id: int,
    *,
    client: AuthenticatedClient,
    json_body: ProductUpdate,
) -> Dict[str, Any]:
    url = "{}/api/v1/products/{product_id}".format(client.base_url, product_id=product_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    json_json_body = json_body.to_dict()

    return {
        "method": "put",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "json": json_json_body,
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[HTTPValidationError, ProductInDBRich]]:
    if response.status_code == 200:
        response_200 = ProductInDBRich.from_dict(response.json())

        return response_200
    if response.status_code == 422:
        response_422 = HTTPValidationError.from_dict(response.json())

        return response_422
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[HTTPValidationError, ProductInDBRich]]:
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
    json_body: ProductUpdate,
) -> Response[Union[HTTPValidationError, ProductInDBRich]]:
    """Update Product

    Args:
        product_id (int):
        json_body (ProductUpdate):

    Returns:
        Response[Union[HTTPValidationError, ProductInDBRich]]
    """

    kwargs = _get_kwargs(
        product_id=product_id,
        client=client,
        json_body=json_body,
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
    json_body: ProductUpdate,
) -> Optional[Union[HTTPValidationError, ProductInDBRich]]:
    """Update Product

    Args:
        product_id (int):
        json_body (ProductUpdate):

    Returns:
        Response[Union[HTTPValidationError, ProductInDBRich]]
    """

    return sync_detailed(
        product_id=product_id,
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    product_id: int,
    *,
    client: AuthenticatedClient,
    json_body: ProductUpdate,
) -> Response[Union[HTTPValidationError, ProductInDBRich]]:
    """Update Product

    Args:
        product_id (int):
        json_body (ProductUpdate):

    Returns:
        Response[Union[HTTPValidationError, ProductInDBRich]]
    """

    kwargs = _get_kwargs(
        product_id=product_id,
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    product_id: int,
    *,
    client: AuthenticatedClient,
    json_body: ProductUpdate,
) -> Optional[Union[HTTPValidationError, ProductInDBRich]]:
    """Update Product

    Args:
        product_id (int):
        json_body (ProductUpdate):

    Returns:
        Response[Union[HTTPValidationError, ProductInDBRich]]
    """

    return (
        await asyncio_detailed(
            product_id=product_id,
            client=client,
            json_body=json_body,
        )
    ).parsed
