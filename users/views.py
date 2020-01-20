from django.shortcuts import render, resolve_url
from django.contrib.auth import views


# def login(request):
#     return render(request, "users/login.html")


class LoginView(views.LoginView):
    template_name = "users/login.html"

    def get_success_url(self):

        next_url = self.request.GET.get("next")
        print(next_url)
        return resolve_url(next_url)


login = LoginView.as_view()
