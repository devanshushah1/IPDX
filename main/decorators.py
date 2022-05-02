from django.contrib.auth.decorators import user_passes_test, login_required

ngo_required = user_passes_test(lambda user: user.is_ngo, login_url='login')
donor_required = user_passes_test(
    lambda user: user.is_donor, login_url='login')


def ngo_user_required(view_func):
    decorated_view_func = login_required(ngo_required(view_func))
    return decorated_view_func


def donor_user_required(view_func):
    decorated_view_func = login_required(donor_required(view_func))
    return decorated_view_func
