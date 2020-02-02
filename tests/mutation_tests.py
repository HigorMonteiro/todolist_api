import pytest

from task_api.schema import schema

pytestmark = pytest.mark.django_db


def test_mutations():

    query_project = """
        mutation  {
            createProject(name: "Project One"){
                project {
                    id
                    name
                }
            }
        }

    """
    query = """
        mutation  {
        createAssignment(
            projectBy: 1,
            title: "Task pytest",
            description: "Task pytest description")
            {
                assignment {
                    id
                    title
                    description
                    projectBy {
                        id
                    }

                }
            }
        }
    """
    expected = {
        "createAssignment": {
            "assignment": {
                'id': '1',
                "title": "Task pytest",
                "description": "Task pytest description",
                "projectBy": {
                    "id": "1"
                }
            }
        }
    }
    project = schema.execute(query_project)
    assignment = schema.execute(query)
    assert not project.errors
    assert not assignment.errors
    assert dict(assignment.data) == expected
