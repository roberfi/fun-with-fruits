from typing import Any

import httpx


def assert_status_code(response: httpx.Response, *, expected: int) -> None:
    assert response.status_code == expected, (
        f"Status code is {response.status_code} instead of {expected}"
    )


def assert_response_json(response: httpx.Response, *, expected: Any) -> None:
    assert response.json() == expected, (
        f"JSON response is '{response.json()}', but expected was '{expected}'"
    )


def assert_empty_response(response: httpx.Response) -> None:
    assert response.text == "", (
        f"Response is not empty. Its actual content is: {response.text}"
    )
