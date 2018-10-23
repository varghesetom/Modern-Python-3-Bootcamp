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

## if only one next_sibling will only show the '\n' so call it again
## next_sibling goes to the next element in the same level in hierarchy
data = soup.body.contents[1].next_sibling.next_sibling

### same as

data2 = soup.body.contents[1].find_next_sibling()

data3 = soup.select("[data-example]")[1].contents
print(data3)
