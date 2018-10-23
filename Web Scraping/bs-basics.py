from bs4 import BeautifulSoup
html = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>First HTML Page</title>
</head>
<body>
  <div id="first">
    <h3 data-example="yes">hi</h3>
    <p>more text.</p>
  </div>
  <ol>
    <li class="special">This list item is special.</li>
    <li class="special">This list item is also special.</li>
    <li>This list item is not special.</li>
  </ol>
  <div data-example="yes">bye</div>
</body>
</html>
"""

soup = BeautifulSoup(html, "html.parser")
print(soup.body.div)
print("\n\n")

# same as above
# print(soup.find("div"))

## Finds all the instances of soup object where there is a class tag embedded
class_find = soup.find_all(class_ = "special")
class_find_v2 = soup.select(".special ")

## The above two are equivalent

print(class_find_v2)
print("\n\n")
d = soup.select("[data-example]")


css = soup.select("#first")
print(css)
# print(d)
