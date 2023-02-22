from django.contrib import admin
# from django.apps import apps
from .models import Login,Signup

# Register your models here.
admin.site.register(Signup)
admin.site.register(Login)

# # all other models
# models = apps.get_models()
# for model in models:
#     try:
#         admin.site.register(model)
#     except admin.sites.AlreadyRegistered:
#         pass

