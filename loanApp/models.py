from django.db import models
from phone_field import PhoneField

# Create your models here.
class Customer(models.Model):
	name              = models.CharField(max_length=128)
	phone             = PhoneField(blank=True, help_text='Contact Phone number')
	location          = models.CharField(max_length=100, default='some location')
	business          = models.CharField(max_length=100, default='some business')
	amount            = models.IntegerField(blank=False, default=0)
	customerSignature = models.FileField(blank=True, upload_to='Signatures/')
	PENDING   = 'PE'
	RECEIVED  = 'RE'
	REJECTED  = 'RJ'
	APPROVED  = 'AP'

	STATUS_CHOICES = [
		(PENDING, 'Pending'),
		(RECEIVED, 'Received'),
		(REJECTED, 'Rejected'),
		(APPROVED, 'Approved'),
	]
	status = models.CharField(max_length=2, choices=STATUS_CHOICES, default=PENDING)

	def __str__(self):

		return self.name


