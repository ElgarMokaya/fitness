from django.urls import include, path
#from .views import MemberCreate
from . import views

app_name = 'smartmuscles'
urlpatterns=[
path('',views.index,name='index'),
path('members',views.get_members,name='get_members'),
#path('',MemberCreate.as_view())

]