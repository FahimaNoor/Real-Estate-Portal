from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


# Apartment Details Model
class ApartmentModel(models.Model):
    """
        This class is extended from the Model class so it has all the functionality
        of the model class.


        this class used to create objects for database entry
        """
    apartment_id = models.AutoField(primary_key=True)
    location = models.TextField(max_length=100, null=False)
    apartment_type = models.TextField(max_length=50, null=False)
    description = models.TextField(null=False)
    utilities = models.TextField(null=False)
    picture = models.ImageField(null=True, upload_to='apartment_images')
    money = models.IntegerField(null=False)

    # Default string representation
    def __str__(self):
        return str(self.apartment_id)


# Post Model
class PostModel(models.Model):
    """
        This class is extended from the Model class so it has all the functionality
        of the model class.

        this class used to create objects for database entry
    """
    post_id = models.AutoField(primary_key=True)
    post_header = models.TextField(max_length=150, null=False)
    apartment_id = models.ForeignKey(ApartmentModel, db_column='apartment_id', on_delete=models.CASCADE)
    email = models.ForeignKey(User, db_column='email', auto_created=True, on_delete=models.CASCADE)
    date_and_time = models.DateTimeField(auto_now_add=True, null=False)
    phone = models.IntegerField(null=False)
    type_choice = (
        ('Sell', 'Sell'), ('Rent', 'Rent')
    )
    is_sell_post = models.CharField(max_length=5, null=False, choices=type_choice)

    # Default string representation
    def __str__(self):
        return self.post_header
