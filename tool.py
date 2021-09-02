import re
from urllib.request import urlopen
from urllib.parse import urlparse
import socket as s
import requests
from bs4 import BeautifulSoup
def inputs(label):
    web=input(str(label)+':')
    return web
    #line
class Tools:
    #line
    def details(self,name):
        f = open("label.txt", "r")
        print('\n')
        print(f.read())
        print(name)
        print('\n')
class Osint:
    #line
    def __init__(self,website):
        #line
        self.website = website
    def server(self):
        r = requests.get(self.website)
        print("--------------------------------------------------------------------------")
        print('[+] Server Info')
        info=r.headers
        for x in info:
            print("[*]"+x+":"+info[x])
    def images(self):
        #line
        url = self.website
        reqs = requests.get(url)
        soup = BeautifulSoup(reqs.text, 'html.parser')
        urls = []
        print("--------------------------------------------------------------------------")
        print('[+] Images Found')
        for link in soup.find_all('img'):
            print('[*]     '+str(link.get('src')))
    def urls(self):
        #line
        url = self.website
        reqs = requests.get(url)
        soup = BeautifulSoup(reqs.text, 'html.parser')
        urls = []
        print("--------------------------------------------------------------------------")
        print('[+] URLs Found')
        for link in soup.find_all('a'):
            print('[*]     '+str(link.get('href')))
    def phone(self):
        #line
        print("--------------------------------------------------------------------------")
        print('[+] Phone Numbers Found')
        website = urlopen(self.website).read().decode('utf8')
        numbers = (re.findall(r"((?:\d{3}|\(\d{3}\))?(?:\s|-|\.)?\d{3}(?:\s|-|\.)\d{4})",website))
        print ('\n'.join(map(str, numbers)))
    def ip_address(self):
        #line
        print("--------------------------------------------------------------------------")
        try:
            #line
            domain = urlparse(self.website).netloc
            print(f'IP of {domain} is {s.gethostbyname(domain)}')
        except Exception as e:
            print('[+] IP Not Found')
    def email(self):
        #line
        website = urlopen(self.website).read().decode('utf8')
        emails = (re.findall(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4}",website))
        print("--------------------------------------------------------------------------")
        print('[+] Emails Found')
        print ('\n'.join(map(str, emails)))
def main():
    #line
    p2 = Tools()
    p2.details("Developed By SibinThomas : GITHUB:https://github.com/SibinThomasQuad")
    web=inputs("Enter The URL")
    p1 = Osint(str(web))
    p1.server()
    p1.ip_address()
    p1.email()
    p1.phone()
    p1.urls()
    p1.images()
try:
    main()
except KeyboardInterrupt:
    print ('\nExiting The Program')
else:
    print ('[+] Done')
