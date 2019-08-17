# telling lxml to open the html file to parse it
from lxml import etree

tree = etree.parse("../Fundamentals/src/web_page.html")

print(etree.tostring(tree))
