from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse

User = get_user_model()


# returns a URL
def get_absolute_url():
    return reverse('chat:all')


# ChatModel
class Chat(models.Model):
    """
        This class is extended from the Model class so it has all the functionality
        of the model class.


        this class used to create objects for database entry
        """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    posted_at = models.DateTimeField(auto_now=True, null=True)

    # Default string representation
    def __str__(self):
        return str(self.message)
