from typing import Any, Dict, Optional, Union

import httpx

from ...client import AuthenticatedClient
from ...models.company_in_db import CompanyInDB
from ...models.company_update import CompanyUpdate
from ...models.http_validation_error import HTTPValidationError
from ...types import Response


def _get_kwargs(
    company_id: str,
    *,
    client: AuthenticatedClient,
    json_body: CompanyUpdate,
) -> Dict[str, Any]:
    url = "{}/api/v1/companies/{company_id}".format(client.base_url, company_id=company_id)

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


def _parse_response(*, response: httpx.Response) -> Optional[Union[CompanyInDB, HTTPValidationError]]:
    if response.status_code == 200:
        response_200 = CompanyInDB.from_dict(response.json())

        return response_200
    if response.status_code == 422:
        response_422 = HTTPValidationError.from_dict(response.json())

        return response_422
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[CompanyInDB, HTTPValidationError]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    company_id: str,
    *,
    client: AuthenticatedClient,
    json_body: CompanyUpdate,
) -> Response[Union[CompanyInDB, HTTPValidationError]]:
    """Udpate Company

    Args:
        company_id (str):
        json_body (CompanyUpdate):

    Returns:
        Response[Union[CompanyInDB, HTTPValidationError]]
    """

    kwargs = _get_kwargs(
        company_id=company_id,
        client=client,
        json_body=json_body,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    company_id: str,
    *,
    client: AuthenticatedClient,
    json_body: CompanyUpdate,
) -> Optional[Union[CompanyInDB, HTTPValidationError]]:
    """Udpate Company

    Args:
        company_id (str):
        json_body (CompanyUpdate):

    Returns:
        Response[Union[CompanyInDB, HTTPValidationError]]
    """

    return sync_detailed(
        company_id=company_id,
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    company_id: str,
    *,
    client: AuthenticatedClient,
    json_body: CompanyUpdate,
) -> Response[Union[CompanyInDB, HTTPValidationError]]:
    """Udpate Company

    Args:
        company_id (str):
        json_body (CompanyUpdate):

    Returns:
        Response[Union[CompanyInDB, HTTPValidationError]]
    """

    kwargs = _get_kwargs(
        company_id=company_id,
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    company_id: str,
    *,
    client: AuthenticatedClient,
    json_body: CompanyUpdate,
) -> Optional[Union[CompanyInDB, HTTPValidationError]]:
    """Udpate Company

    Args:
        company_id (str):
        json_body (CompanyUpdate):

    Returns:
        Response[Union[CompanyInDB, HTTPValidationError]]
    """

    return (
        await asyncio_detailed(
            company_id=company_id,
            client=client,
            json_body=json_body,
        )
    ).parsed
