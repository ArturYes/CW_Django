import os

from django.core.management import BaseCommand

from apps.users.models import Users
from config.settings import BASE_DIR


class Command(BaseCommand):

    @staticmethod
    def create_superuser():
        user = Users.objects.create(
            email=os.environ.get("ADMIN_EMAIL"),
            user_name=os.environ.get("ADMIN_USER_NAME"),
            first_name=os.environ.get("ADMIN_FIRST_NAME"),
            last_name=os.environ.get("ADMIN_LAST_NAME"),
            middle_name=os.environ.get("ADMIN_MIDDLE_NAME"),
            is_staff=True,
            is_superuser=True,
            is_active=True,
        )
        user.set_password(os.environ.get("ADMIN_PASSWORD"))
        user.save()

    def handle(self, *args, **options):
        self.create_superuser()
