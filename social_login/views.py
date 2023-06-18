# from django.shortcuts import render
from django.views.generic import TemplateView
from django.shortcuts import redirect


# Create your views here.
class LoginPageView(TemplateView):
    template_name = "login.html"

    def get(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect("success")
        return super().get(request, *args, **kwargs)


class LoginSuccessView(TemplateView):
    template_name = "user.html"

    def get(self, request, *args, **kwargs):
        if self.request.user.is_authenticated is not True:
            return redirect("login_page")

        self.extra_context = {
            "username": self.request.user.get_username(),
            "session_id": self.request.session.session_key,
            "email_address": self.request.user.email,
        }

        return super().get(request, *args, **kwargs)
