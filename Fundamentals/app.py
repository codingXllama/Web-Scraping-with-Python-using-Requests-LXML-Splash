# telling lxml to open the html file to parse it
from lxml import etree

treeObject = etree.parse("../Fundamentals/src/web_page.html")

# print(etree.tostring(treeObject))

# Selecting the title of the html page using the treeObject.find()
pageTitle = treeObject.find("head/title")
# This prints the entire title tag
# print(etree.tostring(pageTitle))
# this prints the content only inside the title tag
print(pageTitle.text)

# Selecting and Printing the paragraph tag
pageParagraph = treeObject.find("body/p")
print(pageParagraph.text)


# Selecting and printing all the list items <li> tags between the ul tag element. This will print a list of item objects in memory location
ulTag = treeObject.findall("body/ul/li")
print(ulTag)

# Printing the text content for each li item
for liTag in ulTag:
    aTag = liTag.find('a')
    if aTag is not None:
        print(f"{liTag.text.strip()} {aTag.text}")
    else:
        print(liTag.text)
