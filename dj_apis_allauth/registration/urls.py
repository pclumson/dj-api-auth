from django.urls import path, re_path
from django.views.generic import TemplateView
from allauth.account.views import *

from rest_framework.views import APIView

from .views import MyRegisterView, RegisterView, VerifyEmailView, ResendEmailVerificationView


urlpatterns = [
    path('', RegisterView.as_view(), name='rest_register'),

    # re_path(r'verify-email/?$', VerifyEmailView.as_view(), name='rest_verify_email'),
    path('verify-email/', VerifyEmailView.as_view(), name='rest_verify_email'),

    path('resend-email/', ResendEmailVerificationView.as_view(), name="rest_resend_email"),
    # re_path(r'resend-email/?$', ResendEmailVerificationView.as_view(), name="rest_resend_email"),

    # This url is used by django-allauth and empty TemplateView is
    # defined just to allow reverse() call inside app, for example when email
    # with verification link is being sent, then it's required to render email
    # content.

    # account_confirm_email - You should override this view to handle it in
    # your API client somehow and then, send post to /verify-email/ endpoint
    # with proper key.
    # If you don't want to use API on that step, then just use ConfirmEmailView
    # view from:
    # django-allauth https://github.com/pennersr/django-allauth/blob/master/allauth/account/views.py

    path(
        'account-confirm-email/<str:key>/', TemplateView.as_view(),
        name='account_confirm_email',
    ),

    # re_path(
    #     r'^account-confirm-email/(?P<key>[-:\w]+)/$', TemplateView.as_view(),
    #     name='account_confirm_email',
    # ),


    # path(
    #     'account-email-verification-sent/', TemplateView.as_view(template_name="signup.html"),
    #     name='account_email_verification_sent',
    # ),

    re_path(
        r'account-email-verification-sent/?$', TemplateView.as_view(),
        name='account_email_verification_sent',
    ),


    # path('account/verify-email/<str:key>/', ConfirmEmailView.as_view(),
    #      name='account_confirm_email'),


    # path('account/password/reset/', PasswordResetView.as_view(),
    #      name='account_reset_password'),


    # path('account/password/reset/key/{key}/', TemplateView.as_view(),
    #      name='account_reset_password_from_key'),


    # path('account/signup/', TemplateView.as_view(),
    #      name='account_signup'),

    # path('account/provider/callback', TemplateView.as_view(),
    #      name='socialaccount_login_error"'),



    
]
