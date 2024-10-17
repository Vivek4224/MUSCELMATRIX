from django.urls import path
from MMApps.web.views import webViewObject,authViewObject

urlpatterns = [
    path('', webViewObject.index_view, name='index_view'),
    path('t&c/', webViewObject.terms_of_service_view,name='terms_of_service_view'),
    path('login/', authViewObject.login_view, name='login_view'),
    path('register/', authViewObject.register_view, name='register_view'),
    path('activate/<str:client_id>/<str:token>/', authViewObject.activate_account, name='activate_account'),
    path('forgotpassword/', authViewObject.forgot_password, name='forgot_password'),

]