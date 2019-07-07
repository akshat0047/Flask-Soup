import requests
import time
from bs4 import BeautifulSoup
import time
import json


def domain(d):
    domain = d.split("//")[1].split("/")[0]
    return domain


class Scraper:
    url_list = []
    fail = []

    def get_links(self, url, p, dom):
        self.page = requests.get(url)
        time.sleep(1)
        if self.page.status_code == 200:
            if "text/html" in self.page.headers["Content-Type"]:
                self.soup = BeautifulSoup(self.page.content, "html5lib")
                self.links = self.soup.findAll('a')
                for link in self.links:
                    if "href" in link.attrs.keys():
                        urlf = link['href']
                        if "http" not in urlf:
                            if urlf.split('/')[0] == '':
                                urlf = urlf[1:]
                                urlf = p + "//" + dom + "/" + urlf
                            else:
                                urlf = p + "//" + dom + "/" + urlf

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
                            if urlf not in self.url_list and urlf.split('.')[-1] not in []:
                                self.url_list.append(urlf)

            else:
                pass
        else:
            self.fail.append(url)
            time.sleep(2)
            pass

    def extract_domain_links(self, url):
        self.url_list.append(url)
        dom = domain(self.url_list[0])
        for i in self.url_list:
            Scraper().get_links(i, i.split("//")[0], dom)
        time.sleep(2)
        self.url_list = list(dict.fromkeys(self.url_list))
        self.fail = list(dict.fromkeys(self.fail))
        time.sleep(2)

        for i in self.fail:
            if i in self.url_list:
                self.url_list.remove(i)

        return {"links": self.url_list, "fail": self.fail}

    def extract_page_links(self, url):
        self.url_list.append(url)
        dom = domain(self.url_list[0])
        Scraper().get_links(url, url.split("//")[0], dom)
        time.sleep(2)
        self.url_list = list(dict.fromkeys(self.url_list))
        self.fail = list(dict.fromkeys(self.fail))

        for i in self.fail:
            if i in self.url_list:
                self.url_list.remove(i)
        return {"links": self.url_list, "fail": self.fail}
