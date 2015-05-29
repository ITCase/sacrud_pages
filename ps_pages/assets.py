#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2014 uralbash <root@uralbash.ru>
#
# Distributed under terms of the MIT license.

"""
Assets
"""


def includeme(config):
    config.include('pyramid_jinja2')
    config.add_jinja2_extension('jinja2.ext.with_')
    config.add_jinja2_search_path("ps_pages:templates")
    config.add_static_view('/ps_pages_static', 'ps_pages:static')
