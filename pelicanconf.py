#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

DEBUG = 1

AUTHOR = 'PyDelhi'
AUTHOR_EMAIL = 'contact@pydelhi.org'
SITENAME = 'PyDelhi Blog'
SITEURL = ''
SITESUBTITLE = 'Python Delhi Users Group'

PATH = 'content'

TIMEZONE = 'Asia/Kolkata'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ATOM = 'feeds/atom.xml'
FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'

FEED_RSS = 'feeds/rss.xml'
FEED_ALL_RSS = 'feeds/all.rss.xml'
CATEGORY_FEED_RSS = 'feeds/%s.rss.xml'

# Blogroll
LINKS = (
    ('PyDelhi.org', 'http://pydelhi.org'),
    ('About PyDelhi', 'https://pydelhi.org/pydelhi-intro'),
    ('Mailing list', 'http://bit.ly/pydelhi-mailinglist'),
    ('Conference', 'https://conference.pydelhi.org'),
)

# Social widget
SOCIAL = (
    ('Twitter', 'http://bit.ly/pydelhi-twitter'),
    ('Github', 'https://github.com/pydelhi'),
    ('Facebook', 'http://bit.ly/pydelhi-facebook'),
    ('Google+', 'http://bit.ly/pydelhi-google'),
)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

# Extra files to copy
STATIC_PATHS = [
    'images',
    'extra/robots.txt',
    'extra/humans.txt',
    'extra/favicon.ico'
]

EXTRA_PATH_METADATA = {
    'extra/robots.txt': {'path': 'robots.txt'},
    'extra/humans.txt': {'path': 'humans.txt'},
    'extra/favicon.ico': {'path': 'favicon.ico'},
}

# settings for Pelican
DEFAULT_CATEGORY = 'General'
THEME = 'theme/pydelhi'
DISQUS_SITENAME = ""

# Plugins
PLUGIN_PATHS = ['plugins']
PLUGINS = ['gravatar']


PRIVACY_POLICY_URL = ""
