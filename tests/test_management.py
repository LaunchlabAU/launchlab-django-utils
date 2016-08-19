"""
Tests for custom management commands.
"""

from django.core.management import call_command
from django.test import TestCase
from django.utils.six import StringIO
from django.core.management.base import CommandError
from django.contrib.auth import get_user_model
from django.core import mail

User = get_user_model()

class CreateSuperusersAndEmailPassword(TestCase):
    command_name = 'create_superuser_and_email_password'
    email_address = 'test@example.org'

    def test_message_argument_required(self):
        out = StringIO()
        with self.assertRaisesRegexp(CommandError, 'too few arguments'):
            call_command(self.command_name, stdout=out)

    def test_message_users_created(self):
        out = StringIO()
        call_command(self.command_name, self.email_address, stdout=out)
        self.assertIn('user created', out.getvalue())

    def test_message_user_exists(self):
        out = StringIO()
        call_command(self.command_name, self.email_address, stdout=out)
        with self.assertRaisesRegexp(CommandError, 'UNIQUE constraint failed'):
            call_command(self.command_name, self.email_address, stdout=out)

    def test_user_created(self):
        out = StringIO()
        call_command(self.command_name, self.email_address, stdout=out)
        self.assertTrue(User.objects.count(), 1)
        self.assertEqual(User.objects.first().email, self.email_address)

    def test_correct_password_sent(self):
        out = StringIO()
        call_command(self.command_name, self.email_address, stdout=out)
        self.assertEquals(len(mail.outbox), 1)
        message = mail.outbox[0]
        self.assertEqual(message.to[0], self.email_address)
        password = message.body
        user = User.objects.first()
        self.assertTrue(user.check_password(password))

    def test_created_user_is_superuser(self):
        out = StringIO()
        call_command(self.command_name, self.email_address, stdout=out)
        self.assertTrue(User.objects.first().is_superuser)
