from flask import Flask, render_template, request, flash, Blueprint, url_for, jsonify
from app.extractor.forms import ApiForm
from app.extractor.tasks import api_links, api_alld, api_allr, api_selected, domain, api_linksd
import requests


# Create some test data for our catalog in the form of a list of dictionaries.

extract = Blueprint('extract', __name__, url_prefix='/extract')
api = Blueprint('api', __name__, url_prefix='/api')


def processUrl(url, domain):
    url = url.decode("utf-8")
    if domain not in url:
        pass
    else:
        return url


@extract.route('/', methods=['GET', 'POST'])
def home():
    form = ApiForm(request.form)
    if request.method == 'POST':
        # if form.validate() == False:
        #    print("false")
        #    flash('All fields are required.')
        #    return render_template('index.html', form=form)
        # elif form.validate() == True:
        print("true")
        link = request.form['url']
        print(link)
        choice = request.form['Extract']
        print(choice)
        if choice == 'sp':
            return api_selected(url=link)

        if choice == 'lop':
            return api_links(url=link)
        if choice == 'lopd':
            return api_linksd(url=link)
        if choice == 'il':
            return api_allr(url=link)
        if choice == 'id':
            return api_alld(url=link)

    elif request.method == 'GET':
        print("here")
        return render_template('extractor/index.html', form=form)


@api.route('/', methods=['GET', 'POST'])
def api_view():
    html = "<h2>Welcome to API</h2>" + "<ul>" + "<li>Links On a Page '/api/v1/links?url=your_url'</li>" + "<li>Links On a Page '/api/v1/links?url=your_url'</li>" + "<li>Links On a Domain '/api/v1/domain_links?url=your_url'</li>" + \
        "<li>Headers On a Page '/api/v1/page?url=your_url'</li>" + "<li>Headers on First Children '/api/v1/first_children_headers?url=your_url'</li>" + \
        "<li>Headers on First Children '/api/v1/domain_headers?url=your_url'</li>"

    return html


@api.route('/v1/links', methods=['GET'])
def view_links():
    return api_links()


@api.route('/v1/domain_links', methods=['GET'])
def view_linksd():
    return api_linksd()


@api.route('/v1/page', methods=['GET'])
def view_select():
    return api_selected()


@api.route('/v1/first_children_headers', methods=['GET'])
def view_internal():
    return api_allr()


@api.route('/v1/domain_headers', methods=['GET'])
def view_domainheads():
    return api_alld()
