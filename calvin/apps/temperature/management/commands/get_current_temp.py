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

    def refresh_temp(self):
        #output_path = os.path.join(self.working_dir, 'temper.out')
        d = datetime.now()
        f = open(self.output_path, 'w')
        f.write(datetime.strftime(d, '%Y-%m-%d %X'))
        f.write('\n')
        f.close()
        call('sudo temper-poll >> %s' % (self.output_path,), shell=True)

    def parse_temp(self):

        f = open(self.output_path, 'ru')
        contents = f.read()
        logger.info(contents)

        timestamp_regex = r'(\d{4})-(\d{2})-(\d{2}) (\d{2}):(\d{2}):(\d{2})'
        timestamp_match = re.search(timestamp_regex, contents)
        temp_time = datetime.strptime(timestamp_match.group(0), '%Y-%m-%d %X')

        temp_regex = r'(\d{1,3}\.\d\S+F)'
        temp_match = re.search(temp_regex, contents)
        temp = temp_match.group(0)

        message = 'The time is %s, and it\'s %s at Mike\'s desk.' % (temp_time.time(), temp,)
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

            #call_command('generate_concern_cats', interactive=True)
            logger.info("hello, world.")
        except AttributeError:
            raise
