from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient
from ...models.http_validation_error import HTTPValidationError
from ...types import Response


def _get_kwargs(
    webhook_id: str,
    *,
    client: AuthenticatedClient,
) -> Dict[str, Any]:
    url = "{}/api/v1/webhooks/{webhook_id}".format(client.base_url, webhook_id=webhook_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "delete",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[Any, HTTPValidationError]]:
    if response.status_code == 200:
        response_200 = cast(Any, response.json())
        return response_200
    if response.status_code == 422:
        response_422 = HTTPValidationError.from_dict(response.json())

        return response_422
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[Any, HTTPValidationError]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    webhook_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[Union[Any, HTTPValidationError]]:
    """Delete Webhook

    Args:
        webhook_id (str):

    Returns:
        Response[Union[Any, HTTPValidationError]]
    """

    kwargs = _get_kwargs(
        webhook_id=webhook_id,
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    webhook_id: str,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[Any, HTTPValidationError]]:
    """Delete Webhook

    Args:
        webhook_id (str):

    Returns:
        Response[Union[Any, HTTPValidationError]]
    """

    return sync_detailed(
        webhook_id=webhook_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    webhook_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[Union[Any, HTTPValidationError]]:
    """Delete Webhook

    Args:
        webhook_id (str):

    Returns:
        Response[Union[Any, HTTPValidationError]]
    """

    kwargs = _get_kwargs(
        webhook_id=webhook_id,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    webhook_id: str,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[Any, HTTPValidationError]]:
    """Delete Webhook

    Args:
        webhook_id (str):

    Returns:
        Response[Union[Any, HTTPValidationError]]
    """

    return (
        await asyncio_detailed(
            webhook_id=webhook_id,
            client=client,
        )
    ).parsed
