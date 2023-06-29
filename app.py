# VERSION: 1.0
# AUTHORS: bacchilega

# LICENSING INFORMATION
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import os
import requests
from bs4 import BeautifulSoup

# URL of the page to scrape
url = "https://github.com/qbittorrent/search-plugins/wiki/Unofficial-search-plugins"

# Send a GET request to the webpage
response = requests.get(url)

# Parse the HTML content of the page with BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Find all <a> elements in the HTML
a_elements = soup.find_all('a')

# Filter out elements that don't have an href attribute ending with .py
py_links = [a['href'] for a in a_elements if a.get('href', '').endswith('.py')]

# Create directory if it doesn't exist
if not os.path.exists('Files'):
    os.makedirs('Files')

for i, url in enumerate(py_links, start=1):
    # If the link is relative, prepend the base URL
    if not url.startswith('http'):
        url = 'https://github.com' + url

    response = requests.get(url)

    filename = os.path.join('Files', url.split("/")[-1])

    # Specify 'utf-8' encoding when opening the file
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(response.text)

print("Download completed for {} files.".format(len(py_links)))
