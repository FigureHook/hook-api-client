from typing import Any, Dict, Optional, Union

import httpx

from ...client import AuthenticatedClient
from ...models.http_validation_error import HTTPValidationError
from ...models.release_ticket_create import ReleaseTicketCreate
from ...models.release_ticket_info import ReleaseTicketInfo
from ...types import Response


def _get_kwargs(
    *,
    client: AuthenticatedClient,
    json_body: ReleaseTicketCreate,
) -> Dict[str, Any]:
    url = "{}/api/v1/release-tickets/".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    json_json_body = json_body.to_dict()

    return {
        "method": "post",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "json": json_json_body,
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[HTTPValidationError, ReleaseTicketInfo]]:
    if response.status_code == 201:
        response_201 = ReleaseTicketInfo.from_dict(response.json())

        return response_201
    if response.status_code == 422:
        response_422 = HTTPValidationError.from_dict(response.json())

        return response_422
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[HTTPValidationError, ReleaseTicketInfo]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    json_body: ReleaseTicketCreate,
) -> Response[Union[HTTPValidationError, ReleaseTicketInfo]]:
    """Create Release Ticket

    Args:
        json_body (ReleaseTicketCreate):

    Returns:
        Response[Union[HTTPValidationError, ReleaseTicketInfo]]
    """

    kwargs = _get_kwargs(
        client=client,
        json_body=json_body,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: AuthenticatedClient,
    json_body: ReleaseTicketCreate,
) -> Optional[Union[HTTPValidationError, ReleaseTicketInfo]]:
    """Create Release Ticket

    Args:
        json_body (ReleaseTicketCreate):

    Returns:
        Response[Union[HTTPValidationError, ReleaseTicketInfo]]
    """

    return sync_detailed(
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    json_body: ReleaseTicketCreate,
) -> Response[Union[HTTPValidationError, ReleaseTicketInfo]]:
    """Create Release Ticket

    Args:
        json_body (ReleaseTicketCreate):

    Returns:
        Response[Union[HTTPValidationError, ReleaseTicketInfo]]
    """

    kwargs = _get_kwargs(
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    json_body: ReleaseTicketCreate,
) -> Optional[Union[HTTPValidationError, ReleaseTicketInfo]]:
    """Create Release Ticket

    Args:
        json_body (ReleaseTicketCreate):

    Returns:
        Response[Union[HTTPValidationError, ReleaseTicketInfo]]
    """

    return (
        await asyncio_detailed(
            client=client,
            json_body=json_body,
        )
    ).parsed
