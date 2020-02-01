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


class Mutation(graphene.ObjectType):
    create_assignment = CreateAssignment.Field()
