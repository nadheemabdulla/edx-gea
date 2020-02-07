# -*- coding: utf-8 -*-
from __future__ import absolute_import

from django.apps import AppConfig
import edx_gea

import logging
log = logging.getLogger(__name__)


class EdxGeaConfig(AppConfig):
    name = 'edx_gea'
    log.error('1')

    def ready(self):
        log.error('2')
        from .gea import GradeExternalActivityXBlock
        log.error('3')
        edx_gea.GradeExternalActivityXBlock = GradeExternalActivityXBlock
        log.error('4')
