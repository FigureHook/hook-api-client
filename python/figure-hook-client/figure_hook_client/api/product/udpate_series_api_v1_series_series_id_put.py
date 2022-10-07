from typing import Any, Dict, Optional, Union

import httpx

from ...client import AuthenticatedClient
from ...models.http_validation_error import HTTPValidationError
from ...models.series_in_db import SeriesInDB
from ...models.series_update import SeriesUpdate
from ...types import Response


def _get_kwargs(
    series_id: str,
    *,
    client: AuthenticatedClient,
    json_body: SeriesUpdate,
) -> Dict[str, Any]:
    url = "{}/api/v1/series/{series_id}".format(client.base_url, series_id=series_id)

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


def _parse_response(*, response: httpx.Response) -> Optional[Union[HTTPValidationError, SeriesInDB]]:
    if response.status_code == 200:
        response_200 = SeriesInDB.from_dict(response.json())

        return response_200
    if response.status_code == 422:
        response_422 = HTTPValidationError.from_dict(response.json())

        return response_422
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[HTTPValidationError, SeriesInDB]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    series_id: str,
    *,
    client: AuthenticatedClient,
    json_body: SeriesUpdate,
) -> Response[Union[HTTPValidationError, SeriesInDB]]:
    """Udpate Series

    Args:
        series_id (str):
        json_body (SeriesUpdate):

    Returns:
        Response[Union[HTTPValidationError, SeriesInDB]]
    """

    kwargs = _get_kwargs(
        series_id=series_id,
        client=client,
        json_body=json_body,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    series_id: str,
    *,
    client: AuthenticatedClient,
    json_body: SeriesUpdate,
) -> Optional[Union[HTTPValidationError, SeriesInDB]]:
    """Udpate Series

    Args:
        series_id (str):
        json_body (SeriesUpdate):

    Returns:
        Response[Union[HTTPValidationError, SeriesInDB]]
    """

    return sync_detailed(
        series_id=series_id,
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    series_id: str,
    *,
    client: AuthenticatedClient,
    json_body: SeriesUpdate,
) -> Response[Union[HTTPValidationError, SeriesInDB]]:
    """Udpate Series

    Args:
        series_id (str):
        json_body (SeriesUpdate):

    Returns:
        Response[Union[HTTPValidationError, SeriesInDB]]
    """

    kwargs = _get_kwargs(
        series_id=series_id,
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    series_id: str,
    *,
    client: AuthenticatedClient,
    json_body: SeriesUpdate,
) -> Optional[Union[HTTPValidationError, SeriesInDB]]:
    """Udpate Series

    Args:
        series_id (str):
        json_body (SeriesUpdate):

    Returns:
        Response[Union[HTTPValidationError, SeriesInDB]]
    """

    return (
        await asyncio_detailed(
            series_id=series_id,
            client=client,
            json_body=json_body,
        )
    ).parsed
