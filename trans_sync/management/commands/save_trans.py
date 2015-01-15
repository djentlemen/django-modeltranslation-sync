# coding: utf-8
from __future__ import unicode_literals
import os
from os.path import join, isdir
from optparse import make_option
from django.core.management.base import NoArgsCommand
from django.conf import settings
from modeltranslation.translator import translator

from babel.messages.catalog import Catalog
from babel.messages.pofile import write_po


class Command(NoArgsCommand):

    option_list = NoArgsCommand.option_list + (
        make_option(
            '--dry-run',
            action='store_true',
            dest='dry_run',
            default=False,
            help='Do not actually save files.'
        ),
    )

    def handle(self, *args, **options):
        if not options['dry_run']:
            pass

        locale_path = settings.LOCALE_MODEL_TRANS
        if not isdir(locale_path):
            os.mkdir(locale_path)

        for lang in [l[0] for l in list(settings.LANGUAGES)]:

            catalog = Catalog(locale=lang)

            for model in translator.get_registered_models():
                opts = translator.get_options_for_model(model)

                for field in opts.get_field_names():
                    tr_field = "%s_%s" % (field, lang)
                    for item in model.objects.all():
                        msgid = "%s.%s.%s" % (item._meta, item.pk, field)
                        msgstr = "%s" % getattr(item, tr_field)
                        catalog.add(id=msgid, string=msgstr)

            # write catalog to file
            lang_path = os.path.join(locale_path, lang)
            if not isdir(lang_path):
                os.mkdir(lang_path)
            f = open(join(lang_path, "LC_MESSAGES", "modeltranslation.po"), "w")
            write_po(f, catalog)
            f.close()