import pytest

from task_api.schema import schema
from .data import initialize

pytestmark = pytest.mark.django_db


def test_list_assignments():
    initialize()
    query = """
        {
            assignments {
                title
                description
                projectBy {
                id
                }
            }
        }
    """
    expected = {"assignments": [{
        "title": "Task One",
        "description": "Description to task one",
        "projectBy": {
            "id": "2"
        }
    }]}
    result = schema.execute(query)

    assert not result.errors
    assert result.data == expected
