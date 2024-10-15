from django.urls import path
from MMApps.web.views import webViewObject,authViewObject

urlpatterns = [
    path('', webViewObject.index_view, name='index_view'),
    path('login/', authViewObject.login_view, name='login_view'),
    path('register/', authViewObject.register_view, name='register_view'),

]