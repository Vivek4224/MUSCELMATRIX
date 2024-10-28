from django.urls import path
from MMApps.web.views import webViewObject,authViewObject

urlpatterns = [
    path('', webViewObject.index_view, name='index_view'),
    path('about/', webViewObject.about_view, name='about_view'),
    path('contact/', webViewObject.contact_view, name='contact_view'),
    path('profile/', webViewObject.profile_view, name='profile_view'),
    path('edit-profile/', webViewObject.edit_profile_view, name='edit_profile_view'),
    path('edit-profile-picture/', webViewObject.edit_profile_picture, name='edit_profile_picture'),
    path('tac/', webViewObject.tac_view,name='tac_view'),
    path('login/', authViewObject.login_view, name='login_view'),
    path('logout/', authViewObject.logout, name='logout'),
    path('register/', authViewObject.register_view, name='register_view'),
    path('activate/<str:client_id>/<str:token>/', authViewObject.activate_account, name='activate_account'),
    path('forgot-password/', authViewObject.forgot_password_view, name='forgot_password_view'),
    path('otp-verification/', authViewObject.otp_verification_view, name='otp_verification_view'),

]