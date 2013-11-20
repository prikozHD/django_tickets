# -*- coding: utf-8 -*-
from django.db import models
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _
from django.conf.global_settings import LANGUAGES as DJANGO_LANGUAGES


class TimeModel(models.Model):
    created = models.DateTimeField(auto_now_add=True, verbose_name=_("Created"))
    modified = models.DateTimeField(auto_now=True, verbose_name=_("Modified"))

    class Meta:
        abstract = True


class Departament(TimeModel):
    name = models.CharField(max_length=200, verbose_name=_("Departament name"), db_index=True, unique=True)
    email = models.EmailField(max_length=200, verbose_name=_("Departament E-mail"), unique=True)
    description = models.TextField(verbose_name=_("Departament description"))
    locale = models.CharField(max_length=3, choices=DJANGO_LANGUAGES, verbose_name=_("Departament Locale"),  blank=True)

    def __unicode__(self):
        return u"{0} {1} {2}".format(self.name, self.created, self.modified)

    class Meta:
        ordering = ['-id']
        verbose_name = _("Departament")
        verbose_name_plural = _("Departaments")

