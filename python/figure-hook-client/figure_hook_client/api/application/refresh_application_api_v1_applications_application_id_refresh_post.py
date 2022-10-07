from typing import Any, Dict, Optional, Union

import httpx

from ...client import AuthenticatedClient
from ...models.application_in_db import ApplicationInDB
from ...models.http_validation_error import HTTPValidationError
from ...types import Response


def _get_kwargs(
    application_id: str,
    *,
    client: AuthenticatedClient,
) -> Dict[str, Any]:
    url = "{}/api/v1/applications/{application_id}/refresh".format(client.base_url, application_id=application_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "post",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[ApplicationInDB, HTTPValidationError]]:
    if response.status_code == 200:
        response_200 = ApplicationInDB.from_dict(response.json())

        return response_200
    if response.status_code == 422:
        response_422 = HTTPValidationError.from_dict(response.json())

        return response_422
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[ApplicationInDB, HTTPValidationError]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    application_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[Union[ApplicationInDB, HTTPValidationError]]:
    """Refresh Application

    Args:
        application_id (str):

    Returns:
        Response[Union[ApplicationInDB, HTTPValidationError]]
    """

    kwargs = _get_kwargs(
        application_id=application_id,
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    application_id: str,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[ApplicationInDB, HTTPValidationError]]:
    """Refresh Application

    Args:
        application_id (str):

    Returns:
        Response[Union[ApplicationInDB, HTTPValidationError]]
    """

    return sync_detailed(
        application_id=application_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    application_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[Union[ApplicationInDB, HTTPValidationError]]:
    """Refresh Application

    Args:
        application_id (str):

    Returns:
        Response[Union[ApplicationInDB, HTTPValidationError]]
    """

    kwargs = _get_kwargs(
        application_id=application_id,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    application_id: str,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[ApplicationInDB, HTTPValidationError]]:
    """Refresh Application

    Args:
        application_id (str):

    Returns:
        Response[Union[ApplicationInDB, HTTPValidationError]]
    """

    return (
        await asyncio_detailed(
            application_id=application_id,
            client=client,
        )
    ).parsed
