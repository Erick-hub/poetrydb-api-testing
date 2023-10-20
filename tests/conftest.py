import pytest
import json
from types import SimpleNamespace


f = open('jubilate_agno.json')


@pytest.fixture
def get_sample(request):
    _sample = json.loads(f, object_hook=lambda d: SimpleNamespace(**d))
    request.cls_sample = _sample
    return request.cls_sample
