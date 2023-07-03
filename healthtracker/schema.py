"""
Django endpoint for GraphQL via Graphene.

Learn more at https://docs.graphene-python.org/en/latest/quickstart
"""

import graphene
from graphene_django import DjangoObjectType

from django.contrib.sessions.models import Session
from django.contrib.auth import get_user_model
from activities.models import Activity, ActivityName
from user_profiles.models import UserProfile


class UserType(DjangoObjectType):
    class Meta:
        model = get_user_model()
        fields = "__all__"


# class PronounsType(DjangoObjectType):
#     class Meta:
#         model = Pronouns
#         fields = "__all__"


class ActivityType(DjangoObjectType):
    class Meta:
        model = Activity
        fields = "__all__"


class ActivityNameType(DjangoObjectType):
    class Meta:
        model = ActivityName
        fields = "__all__"


class UserProfileType(DjangoObjectType):
    class Meta:
        model = UserProfile
        fields = "__all__"


class UserProfileMutation(graphene.Mutation):
    class Arguments:
        user_id = graphene.ID()
        display_name = graphene.String()
        short_term_goal = graphene.String(required=True)
        long_term_goal = graphene.String(required=True)

    user_profile = graphene.Field(UserProfileType)

    @classmethod
    def mutate(cls, user_id, display_name, short_term_goal, long_term_goal):
        user_profile = UserProfile.objects.get(user_id=user_id)
        user_profile.display_name = display_name
        user_profile.short_term_goal = short_term_goal
        user_profile.long_term_goal = long_term_goal
        user_profile.save()
        # Notice we return an instance of this mutation
        return UserProfileMutation(user_profile=user_profile)


class Query(graphene.ObjectType):
    """
    Class that handles GraphQL queries
    """

    user_profile_by_sid = graphene.Field(
        UserProfileType, sid=graphene.String(required=True)
    )
    activities_by_sid = graphene.List(ActivityType, sid=graphene.String(required=True))
    activity_names = graphene.List(ActivityNameType)

    def resolve_activity_names(self):
        # We can easily optimize query count in the resolve method
        return ActivityName.objects.all()

    def resolve_user_profile_by_sid(self, sid):
        try:
            session = Session.objects.get(session_key=sid)
            session_data = session.get_decoded()
            uid = session_data.get("_auth_user_id")

            return UserProfile.objects.select_related("user").get(user_id=uid)
        except Session.DoesNotExist:
            return None
        except UserProfile.DoesNotExist:
            return None

    def resolve_activities_by_sid(self, sid):
        try:
            session = Session.objects.get(session_key=sid)
            session_data = session.get_decoded()
            uid = session_data.get("_auth_user_id")

            return (
                Activity.objects.select_related("user", "activity_name")
                .filter(user_id=uid)
                .all()
            )
        except Session.DoesNotExist:
            return None
        except Activity.DoesNotExist:
            return None

    hello = graphene.String(default_value="Hi!")
    ping = graphene.String(default_value="pong")


schema = graphene.Schema(query=Query)
