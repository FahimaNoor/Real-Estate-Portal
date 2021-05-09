from django.contrib import admin
from post.models import PostModel, ApartmentModel

# Admin can access PostModel and ApartmentModel
admin.site.register(PostModel)
admin.site.register(ApartmentModel)
