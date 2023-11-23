from django.urls import path


from views import *

urlpatterns = [
    path('', index, name='home'),#http://127.0.0.1:8000/index/
    path('user/', user),#http://127.0.0.1:8000/user/
    path('trade/', trade),#http://127.0.0.1:8000/trade/
]
