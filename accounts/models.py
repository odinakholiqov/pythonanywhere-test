from django.db import models
from django.contrib.auth.models import AbstractUser, Permission


# class Role(models.Model):
#     name = models.CharField(max_length=50)
#
#     user_permissions = models.ManyToManyField(
#         Permission,
#         verbose_name=_("user permissions"),
#         blank=True,
#         help_text=_("Specific permissions for this user."),
#         related_name="user_set",
#         related_query_name="user",
#     )

class User(AbstractUser):
    # role = models.ForeignKey(to=Role, on_delete=models.CASCADE, null=True)
    is_deleted = models.BooleanField(default=False)


