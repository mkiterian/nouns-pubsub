import collections
import os
import pprint
import requests
from requests_oauthlib import OAuth1
from dotenv import load_dotenv


load_dotenv()

KEY = os.getenv('THE_NOUN_PROJECT_KEY')
SECRET = os.getenv('THE_NOUN_PROJECT_SECRET')
auth = OAuth1(KEY, SECRET)


def get_licence_types(icons):
    licences = [icon['license_description'] for icon in icons]
    return set(licences)


def get_icon_groups(icons):
    grouped = collections.defaultdict(list)
    for icon in icons:
        grouped[icon['license_description']].append(icon)
    return dict(grouped)


def get_icons(item):
    icons = []
    endpoint = 'http://api.thenounproject.com/icons/{}?limit=50'.format(item)
    response = requests.get(endpoint, auth=auth)
    icons = response.json()['icons']
    return icons


def get_all_icons(items):
    all_icons = []
    for item in items:
        all_icons += get_icons(item)
    return all_icons
