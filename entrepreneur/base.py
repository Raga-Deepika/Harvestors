import requests
from bs4 import BeautifulSoup
from dateparser import parse
from datetime import datetime


def entre_main(category, page):
    try:
        entrepreneurDict = {}
        entrepreneurDict['success'] = True
        base_url = 'https://www.entrepreneur.com/topic'
        link = '{0}/{1}/{2}'.format(base_url, category, page)
        try:
            req = requests.get(link)
        except Exception as e:
            entrepreneurDict['success'] = False
            entrepreneurDict['errorMessage'] = str(e)
            return entrepreneurDict
        data = []
        posted_at = ''
        if req.status_code == 200:
            soup = BeautifulSoup(req.content, 'lxml')
            try:
                card = soup.find_all('div', class_='block')
            except Exception as e:
                card = []

            for item in card:
                content = ''
                obj = {}
                entrepreneurDict['success'] = True
                try:
                    titles = item.find('h3').text.strip()
                except:
                    titles = None
                try:
                    url = item.h3.a.get('href')
                    base_url1 = base_url.split('.com')[0] + '.com'
                    links = '{0}{1}'.format(base_url1, url)
                except:
                    url = None
                try:
                    req1 = requests.get(links)
                except Exception as e:
                    entrepreneurDict['success'] = False
                    entrepreneurDict['errorMessage'] = str(e)
                soup1 = BeautifulSoup(req1.content, 'lxml')
                try:
                    snip = item.find('div', class_='deck')
                    if snip is None:
                        snip1 = soup1.find('div', class_='art-deck').text.strip()
                        obj['snippet'] = snip1
                    else:
                        obj['snippet'] = snip.text.strip()
                except:
                    snip = None
                card1 = soup1.find('div', class_='art-v2-body')
                try:
                    date = card1.div.time.get('content')
                    posted_at = parse(date)
                except:
                    date = None
                try:
                    contents = card1.find_all({'p', 'ul'})
                    for ps in contents:
                        cont = ps.text.strip()
                        content += cont
                except:
                    contents = None
                obj['title'] = titles
                obj['url'] = links
                obj['date'] = posted_at
                obj['content'] = content
                obj['category'] = category
                obj['source'] = 'entrepreneur'
                data.append(obj)
            entrepreneurDict['data'] = data
            entrepreneurDict['created_at'] = datetime.now()
            entrepreneurDict['updated_at'] = datetime.now()
            return entrepreneurDict
    except Exception as e:
        print(str(e))
        return None
