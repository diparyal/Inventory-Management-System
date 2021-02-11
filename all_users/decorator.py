from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth import REDIRECT_FIELD_NAME

# user_login_required = user_passes_test(lambda user: user.is_admin, login_url='/account/login/')

# def admin_status_required(view_func):
#     decorated_view_func = login_required(user_login_required(view_func))
#     return decorated_view_func



def admin_status_required(function=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url='login'):
    '''
    Decorator for views that checks that the logged in user is a admin,
    redirects to the log-in page if necessary.
    '''
    actual_decorator = user_passes_test(
        lambda u: u.is_active and u.is_admin,
        login_url=login_url,
        redirect_field_name=redirect_field_name
    )
    print("actual_decorator:",actual_decorator)
    if function:
        return actual_decorator(function)
    return actual_decorator