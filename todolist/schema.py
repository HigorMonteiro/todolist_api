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

