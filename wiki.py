# Import libraries 
from bs4 import BeautifulSoup
import requests
from urllib.request import urlparse
import re

# !-- Change for starting URL --! #
inputUrl = "https://en.wikipedia.org/wiki/Special:Random"
# !-- Change for ending URL --! #
endUrl = "https://en.wikipedia.org/wiki/Star_Wars"

# Parse the page for the urls
initial_page = requests.get(inputUrl)
page = BeautifulSoup(initial_page.text, 'html.parser')
mainBody = page.find(id="bodyContent")


# Only gets wikipedia pages and removes special links
def internal_not_special(href):
	if href:
		if re.compile('^/wiki/').search(href):
			if not re.compile('/\w+:').search(href):
				if not re.compile('#').search(href):
					return True
	return False

# Create a list of visited urls so we don't waste time
visited = []


# Using a DFS to iterate through the first link of every link 
# 6 deep, then go back to get the second link, and so on.
# Takes longer if star wars is somewhere on the page since I don't
# Check the whole page first.
def dfs(link: str, depth: int) -> bool:
  """
  link: url of the wikipedia page to check for star wars
  depth: how far we are from the initial page
  
  returns: ???
  """
  # If we aren't at 6 deep alraedy
  if depth < 6:
  	# Get the links of the page
    nextPage = requests.get(link)
    page = BeautifulSoup(nextPage.text, 'html.parser')
    mainBody = page.find(id="bodyContent")
    links = mainBody.find_all('a', href=internal_not_special)
    # Iterate through the page links
    for _ in range(depth):
      print("  ", end='')
    print(f"{depth}: {link}")
    for url in links:
      # Convert the url
      url_get = ("https://en.wikipedia.org" + url.get('href'))
      print(url_get)
      # If the url is star wars, print the path
      if url_get == endUrl:
        print("Found Star Wars in " + str(depth) + " jumps")
        return True
      # If we haven't visted the url
      elif url_get not in visited:
        # Add the url to the list
        visited.append(url_get)
        # If we haven't returned false, recurse
        if dfs(url_get, depth+1):
          # print(f"Found: {depth}: {link}")
          return True
      # If we have visited the link, return false
      else:
        return False
    # Return false if we have gone through all of the links
    print("No such thing as Star Wars existed")
    return False
  # If we are over 6 deep, return false
  else:
    return False

# Call the function
dfs(inputUrl, 0)


# End of program