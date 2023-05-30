"""
Django endpoint for GraphQL via Graphene.

Learn more at https://docs.graphene-python.org/en/latest/quickstart
"""

import graphene


class Query(graphene.ObjectType):
    """
    Class that handles GraphQL queries
    """

    hello = graphene.String(default_value="Hi!")
    ping = graphene.String(default_value="pong")


schema = graphene.Schema(query=Query)
