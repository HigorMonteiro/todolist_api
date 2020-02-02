import graphene
from graphene_django import DjangoObjectType

from .models import Assignment, Project


class AssignmentType(DjangoObjectType):
    class Meta:
        model = Assignment


class ProjectType(DjangoObjectType):
    class Meta:
        model = Project


class Query(graphene.ObjectType):
    assignments = graphene.List(AssignmentType)
    project = graphene.List(ProjectType)

    def resolve_assignments(self, info):
        return Assignment.objects.all()

    def resolve_project(self, info):
        return Project.objects.all()


class CreateAssignment(graphene.Mutation):
    assignment = graphene.Field(AssignmentType)
    project = graphene.Field(ProjectType)

    class Arguments:
        title = graphene.String()
        description = graphene.String()
        project_by = graphene.Int(required=True)

    def mutate(self, info, title, description, project_by):
        project = Project.objects.get(id=project_by)

        if not project:
            raise Exception('Cannot find project')

        assignment = Assignment(
            title=title,
            description=description,
            project_by=project)
        assignment.save()
        return CreateAssignment(assignment=assignment)


class CreateProject(graphene.Mutation):
    project = graphene.Field(ProjectType)

    class Arguments:
        name = graphene.String()

    def mutate(self, info, name):
        project = Project(name=name)
        project.save()
        return CreateProject(project=project)


class UpdateAssignment(graphene.Mutation):
    assignment = graphene.Field(AssignmentType)
    project = graphene.Field(ProjectType)

    class Arguments:
        assignment_id = graphene.Int(required=True)
        title = graphene.String()
        description = graphene.String()
        project_by = graphene.Int(required=True)

    def mutate(self, info, assignment_id, title, description, project_by):
        assignment = Assignment.objects.get(id=assignment_id)
        project = Project.objects.get(id=project_by)

        if not project:
            raise Exception('Cannot find project')

        assignment.title = title
        assignment.description = description
        assignment.project_by = project
        assignment.save()

        return UpdateAssignment(assignment=assignment)


class UpdateProject(graphene.Mutation):
    project = graphene.Field(ProjectType)

    class Arguments:
        project_id = graphene.Int(required=True)
        name = graphene.String()

    def mutate(self, info, project_id, name):
        project = Project.objects.get(id=project_id)
        project.name = name
        project.save()

        return UpdateProject(project=project)


class DeleteAssignment(graphene.Mutation):
    assignment_id = graphene.Int()

    class Arguments:
        assignment_id = graphene.Int(required=True)

    def mutate(self, info, assignment_id):
        assignment = Assignment.objects.get(id=assignment_id)
        assignment.delete()

        return DeleteAssignment(assignment_id=assignment_id)


class DeleteProject(graphene.Mutation):
    project_id = graphene.Int()

    class Arguments:
        project_id = graphene.Int(required=True)

    def mutate(self, info, project_id):
        project = Project.objects.get(id=project_id)
        project.delete()

        return DeleteProject(project_id=project_id)


class Mutation(graphene.ObjectType):
    create_assignment = CreateAssignment.Field()
    update_assignment = UpdateAssignment.Field()
    delete_assignment = DeleteAssignment.Field()
    create_project = CreateProject.Field()
    update_project = UpdateProject.Field()
    delete_project = DeleteProject.Field()
