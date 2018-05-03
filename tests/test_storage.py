"""
Test storage
"""

from django.test import TestCase

class StorageTestCase(TestCase):
    def test_import(self):
        from launchlab_django_utils.storage import StaticRootS3Boto3Storage
        from launchlab_django_utils.storage import MediaRootS3Boto3Storage
