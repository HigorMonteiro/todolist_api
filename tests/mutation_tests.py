import pytest

from task_api.schema import schema

pytestmark = pytest.mark.django_db


def test_mutations():

    query = """
        mutation  {
        createAssignment(
            title: "Task pytest",
            description: "Task pytest description")
            {
                assignment {
                    id
                    title
                    description
                }
            }
        }
    """
    expected = {
        "createAssignment": {
            "assignment": {
                'id': '1',
                "title": "Task pytest",
                "description": "Task pytest description"
            }
        }
    }
    executed = schema.execute(query)
    assert not executed.errors
    assert dict(executed.data) == expected
