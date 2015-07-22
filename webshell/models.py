# -*- coding: utf-8 -*-

from django.db import models


class Script(models.Model):
    name = models.CharField(u'Название', max_length=100)
    source = models.TextField(u'Текст скрипта')

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = u'Скрипт'
        verbose_name_plural = u'Скрипты'