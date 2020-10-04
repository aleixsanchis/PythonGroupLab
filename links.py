from urllib.error import HTTPError, URLError
import urllib.request
def is_link_live(url):
  try :
    urllib.request.urlopen(url, None, 4)
    return True
  except (URLError, ValueError):
    return False
  
def test_page_links(url):
  links = extract_page_links(url)
  for link in links:
    if not is_link_live(link):
      print(link)

def extract_page_links(url):
  return []

def links_prompt():
  url = input("Enter a URL: ")
  if is_link_live(url):
    print("This link is live")
  else:
    print("This link is dead")
