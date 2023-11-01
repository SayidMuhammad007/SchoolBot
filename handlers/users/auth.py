from secret import ADMIN_ID


def authentication(user_id):
    if user_id in ADMIN_ID:
        return True
    else:
        return False