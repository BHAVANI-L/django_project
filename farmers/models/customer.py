from django.db import  models
from django.core.validators import MinLengthValidator

class Customer(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    password = models.CharField(max_length=500)
    phone = models.CharField(max_length=15)
    location=models.CharField(max_length=50)
    image=models.ImageField(upload_to='uploads/customers/')

    def register(self):
        self.save()

    @staticmethod
    def get_customer_by_email(email):
        try:
            return Customer.objects.get(email=email)
        except:
            return False


    def isExists(self):
        if Customer.objects.filter(email = self.email):
            return True

        return  False