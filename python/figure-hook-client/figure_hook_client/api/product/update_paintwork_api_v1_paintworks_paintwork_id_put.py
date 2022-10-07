from typing import Any, Dict, Optional, Union

import httpx

from ...client import AuthenticatedClient
from ...models.http_validation_error import HTTPValidationError
from ...models.worker_in_db import WorkerInDB
from ...models.worker_update import WorkerUpdate
from ...types import Response


def _get_kwargs(
    paintwork_id: int,
    *,
    client: AuthenticatedClient,
    json_body: WorkerUpdate,
) -> Dict[str, Any]:
    url = "{}/api/v1/paintworks/{paintwork_id}".format(client.base_url, paintwork_id=paintwork_id)

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


def _parse_response(*, response: httpx.Response) -> Optional[Union[HTTPValidationError, WorkerInDB]]:
    if response.status_code == 200:
        response_200 = WorkerInDB.from_dict(response.json())

        return response_200
    if response.status_code == 422:
        response_422 = HTTPValidationError.from_dict(response.json())

        return response_422
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[HTTPValidationError, WorkerInDB]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    paintwork_id: int,
    *,
    client: AuthenticatedClient,
    json_body: WorkerUpdate,
) -> Response[Union[HTTPValidationError, WorkerInDB]]:
    """Update Paintwork

    Args:
        paintwork_id (int):
        json_body (WorkerUpdate):

    Returns:
        Response[Union[HTTPValidationError, WorkerInDB]]
    """

    kwargs = _get_kwargs(
        paintwork_id=paintwork_id,
        client=client,
        json_body=json_body,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    paintwork_id: int,
    *,
    client: AuthenticatedClient,
    json_body: WorkerUpdate,
) -> Optional[Union[HTTPValidationError, WorkerInDB]]:
    """Update Paintwork

    Args:
        paintwork_id (int):
        json_body (WorkerUpdate):

    Returns:
        Response[Union[HTTPValidationError, WorkerInDB]]
    """

    return sync_detailed(
        paintwork_id=paintwork_id,
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    paintwork_id: int,
    *,
    client: AuthenticatedClient,
    json_body: WorkerUpdate,
) -> Response[Union[HTTPValidationError, WorkerInDB]]:
    """Update Paintwork

    Args:
        paintwork_id (int):
        json_body (WorkerUpdate):

    Returns:
        Response[Union[HTTPValidationError, WorkerInDB]]
    """

    kwargs = _get_kwargs(
        paintwork_id=paintwork_id,
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    paintwork_id: int,
    *,
    client: AuthenticatedClient,
    json_body: WorkerUpdate,
) -> Optional[Union[HTTPValidationError, WorkerInDB]]:
    """Update Paintwork

    Args:
        paintwork_id (int):
        json_body (WorkerUpdate):

    Returns:
        Response[Union[HTTPValidationError, WorkerInDB]]
    """

    return (
        await asyncio_detailed(
            paintwork_id=paintwork_id,
            client=client,
            json_body=json_body,
        )
    ).parsed
