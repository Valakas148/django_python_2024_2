import os

from django.contrib.auth import get_user_model
from django.core.mail import EmailMultiAlternatives
from django.db.models import Model
from django.template.loader import get_template

from config.celery import app

from core.dataclasses.user_dataclass import User
from core.services.jwt_service import ActivateToken, JWTService, RecoveryToken

UserModel: User | Model = get_user_model()
class EmailService:
    @staticmethod
    @app.task
    def __send_email(to:str, template_name:str, context:dict, subject:str):
        template = get_template(template_name)
        html_content = template.render(context)
        msg = EmailMultiAlternatives(subject=subject, from_email=os.environ.get('EMAIL_HOST_USER'), to=[to])
        msg.attach_alternative(html_content, "text/html")
        msg.send()

    @classmethod
    def send_test(cls):
        cls.__send_email('ilyabychkov5x404@gmail.com', 'test.html', {}, 'Test Email')

    @classmethod
    def register_email(cls, user: User):
        token = JWTService.create_token(user, ActivateToken)
        url = f"https://localhost:8000/activate/{token}"
        cls.__send_email.delay(user.email, template_name='register.html', context={'name': user.profile.name, 'url': url}, subject='Register')

    @classmethod
    def recovery_email(cls, user: User):
        token = JWTService.create_token(user, RecoveryToken)
        url = f"https://localhost:8000/recovery/{token}"
        cls.__send_email(user.email, template_name='revoke.html', context={'name': user.profile.name, 'url': url}, subject='Recovery')

    @staticmethod
    @app.task
    def spam():
        for user in UserModel.objects.all():
            EmailService.__send_email(user.email, template_name='foremail.html', context={'name': user.profile.name}, subject='Spam')
