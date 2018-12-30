from accounts.models import User


def get_or_create_user_by_email(email):
    try:
        user = User.objects.get(email=email)
    except User.DoesNotExist:
        user = User.objects.create(email=email)
    return user
