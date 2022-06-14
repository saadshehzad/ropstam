from django.core.mail import send_mail
from django.urls import reverse_lazy
from django.views import generic

from .forms import CustomUserCreationForm


class SignupPageView(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "signup.html"

    def post(self, request, *args, **kwargs):
        send_mail(
            "Thanks for registring",
            "Here is the message.",
            "ropstan@abc.com",
            [request.user],
            fail_silently=False,
        )
        return super().post(request, *args, **kwargs)
