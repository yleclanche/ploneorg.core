# -*- coding: utf-8 -*-

import pycountry
from zope.schema.vocabulary import SimpleTerm
from zope.schema.vocabulary import SimpleVocabulary


countries = [SimpleTerm(value=country.alpha3,
                        token=country.alpha3,
                        title=country.name)
             for country in pycountry.countries]
country_vocabulary = SimpleVocabulary(countries)
