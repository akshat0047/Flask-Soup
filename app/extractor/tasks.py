from flask import request, jsonify
import json
import time
import requests
from bs4 import BeautifulSoup, SoupStrainer
from app.extractor.utils import Scraper
import celery
import os

# DOMAIN NAME


def domain(d):
    domain = d.split("//")[1].split("/")[0]
    return domain

# ALL LINKS ON A PAGE


@celery.task
def api_links(url=''):
    if 'url' in request.args:
        url = str(request.args['url'])

    information = []
    a = {}
    dom = domain(url)
    i = 0
    link_result = Scraper().extract_page_links(url)
    url_list = link_result['links']
    fail_dict = {"Links Failed": link_result['fail']}

    for link in url_list:
        a[i] = link
        i += 1

    information.append(a)
    information.append(fail_dict)

    return jsonify(a)


# ALL LINKS ON A DOMAIN

@celery.task
def api_linksd(url=''):
    if 'url' in request.args:
        url = str(request.args['url'])

    information = []
    a = {}
    dom = domain(url)
    i = 0
    link_result = Scraper().extract_domain_links(url)
    url_list = link_result['links']
    fail_dict = {"Links Failed": link_result['fail']}
    print(fail_dict)

    for link in url_list:
        a[i] = link
        i += 1

    information.append(a)
    information.append(fail_dict)
    return jsonify(information)


# HEADERS ON A DOMAIN

@celery.task
def api_alld(url=''):
    if 'url' in request.args:
        url = str(request.args['url'])
    a = {}
    information = []
    dom = domain(url)
    i = 0
    link_result = Scraper().extract_domain_links(url)
    url_list = link_result['links']
    fail_dict = {"Links Failed": link_result['fail']}

    for link in url_list:
        a[i] = link
        i += 1

    for link in a.values():
        r = requests.get(link)
        time.sleep(2)
        soup = BeautifulSoup(r.content, 'html5lib')
        h1 = soup.findAll('h1')
        h2 = soup.findAll('h2')
        h3 = soup.findAll('h3')
        h4 = soup.findAll('h4')
        h5 = soup.findAll('h5')

        headers = {'h1': h1, 'h2': h2, 'h3': h3, 'h4': h4, 'h5': h5}

        info = {'URL': link}

        for head in headers:
            info[head] = []
            for row in headers[head]:
                info[head].append(row.text.strip())
        information.append(info)
    information.append(fail_dict)

    return jsonify(information)

# HEADERS OF LINKS ON A PAGE


@celery.task
def api_allr(url=''):
    if 'url' in request.args:
        url = str(request.args['url'])

    a = {}
    information = []
    dom = domain(url)
    i = 0
    link_result = Scraper().extract_page_links(url)
    url_list = link_result['links']
    fail_dict = {"Links Failed": link_result['fail']}

    for link in url_list:
        a[i] = link
        i += 1

    for link in a.values():
        r = requests.get(link)
        time.sleep(2)
        soup = BeautifulSoup(r.content, 'html5lib')
        h1 = soup.findAll('h1')
        h2 = soup.findAll('h2')
        h3 = soup.findAll('h3')
        h4 = soup.findAll('h4')
        h5 = soup.findAll('h5')

        headers = {'h1': h1, 'h2': h2, 'h3': h3, 'h4': h4, 'h5': h5}

        info = {'URL': link}

        for head in headers:
            info[head] = []
            for row in headers[head]:
                info[head].append(row.text.strip())
        information.append(info)
    information.append(fail_dict)

    return jsonify(information)

# HEADERS ON A PAGE
@celery.task
def api_selected(url=''):
    if 'url' in request.args:
        url = str(request.args['url'])

    a = {}
    information = []
    dom = domain(url)
    r = requests.get(url)

    soup = BeautifulSoup(r.content, 'html5lib')
    h1 = soup.findAll('h1')
    h2 = soup.findAll('h2')
    h3 = soup.findAll('h3')
    h4 = soup.findAll('h4')
    h5 = soup.findAll('h5')

    headers = {'h1': h1, 'h2': h2, 'h3': h3, 'h4': h4, 'h5': h5}

    info = {'Domain': dom, 'URL': url}

    for head in headers:
        info[head] = []
        for row in headers[head]:
            info[head].append(row.text.strip())

    information.append(info)

    return jsonify(information)
