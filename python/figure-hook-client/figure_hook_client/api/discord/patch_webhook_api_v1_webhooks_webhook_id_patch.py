from typing import Any, Dict, Optional, Union

import httpx

from ...client import AuthenticatedClient
from ...models.decrypted_webhook_in_db import DecryptedWebhookInDB
from ...models.http_validation_error import HTTPValidationError
from ...models.webhook_update import WebhookUpdate
from ...types import Response


def _get_kwargs(
    webhook_id: str,
    *,
    client: AuthenticatedClient,
    json_body: WebhookUpdate,
) -> Dict[str, Any]:
    url = "{}/api/v1/webhooks/{webhook_id}".format(client.base_url, webhook_id=webhook_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    json_json_body = json_body.to_dict()

    return {
        "method": "patch",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "json": json_json_body,
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[DecryptedWebhookInDB, HTTPValidationError]]:
    if response.status_code == 200:
        response_200 = DecryptedWebhookInDB.from_dict(response.json())

        return response_200
    if response.status_code == 422:
        response_422 = HTTPValidationError.from_dict(response.json())

        return response_422
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[DecryptedWebhookInDB, HTTPValidationError]]:
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
    json_body: WebhookUpdate,
) -> Response[Union[DecryptedWebhookInDB, HTTPValidationError]]:
    """Patch Webhook

    Args:
        webhook_id (str):
        json_body (WebhookUpdate):

    Returns:
        Response[Union[DecryptedWebhookInDB, HTTPValidationError]]
    """

    kwargs = _get_kwargs(
        webhook_id=webhook_id,
        client=client,
        json_body=json_body,
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
    json_body: WebhookUpdate,
) -> Optional[Union[DecryptedWebhookInDB, HTTPValidationError]]:
    """Patch Webhook

    Args:
        webhook_id (str):
        json_body (WebhookUpdate):

    Returns:
        Response[Union[DecryptedWebhookInDB, HTTPValidationError]]
    """

    return sync_detailed(
        webhook_id=webhook_id,
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    webhook_id: str,
    *,
    client: AuthenticatedClient,
    json_body: WebhookUpdate,
) -> Response[Union[DecryptedWebhookInDB, HTTPValidationError]]:
    """Patch Webhook

    Args:
        webhook_id (str):
        json_body (WebhookUpdate):

    Returns:
        Response[Union[DecryptedWebhookInDB, HTTPValidationError]]
    """

    kwargs = _get_kwargs(
        webhook_id=webhook_id,
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    webhook_id: str,
    *,
    client: AuthenticatedClient,
    json_body: WebhookUpdate,
) -> Optional[Union[DecryptedWebhookInDB, HTTPValidationError]]:
    """Patch Webhook

    Args:
        webhook_id (str):
        json_body (WebhookUpdate):

    Returns:
        Response[Union[DecryptedWebhookInDB, HTTPValidationError]]
    """

    return (
        await asyncio_detailed(
            webhook_id=webhook_id,
            client=client,
            json_body=json_body,
        )
    ).parsed
