import os
from bs4 import BeautifulSoup

HTML_FILE = os.path.join(os.path.dirname(os.path.dirname(__file__)), "index.html")

with open(HTML_FILE, "r", encoding="utf-8") as f:
    soup = BeautifulSoup(f, "html.parser")

def test_main_element_has_id_main():
    assert soup.find("main", id="main") is not None, "<main id='main'> not found"

def test_no_duplicates_in_dijital_cag_arastirmalari():
    header = soup.find("h4", string=lambda s: s and "Dijital Çağ Araştırmaları" in s)
    assert header is not None, "Section header not found"
    ol = header.find_next("ol")
    assert ol is not None, "Ordered list not found after section header"
    items = [li.get_text(strip=True) for li in ol.find_all("li")]
    assert len(items) == len(set(items)), "Duplicate list items found"
