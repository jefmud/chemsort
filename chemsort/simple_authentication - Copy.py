# a simple-minded authentication module, replace in production
# probably OAuth2 would be nice here.

# change to valid values, don't use any actual account passwords!
# since the form has a email validator, you would have to use an email
# as the username
userhive = [
    {'username': 'your-email', 'password': 'your-password'},
    {'username': 'your-email2', 'password': 'your-password2'}
]

def authenticate(username, password):
    for user in userhive:
        if user['username'] == username:
            if user['password'] == password:
                return True
    return False
        
