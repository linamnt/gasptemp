#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# Do not change the following
AUTHOR = u'GASP'
SITENAME = 'Graduate Association for Students in Physiology'
SITENICK = 'GASP'
SITEURL = ''
SITELOGO = 'images/logo.jpg'
SITELOGO_SIZE = 50
PATH = 'content'
TIMEZONE = 'America/Toronto'
DEFAULT_LANG = u'en'
STATIC_PATHS = ['images', 'pdfs', 'posters']
SUMMARY_MAX_LENGTH = None
THEME = '../theme/'
BOOTSTRAP_THEME = 'paper'
FAVICON = 'images/favicon.ico'
TWITTER_WIDGET_ID = 'gaspuoft/gasp'
OUTPUT_PATH = 'www-data/'
DEFAULT_PAGINATION = 10
# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None



# Blogroll
LINKS = (('UofT Physiology', 'https://physiology.utoronto.ca/'),
("Graduate Student's Union", 'https://www.utgsu.ca/'),
('University of Toronto', 'https://www.utoronto.ca/'),
)

# Social widget
SOCIAL = (('Facebook', 'https://www.facebook.com/UofTGASP'),
('Email', 'gasp.physiology@utoronto.ca'),
('Mobile', 'https://play.google.com/store/apps/details?id=com.leesoft.gaspmobileapp'),
)

# Newsletter link for front page
NEWSLETTER = 'posters/dec2016.jpg'

# Upcoming Events in sidebar
UPCOMING_EVENTS = (
('Mount Sinai Coffee Break', 'Tuesday, Dec 13th, 3pm', 'Mount Sinai', 'category/events'),
('Gingerbread House Decorating', 'Friday, Dec 16th, 6:30pm', 'MSB 3227', 'gingerbread-decorating'),
('Coffee Break', 'Wednesdays at 2pm', 'Physiology Lunch Room', 'coffee-break'),
)


# Executive & Council Members:
EXECMEMBERS = (
(1, 'President', 'Melanie', 'Markovic', 'mel.markovic@mail.utoronto.ca'),
(1, 'Secretary', 'Farigol', 'Zadeh', 'gasp.physiology@utoronto.ca'),
(1, 'Treasurer', 'Frank', 'Lee', 'gasp.physiology@utoronto.ca'),
(2, 'Co-Vice President', 'Ankur', 'Bodalia', 'uoftfip@gmail.com'),
(2, 'Co-Vice President', 'Hanna', 'Kim', 'uoftfip@gmail.com'),
(2, 'Co-Vice President', 'Kirusanthy', 'Kaneshwaran', 'uoftfip@gmail.com'),
)

COUNCILMEMBERS = (
(1, 'Social Coordinator', 'Kenny', 'Chan', 'kennyl.chan@mail.utoronto.ca'),
(1, 'Social Coordinator', 'Scott', 'Frendo-Cumbo', 'scott.frendo.cumbo@mail.utoronto.ca'),
(1, 'Sports Coordinator', 'John', 'Choi', 'gasp.sports@gmail.com'),
(2, 'Academic Coordinator', 'Sammy', 'Cai', 'sammy.cai@mail.utoronto.ca'),
(2, 'Outreach Coordinator', 'Ashkan', 'Salehi', 'ash.salehi@mail.utoronto.ca'),
(2, 'Off-Campus Representative', 'Sina', 'Hadipour-Lakmehsari', 'sina.hadipour.lakmehsari@mail.utoronto.ca'), 
(3, 'Science Rendezvous Representative', 'Farwah', 'Iqbal', 'farwah.iqbal@mail.utoronto.ca'),
(3, 'GSU Representative', 'Susmita', 'Sarkar', 's.sarkar@mail.utoronto.ca'),
(3, 'CUPE Representative', 'Shahin', 'Khodaei', 'shahin.khodaei@mail.utoronto.ca'),
(4, 'Webmaster', 'Lina', 'Tran', 'lina.tran@mail.utoronto.ca'),
)
