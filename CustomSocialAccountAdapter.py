from allauth.socialaccount.adapter import DefaultSocialAccountAdapter
from django.contrib.auth import get_user_model
from allauth.account.utils import user_email, user_field, user_username
from allauth.utils import valid_email_or_none


class SocialAccountAdapter(DefaultSocialAccountAdapter):
    def populate_user(self, request, sociallogin, data):
        social_app_name = sociallogin.account.provider.upper()
        first_name = data.get("first_name")
        last_name = data.get("last_name")
        if social_app_name == "GOOGLE":
            username = last_name + first_name
        elif social_app_name == "NAVER":
            username = sociallogin.account.extra_data["properties"]["nickname"]
        else:
            username = data.get("username")
        email = data.get("email")
        name = data.get("name")
        user = sociallogin.user
        user_username(user, username or "")
        user_email(user, valid_email_or_none(email) or "")
        name_parts = (name or "").partition(" ")
        user_field(user, "first_name", first_name or name_parts[0])
        user_field(user, "last_name", last_name or name_parts[2])
        return user


# https://github.com/pennersr/django-allauth
# https://whatisthenext.tistory.com/130
# https://django-allauth.readthedocs.io/en/latest/advanced.html#custom-user-models
# https://medium.com/@gajeshbhat/extending-and-customizing-django-allauth-eed206623a1a
# https://dev.to/gajesh/the-complete-django-allauth-guide-la3
# https://himanmengit.github.io/django/2019/04/22/django-allauth-socialuser-connect.html
# https://fluffycloudsandlines.blog/using-django-allauth-for-google-login-to-any-django-app/
# https://stackoverflow.com/questions/26287828/prepopulate-custom-form-with-social-data-in-django-allauth
