import graphene
from graphene_django import DjangoObjectType

from .models import Assignment


class AssignmentType(DjangoObjectType):
    class Meta:
        model = Assignment


class Query(graphene.ObjectType):
    assignments = graphene.List(AssignmentType)

    def resolve_assignments(self, info):
        return Assignment.objects.all()


class CreateAssignment(graphene.Mutation):
    assignment = graphene.Field(AssignmentType)

    class Arguments:
        title = graphene.String()
        description = graphene.String()

    def mutate(self, info, title, description):
        assignment = Assignment(title=title, description=description)
        assignment.save()
        return CreateAssignment(assignment=assignment)


class UpdateAssignment(graphene.Mutation):
    assignment = graphene.Field(AssignmentType)

    class Arguments:
        assignment_id = graphene.Int(required=True)
        title = graphene.String()
        description = graphene.String()

    def mutate(self, info, assignment_id, title, description):
        assignment = Assignment.objects.get(id=assignment_id)

        assignment.title = title
        assignment.description = description
        assignment.save()

        return UpdateAssignment(assignment=assignment)


class DeleteAssignment(graphene.Mutation):
    assignment_id = graphene.Int()

    class Arguments:
        assignment_id = graphene.Int(required=True)

    def mutate(self, info, assignment_id):
        assignment = Assignment.objects.get(id=assignment_id)
        assignment.delete()

        return DeleteAssignment(assignment_id=assignment_id)


class Mutation(graphene.ObjectType):
    create_assignment = CreateAssignment.Field()
    update_assignment = UpdateAssignment.Field()
    delete_assignment = DeleteAssignment.Field()
