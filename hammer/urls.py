from django.contrib import admin
from django.urls import path
from hammer.views import SendCodeView, VerifyCodeView, UserListView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('send_code/', SendCodeView.as_view()),
    path('verify/', VerifyCodeView.as_view()),
    path('users/', UserListView.as_view()),
]
