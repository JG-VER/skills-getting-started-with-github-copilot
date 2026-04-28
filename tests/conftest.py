from copy import deepcopy

import pytest
from fastapi.testclient import TestClient

from src import app as app_module


@pytest.fixture(scope="session")
def baseline_activities():
    return deepcopy(app_module.activities)


@pytest.fixture(autouse=True)
def reset_activities(baseline_activities):
    # Arrange: isolate each test by restoring in-memory data.
    app_module.activities = deepcopy(baseline_activities)
    yield
    app_module.activities = deepcopy(baseline_activities)


@pytest.fixture
def client():
    return TestClient(app_module.app)
