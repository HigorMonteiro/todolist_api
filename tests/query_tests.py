import pytest
from graphene import Schema

from .data import initialize
from todolist.schema import Query

pytestmark = pytest.mark.django_db


def test_list_assignments():
    initialize()
    query = """
    {
        assignments {
            title
            description
        }
    }
    """
    expected = {"assignments": [{
        "title": "Task One",
        "description": "Description to task one"
    }]}
    schema = Schema(Query)
    result = schema.execute(query)
    assert not result.errors
    assert result.data == expected
