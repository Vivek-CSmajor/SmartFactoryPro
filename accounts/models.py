from django.contrib.auth.models import AbstractUser


# AbstractUser is built in provides default user model properties which can be modified for our use
#such as username, email, first_name, last_name, etc. and allows features like authentication seamlessly.
class User(AbstractUser):
    pass
