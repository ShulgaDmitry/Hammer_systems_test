from django.db import models
from django.contrib.auth.models import AbstractUser
import random
import string

def generate_invite_code():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=6))

class User(AbstractUser):
    phone = models.CharField(max_length=15, unique=True)
    invite_code = models.CharField(max_length=6, default=generate_invite_code, unique=True)
    invited_by = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL)
    is_verified = models.BooleanField(default=False)

class VerificationCode(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    code = models.CharField(max_length=4)
    created_at = models.DateTimeField(auto_now_add=True)


