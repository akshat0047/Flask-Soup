import requests
import time
from bs4 import BeautifulSoup
import time
import json


def domain(d):
    domain = d.split("//")[1]
    if domain.split('/'):
        domain = domain.split('/')[0]
    return domain


url_list = []
fail = []


class Scraper:

    def get_links(self, url, p, dom):
        global url_list
        page = requests.get(url)
        time.sleep(1)
        if page.status_code == 200:
            if "text/html" in page.headers["Content-Type"]:
                soup = BeautifulSoup(page.content, "html5lib")
                links = soup.findAll('a')
                for link in links:
                    if "href" in link.attrs.keys():
                        urlf = link['href']
                        if urlf.find("http", 0, 5) == -1:
                            if urlf.split('/')[0] == '':
                                urlf = urlf[1:]
                                urlf = p + "//" + dom + "/" + urlf
                            else:
                                urlf = p + "//" + dom + "/" + urlf
                        print(urlf)
                        domainanalyze = domain(urlf).split(".")
                        if len(domainanalyze) == 3:
                            subdomain = domainanalyze[0]
                        else:
                            subdomain = ''
                        if subdomain != "www" and subdomain != "":
                            pass
                        elif dom not in urlf:
                            pass
                        elif "#" in urlf:
                            pass
                        elif "mailto" in urlf:
                            pass
                        elif ".jpeg" in urlf:
                            pass
                        elif ".jpg" in urlf:
                            pass
                        elif ".png" in urlf:
                            pass
                        elif ".pdf" in urlf:
                            pass
                        elif "wp-login" in urlf:
                            pass
                        elif "tel:" in urlf:
                            pass
                        elif "index.html" in urlf:
                            pass
                        elif urlf == 'https://':
                            pass
                        else:
                            if urlf not in url_list:
                                url_list.append(urlf)

            else:
                pass
        else:
            fail.append(url)
            time.sleep(2)
            pass

    def extract_domain_links(self, url):
        global url_list
        global fail
        url_list = []
        fail = []
        url_list.append(url)
        dom = domain(url_list[0])
        print(url)
        for i in url_list:
            Scraper().get_links(i, i.split("//")[0], dom)
        time.sleep(2)
        url_list = list(dict.fromkeys(url_list))
        fail = list(dict.fromkeys(fail))
        print(url_list)
        time.sleep(2)

        for i in fail:
            if i in url_list:
                url_list.remove(i)

        return {"links": url_list, "fail": fail}

    def extract_page_links(self, url):
        global url_list
        global fail
        url_list = []
        fail = []
        url_list.append(url)
        dom = domain(url_list[0])
        Scraper().get_links(url, url.split("//")[0], dom)
        time.sleep(2)
        url_list = list(dict.fromkeys(url_list))
        fail = list(dict.fromkeys(fail))

        for i in fail:
            if i in url_list:
                url_list.remove(i)
        return {"links": url_list, "fail": fail}
