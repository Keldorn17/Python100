from bs4 import BeautifulSoup
import requests
# import lxml  # lxml.parser


# with open("website.html") as data:
#     web_data: str = data.read()
#
# soup: BeautifulSoup = BeautifulSoup(web_data, "html.parser")
# print(soup.title)
# print(soup.title.string)
# print(soup.prettify())

# print(soup.li)

# all_anchor_tags = soup.find_all(name="a")
# print(all_anchor_tags)
#
# for tag in all_anchor_tags:
#     # print(tag.getText())
#     print(tag.get("href"))

# heading = soup.find(name="h1", id="name")
# print(heading)

# section_heading = soup.find(name="h3", class_="heading")
# print(section_heading.getText())

# company_url = soup.select_one(selector="p a")
# print(company_url)
#
# name = soup.select_one(selector="#name")
# print(name)
#
# heading = soup.select(selector=".heading")
# print(heading)

response = requests.get("https://news.ycombinator.com/news")
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")

article_tag = soup.find_all(name="span", class_="titleline")
article_text = []
article_link = []
for article in article_tag:
    article_text.append(article.find(name="a").getText())
    article_link.append(article.find(name="a").get("href"))
subtexts = soup.findAll(class_="subtext")
# Ternary Operator
# <expression_if_true> if <condition> else <expression_if_false>
# List Comprehension
# [<results> for <item> in <iterable> if <condition>]
# Dictionary Comprehension
# {<result_key>: <result_value> for (<key>, <value>) in <dict>.items() if <condition>}
# Ternary Operator with List Comprehension
# [<expression_if_true> if <condition> else <expression_if_false> for <item> in <iterable> if <condition>]
article_upvote = [int(line.span.span.getText().strip(" points")) if line.span.span else 0 for line in subtexts]

largest_number = max(article_upvote)
largest_index = article_upvote.index(largest_number)

print(
    f"Most upvoted article: {article_text[largest_index]}\n"
    f"Number of upvotes: {article_upvote[largest_index]} points\n"
    f"Available at: {article_link[largest_index]}."
)
