# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from scrapy.selector import Selector

import random

from django.shortcuts import render

from .forms import SurveyForm

def scrap(lat, lng):

    url = 'http://www.georisques.gouv.fr/ma_maison_mes_risques/rapport?lon=%s&lat=%s' % (lng, lat)
    print url
    # browser = webdriver.PhantomJS()
    # browser.get(url)

    # html = browser.page_source
    html = False
    # selector = Selector(text=html)

    data = [
        {'fieldset':u'Innondations',
         'fields':[
            {'label':u'Localisation exposée à une remontée de nappe dans les sédiments', 'xpath':'//*[@id="alea-INN"]/ul[2]/li[1]/text()'},
            {'label':u'Localisation exposée à une remontée de nappe dans le socle', 'xpath':'//*[@id="alea-INN"]/ul[3]/li/text()'},
            {'label':u'Type d\'exposition', 'xpath':'//*[@id="alea-INN"]/ul[3]/li[2]/text()'},
        ]},
        {'fieldset':u'Retrait-gonflements des argiles',
         'fields':[
            {'label':u'Localisation exposée aux retrait-gonflements des argiles', 'xpath':'//*[@id="alea-RETRAIT"]/ul[2]/li[1]/text()'},
            {'label':u'Type d\'exposition', 'xpath':'//*[@id="alea-RETRAIT"]/ul[2]/li[2]/text()'},
        ]},
        {'fieldset':u'Mouvements de terrain',
         'fields':[
            {'label':u'Mouvements de terrain recensés dans un rayon de 200m', 'xpath':'//*[@id="alea-MVMT"]/ul[2]/li/text()'},
        ]},
        {'fieldset':u'Cavités souterraines',
         'fields':[
            {'label':u'Cavités recensées dans un rayon de 200m', 'xpath':'//*[@id="alea-CAV"]/ul[2]/li/text()'},
        ]},
        {'fieldset':u'Séismes',
         'fields':[
            {'label':u'Localisation exposée aux séismes', 'xpath':'//*[@id="alea-SEISM"]/ul[2]/li[1]/text()'},
            {'label':u'Type d\'exposition', 'xpath':'//*[@id="alea-SEISM"]/ul[2]/li[2]/text()'},
        ]},
        {'fieldset':u'Sites et sols industriels',
         'fields':[
            {'label':u'Sites pollués dans un rayon de 200m', 'xpath':'//*[@id="alea-POL"]/ul[1]/li/text()'},
            {'label':u'Ancien site industriel et activité de service non localisé sur la commune', 'xpath':'//*[@id="alea-POL"]/ul[2]/li[2]/span/text()'},
            {'label':u'Ancien site industriel et activité de service dans un rayon de 200 m', 'xpath':'//*[@id="alea-POL"]/ul[2]/li[3]/span/text()'},
        ]},
        {'fieldset':u'Installations classées',
         'fields':[
            {'label':u'Votre installation est concernée par des installations classées', 'xpath':'//*[@id="alea-INST"]/ul[2]/li[1]/text()'},
            {'label':u'Votre installation est impactée par des installations classées', 'xpath':'//*[@id="alea-INST"]/ul[2]/li[2]/text()'},
            {'label':u'Votre installation est concernée par des installations rejetant des polluants dans un rayon de 5 km', 'xpath':'//*[@id="alea-INST"]/ul[3]/li/text()'},
        ]},
        {'fieldset':u'Canalisations de matières dangereuses',
         'fields':[
            {'label':u'Canalisations de matières dangereuses dans un rayon de 100m', 'xpath':'//*[@id="alea-CAN"]/ul/li/text()'},
        ]},
        {'fieldset':u'Installations nucléaires',
         'fields':[
            {'label':u'Installations nucléaires dans un rayon de 10km', 'xpath':'//*[@id="alea-NUC"]/ul/li[1]/text()'},
            {'label':u'Centrales nucléaires dans un rayon de 20km', 'xpath':'//*[@id="alea-NUC"]/ul/li[2]/text()'},
        ]},
    ]

    for d in data:
        for f in d['fields']:
            # try:
            #     f['value'] = selector.xpath(f['xpath']).extract()
            # except:
            f['value'] = random.choice([True, False])

    results = []
    for d in data:
        vals = [f['value'] for f in d['fields']]
        if any(vals):
            results.append(True)
        else:
            results.append(False)

    return results, data, html


def home(request):
    if request.method == "POST":
        form = SurveyForm(request.POST)
        if form.is_valid():
            instance = form.save()
            lat = instance.lat
            lng = instance.lng
            results, data, html = scrap(lat, lng)
            print results
            return render(request, 'result.html', {
                'form': form,
                'instance': instance,
                'results': results,
                'html': html
            })
    form = SurveyForm()
    return render(request, 'home.html', {
        'form': form
    })