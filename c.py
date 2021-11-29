import requests
import urllib.request
from queue import Queue
import re
#root = 'http://10.0.2.15/'
#root = "http://127.0.0.1:5000/"
root = "https://twitter.com/"
name = 'twitter'
class spider:
    def __init__(self, domain,name):
        self.domain = domain
        self.name = name


    
    def crawl(self):
        html = urllib.request.urlopen(self.domain)

        text = html.read()

        plaintext = text.decode('utf8')

        links = re.findall("href=[\"\'](.*?)[\"\']", plaintext)
        fl = []
        searched = []
        internal = []
        external = []
        hrefs = []
        i = 0
        def search(url):
            q = Queue()
            print(search.counter) 
            try:
                html = urllib.request.urlopen(url)
                with open("internal.txt", "a") as f:
                    f.write(f'{url}\n')
                text = html.read()
                plaintext = text.decode('utf8')
                links = re.findall("href=[\"\'](.*?)[\"\']", plaintext)
                for l in links:   
                    if l not in searched:
                        print(f"     --{l}")
                        searched.append(l)
                        if l.startswith('https://') or l.startswith('http://'):
                            external.append(l)
                        else:
                            q.put(l)
                while not q.empty():
                    
                    l=q.get()
                    print(f"hi-{l}")
                    try:
                        if l[0] == "/":
                            if l[:2] == '//':
                                link = l[2:]
                                with open("subs.txt", "a") as f:
                                    f.write(f'{link}\n')
                            else:
                                link = f"{self.domain[:-1]}{l}"
                                search(link)
                        else:
                            link = f"{url}{l}"
                            with open("internal.txt", "a") as f:
                                f.write(f'{link}\n')

                        print(link) 
                    except:
                        print('failed')       
            except:
                print(f"invalid url - {url}")
            finally:
                print("________________")    
                
                    
                    
                search.counter += 1
                print("________________") 

            
        search.counter = 0
        search(root)
        print(searched)
        for s in searched:
            with open("hrefs.txt","a") as f:
                f.write(f'{s}\n')

if __name__ == "__main__":
    t = spider(root,name)
    t.crawl()