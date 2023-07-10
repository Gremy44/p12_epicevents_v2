def user_role(request):
    role = None
    if request.user.is_authenticated:
        role = request.user.role_id
    return {'user_role': role}