from todolist.models import Assignment


def initialize():
    task_one = Assignment(
        title="Task One",
        description="Description to task one"
    )
    task_one.save()


def create_assignment(title, description):
    new_assignment = Assignment(title=title, description=description)
    new_assignment.save()
    return new_assignment


def get_assignments():
    return Assignment.object.all()

