import graphene
import todolist.schema


class Query(todolist.schema.Query, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query)
