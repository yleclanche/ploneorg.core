# -*- coding: utf-8 -*-
from datetime import datetime
from plone import api
from Products.Five import BrowserView
from random import shuffle


class HomePage(BrowserView):

    def get_links(self):
        pc = api.portal.get_tool('portal_catalog')
        links = pc.searchResults(
            portal_type="site_link",
            review_state='published'
        )
        return [i.getObject() for i in links]

    def get_events(self):
        pc = api.portal.get_tool('portal_catalog')
        results = pc.searchResults(
            portal_type='Event',
            end={'query': datetime.now(), 'range': 'min'},
            sort_on='start',
            review_state='published'
        )
        return [i.getObject() for i in results[:4]]

    def get_news(self):
        portal = api.portal.get()
        try:
            front_page_news = portal['news']['front-page-news']
        except:
            return
        result = front_page_news.results(brains=True)
        return result

    def get_premium_sponsors(self):
        pc = api.portal.get_tool('portal_catalog')
        result = pc.searchResults(
            portal_type='FoundationSponsor',
            sponsorship_type='premium'
        )
        result_list = list(result)
        shuffle(result_list)
        return result_list
