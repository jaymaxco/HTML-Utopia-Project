import os
from bs4 import BeautifulSoup

COMPONENTS_DIR = "components"

def read_file(filename):
    path = os.path.join(COMPONENTS_DIR, filename)
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f:
            return f.read()
    return ""

# Read main templates
head_content = read_file("head.html")
body_content = read_file("body.html")

# Map placeholders (or just empty tags) to partials
partials = {
    "<!--HEADER-->": "header.html",
    "<!--MAIN-->": "main.html",
    "<!--FOOTER-->": "footer.html"
}

# Replace placeholders in body with partial content
for placeholder, filename in partials.items():
    content = read_file(filename)
    body_content = body_content.replace(placeholder, content)

# Merge head and body
final_html = f"{head_content}\n{body_content}"

# Pretty-print using BeautifulSoup
soup = BeautifulSoup(final_html, "html.parser")
pretty_html = soup.prettify()

# Write output
with open("index.html", "w", encoding="utf-8") as f:
    f.write(pretty_html)

print("index.html created successfully with clean indentation!")
