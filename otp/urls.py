# urls.py

from django.urls import path
from .views import send_otp, verify_otp, resend_otp

urlpatterns = [
    # ...
    path('send-otp/', send_otp, name='send_otp'),
    path('verify-otp/', verify_otp, name='verify_otp'),
    path('resend-otp/', resend_otp, name='resend_otp'),
    # path('logout/', logout_view, name='logout'),

]
