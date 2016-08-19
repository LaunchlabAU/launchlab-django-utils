"""
Create superusers and email password to user.

Assumes the user is takes an email as a username.

This command is useful when we don't have an interactive console or access to a shell (e.g. running on AWS Lambda)
"""

from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth import get_user_model
from django.db import IntegrityError
from django.core.mail import send_mail
from django.conf import settings

User = get_user_model()


class Command(BaseCommand):
    """
    Creates superuser with email address and sends password.
    """
    help = 'Creates superuser with email address and sends password'

    def add_arguments(self, parser):
        parser.add_argument('email', nargs=1, type=str)

    def handle(self, *args, **options):
        try:
            email = options['email'][0]
            password = User.objects.make_random_password()
            User.objects.create_superuser(email=email, password=password)
            send_mail('Superuser password', password, settings.DEFAULT_FROM_EMAIL, [email])
            self.stdout.write(self.style.SUCCESS('user created'))
        except IntegrityError as e:
            raise CommandError(e)
