#!/usr/local/bin/python3

from yelp.client import Client
from yelp.oauth1_authenticator import Oauth1Authenticator
from dotenv import load_dotenv, find_dotenv
import os

load_dotenv(find_dotenv())

def get_business_list(search_term, location):
    auth = Oauth1Authenticator(
        consumer_key=os.environ.get('YELP_CONSUMER_KEY'),
        consumer_secret=os.environ.get('YELP_CONSUMER_SECRET'),
        token=os.environ.get('YELP_TOKEN'),
        token_secret=os.environ.get('YELP_TOKEN_SECRET')
    )

    client = Client(auth)
    params = {
        'term': search_term,
        'lang': 'en'
    }

    businesses = []
    response = client.search(location, **params)
    for i in range(3):
        businesses.append({'name': response.businesses[i].name,
                            'phone': response.businesses[i].phone,
                            'rating': response.businesses[i].rating})
    return businesses
