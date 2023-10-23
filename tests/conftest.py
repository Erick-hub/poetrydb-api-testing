import pytest
import json
from types import SimpleNamespace


@pytest.fixture
def get_sample(request):
    f = open('jubilate_agno.json')
    _sample = json.load(f)
    request.cls.sample = _sample
    return request.cls.sample
