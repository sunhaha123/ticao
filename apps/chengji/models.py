# -*- coding:utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from yundongyuan.models import Athlete
from events.models import Xiangmu

# Create your models here.
class ChengjiDate(models.Model):
    athlete = models.ForeignKey(Athlete, verbose_name=u'运动员姓名')
    date = models.DateField(null=True, blank=True, verbose_name=u'比赛日期', default='2010-01-01')
    mingcheng = models.CharField(max_length=50, null=True, blank=True, verbose_name=u'赛事名称')
    jibie = models.CharField(max_length=6,choices=(("guoji",u"国际"),("quanguo",u"全国"),("shengji",u"省级")),default=u"省级",verbose_name=u'赛事级别')
    xiangmu = models.ForeignKey(Xiangmu, verbose_name=u'体操项目')
    nandufen = models.FloatField(verbose_name=u'难度分')
    wanchengfen = models.FloatField(verbose_name=u'完成')
    zongfen = models.FloatField(verbose_name=u'总分')


    # gender = models.CharField(max_length=6, choices=(("male", u"男"), ("female", u"女")), default=u"male",
    #                           verbose_name=u'性别')
    # address = models.CharField(max_length=100, default=u'', verbose_name=u'地址')
    # mobile = models.CharField(max_length=11, null=True, blank=True, verbose_name=u'手机号')



    class Meta:
        verbose_name = u'运动成绩'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.athlete.name


class ChengjiSh(models.Model):
    xingming = models.ForeignKey(Athlete, verbose_name=u'队员姓名')
    riqi = models.DateField(null=True, blank=True, verbose_name=u'生化日期', default='2010-01-01')
    gaotong = models.FloatField(verbose_name=u'睾酮')
    nandufen = models.FloatField(verbose_name=u'难度分')
    wanchengfen = models.FloatField(verbose_name=u'完成分')
    zongfen = models.FloatField(verbose_name=u'总分')

    class Meta:
        verbose_name = u'成绩-生化'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.xingming.name