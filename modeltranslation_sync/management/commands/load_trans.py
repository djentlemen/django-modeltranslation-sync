# coding: utf-8
from __future__ import unicode_literals

from optparse import make_option
from django.core.management.base import NoArgsCommand


class Command(NoArgsCommand):

    option_list = NoArgsCommand.option_list + (
        make_option(
            '--dry-run',
            action='store_true',
            dest='dry_run',
            default=False,
            help='Do not actually send signals (and all connected stuff).'
        ),
    )

    def handle(self, *args, **options):
        if not options['dry_run']:
            pass