"""
Django command to wait for the database to be avaliable
"""

import time
from webbrowser import Opera

from psycopg2 import OperationalError as Psycopg20pError

from django.db.utils import OperationalError
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    """Command to wait for database"""

    def handle(self,*args, **options):
        """entrypoint for command."""
        self.stdout.write('waiting for database ...')
        db_up = False
        while db_up is False:
            try:
                self.check(databases=['default'])
                db_up=True
            except (Psycopg20pError, OperationalError):
                self.stdout.write('Database is unavaliable, wait 1 second ...')
                time.sleep(1)
        self.stdout.write(self.style.SUCCESS('Database avaliable!'))