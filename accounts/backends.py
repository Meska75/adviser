from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q

class EmailOrUsernameBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        User = get_user_model()
        try:
            user = User.objects.get(Q(email__iexact=username) | Q(username__iexact=username))
        except User.DoesNotExist:
            return None
        if user.check_password(password):
            return user
        return None