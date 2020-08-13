import uuid
from django.contrib.auth.models import AbstractUser
from django.db import models

class Role(models.Model):
    """
    The Role entries are managed by the system,
    automatically created via a Django data migration.
    """
    CUSTOMERSUPPORT      = 'customersupport'
    BACKOFFICE           = 'backoffice'
    

    ROLE_CHOICES = (
        (CUSTOMERSUPPORT, 'customersupport'),
        (BACKOFFICE, 'backoffice')
    )

    id = models.CharField(primary_key=True, choices=ROLE_CHOICES, max_length=30)

    class Meta:
        db_table = 'role'

    def __str__(self):
        """ Return a string representation for the Roles """
        return self.get_id_display()


class User(AbstractUser):
    """ Custom user model with additional fields """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4,
                          unique=True, editable=False)
    roles = models.ManyToManyField(Role)
    middle_name = models.CharField(max_length=20, blank=True, null=True,
                                   default='')
    class Meta:
        db_table = 'wakala_user'

    def __str__(self):
        return self.username





