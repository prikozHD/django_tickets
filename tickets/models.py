# -*- coding: utf-8 -*-
from django.db import models
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _


class TimeModel(models.Model):
    created = models.DateTimeField(auto_now_add=True, verbose_name=_("Created"))
    modified = models.DateTimeField(auto_now=True, verbose_name=_("Modified"))

    class Meta:
        abstract = True


class Departament(TimeModel):
    name = models.CharField(max_length=200, verbose_name=_("Departament"))

    def __unicode__(self):
        return u"{0} {1} {2}".format(self.name, self.created, self.modified)

    class Meta:
        ordering = ['-id']
        verbose_name = _("Departament")
        verbose_name_plural = _("Departaments")


