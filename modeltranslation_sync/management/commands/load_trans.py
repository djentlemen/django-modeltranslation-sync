# coding: utf-8
from __future__ import unicode_literals
from os.path import join, isdir
from django.conf import settings

from django.core.management.base import NoArgsCommand, CommandError
from django.db.models.loading import get_model
from babel.messages.pofile import read_po


class Command(NoArgsCommand):

    def handle(self, *args, **options):

        if not hasattr(settings, 'MODELTRANSLATION_LOCALE_PATH'):
            raise CommandError("Settings has no attribute 'LOCALE_MODEL_TRANS'")

        if not hasattr(settings, 'MODELTRANSLATION_PO_FILE'):
            filename_po = "modeltranslation.po"
        else:
            filename_po = settings.MODELTRANSLATION_PO_FILE
            if not filename_po.endswith(".po"):
                filename_po += '.po'

        locale_path = settings.MODELTRANSLATION_LOCALE_PATH
        if not isdir(locale_path):
            raise CommandError("Locale directory does not exists.")

        for lang in [l[0] for l in list(settings.LANGUAGES)]:

            lang_path = join(locale_path, lang)
            if not isdir(lang_path):
                raise CommandError("Language directory does not exists.")
            f = open(join(lang_path, "LC_MESSAGES", filename_po), "r")
            catalog = read_po(f)
            f.close()

            for message in catalog:
                if message.id:
                    [app, class_name, pk, field] = message.id.split('.')
                    model = get_model(app, class_name)
                    obj = model.objects.get(pk=pk)
                    tr_field = "%s_%s" % (field, lang)
                    setattr(obj, tr_field, message.string)
                    obj.save()