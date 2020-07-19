from django.db import models

class Users(models.Model):
    name = models.CharField(max_length = 50)
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=15)
    phone = models.CharField(max_length=20)
    ph_valid = models.IntegerField(default = 0)

    class Meta:
        db_table = 'users'

    def __str__(self):
        return self.name

class OTPValidator(models.Model):
    otp = models.IntegerField()
    uid = models.IntegerField()

    class Meta:
        db_table = 'otp_validator'