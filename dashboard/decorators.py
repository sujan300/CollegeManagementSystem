from django.contrib.auth import REDIRECT_FIELD_NAME
from django.contrib.auth.decorators import user_passes_test


def admin_required(function=None,redirect_field_name=REDIRECT_FIELD_NAME,login_url='login'):
    print("the function is",function)
    actual_decorator = user_passes_test(
        lambda u: u.is_active and u.is_superadmin,
        login_url=login_url,
        redirect_field_name=redirect_field_name,
    )
    print("=============================actual decorator==================================")
    print(actual_decorator(function))
    print("========= actual decorator =========")
    print(actual_decorator)

    if function:
        return actual_decorator(function)
    return actual_decorator