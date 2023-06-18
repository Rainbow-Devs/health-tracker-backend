"""
Django endpoint for GraphQL via Graphene.

Learn more at https://docs.graphene-python.org/en/latest/quickstart
"""

from django.contrib.auth.models import User
from graphene_django import DjangoObjectType
import graphene


class UserType(DjangoObjectType):
    class Meta:
        model = User
        fields = ("id", "username", "email")


class Query(graphene.ObjectType):
    """
    Class that handles GraphQL queries
    """

    hello = graphene.String(default_value="Hi!")
    ping = graphene.String(default_value="pong")
    users = graphene.List(UserType)

    def resolve_users(self, **kwargs):
        return User.objects.all()


schema = graphene.Schema(query=Query)
