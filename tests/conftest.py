import pytest


def pytest_collection_modifyitems(items: list[pytest.Item]) -> None:
    for item in items:
        if item.get_closest_marker("pending") is not None:
            item.add_marker(pytest.mark.skip(reason="not implemented"))
