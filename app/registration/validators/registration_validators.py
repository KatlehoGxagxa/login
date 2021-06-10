
def validate_email_unique(query):
    if query == []:
        return True
    else:
        return False
    
def email_valid(email):
    if "@" in email:
        return True
    else:
        return False
    
def confirm_password(password, confirm_password):
    if password == confirm_password:
        return True
    else:
        return False
    