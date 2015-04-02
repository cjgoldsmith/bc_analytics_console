from django.db import models

# Create your models here.
class BCCredentials(models.Model):
    name = models.CharField(
        max_length=255,
        db_index=True,
    )
    client_id = models.CharField(max_length=255)
    client_secret = models.CharField(max_length=255)

    class Meta:
        ordering = ('name', )

class BCAccounts(models.Model):
    name = models.CharField(
        max_length=255,
        db_index=True,
    )
    pub_id = models.PositiveIntegerField(unique=True)
    auth = models.CharField(max_length=255)
    token = models.CharField(max_length=255)

    class Meta:
        ordering = ('name', )

