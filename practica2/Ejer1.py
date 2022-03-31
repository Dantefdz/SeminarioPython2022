from urllib import request
README_URL = 'https://raw.githubusercontent.com/numpy/numpy/main/README.md'

page = request.urlopen(README_URL)

content_as_string = str(page.read())
lines = content_as_string.split('\\n')

lines_with_links = list(filter(lambda string: 'http' in string, lines))

print(' //////////////////////////////////Todas las linesas con links son://////////////////////////////////////')
for line in lines_with_links:
    print(line)