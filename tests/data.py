from todolist.models import Assignment, Project


def initialize():
    project = Project.objects.create(name="Project One")
    project.assignment_set.create(
        title="Task One",
        description="Description to task one",
        project_by=1)


def create_assignment(title, description, project_by):
    new_assignment = Assignment(
        title=title,
        description=description,
        project_by=project_by)
    new_assignment.save()
    return new_assignment


def get_assignments():
    return Assignment.object.all()

