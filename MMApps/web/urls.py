from django.urls import path
from MMApps.web.views import webViewObject

urlpatterns = [
    path('', webViewObject.index_view, name='index_view'),
]