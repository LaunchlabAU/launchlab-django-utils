"""
Test storage
"""

from django.test import TestCase

class StorageTestCase(TestCase):
    def test_import(self):
        from launchlab_django_utils.storage import StaticRootS3BotoStorage
        from launchlab_django_utils.storage import MediaRootS3BotoStorage
