from django.urls import path
from accounts import views

urlpatterns = [
    path('login/',views.login_page, name="login"),
    path('register/',views.register_page, name="register"),
    path('send_otp/<email>/' , views.send_otp, name='send_otp'),
    path('verify-otp/<email>/' , views.verify_otp, name='verify_otp'),


    path('verify-account/<token>/', views.verify_email_token, name="verify_email_token")
]
