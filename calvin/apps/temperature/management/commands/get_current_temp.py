import logging
from subprocess import call
from datetime import datetime
import os
import re

from django.core.management.base import BaseCommand
from django.conf import settings
from django.core.mail import send_mail

logger = logging.getLogger('cir.custom')


class Command(BaseCommand):
    help = "Updates Application objects' ag_use boolean using record_id."

    output_path = os.path.join(settings.BASE_DIR, 'data', 'temper.out')
    from_email = settings.FROM_EMAIL
    email_list = settings.EMAIL_LIST

    latest_temp = ''
    latest_temp_time = ''

    def refresh_temp(self):
        d = datetime.now()
        f = open(self.output_path, 'w')
        f.write(datetime.strftime(d, '%Y-%m-%d %X'))
        f.write('\n')
        f.close()
        call('temper-poll >> %s' % (self.output_path,), shell=True)  # This is a pretty hacky way to do this. We send the output of the command to a text file, then pick it up with parse. Must be a way to run temper-poll directly, and without sudo.

    def parse_temp(self):

        f = open(self.output_path, 'ru')
        contents = f.read()
        logger.info(contents)

        timestamp_regex = r'(\d{4})-(\d{2})-(\d{2}) (\d{2}):(\d{2}):(\d{2})'
        timestamp_match = re.search(timestamp_regex, contents)
        self.latest_temp_time = datetime.strptime(timestamp_match.group(0), '%Y-%m-%d %X')

        temp_regex = r'(\d{1,3}\.\d\S+F)'  # Right now this is a pretty lazy regex, and returns the degrees sign and "F". Could (and should) be easily modified to be a float.
        temp_match = re.search(temp_regex, contents)
        self.latest_temp = temp_match.group(0)

    def send_message(self):
        message = 'The time is %s, and it\'s %s at the data disco.' % (self.latest_temp_time.time(), self.latest_temp,)
        logger.info(message)
        send_mail(
            'Important Temperature Warning',
            message,
            self.from_email,
            self.email_list,
            fail_silently=False
        )

    def handle(self, *args, **options):
        try:
            self.refresh_temp()
            self.parse_temp()
            self.send_message()

            logger.info("hello, world.")
        except AttributeError:
            raise
