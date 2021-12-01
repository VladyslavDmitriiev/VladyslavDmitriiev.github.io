import markdown


with open('src/index.md', 'r') as md:
  markdown_file = md.read()

markdown_to_html = markdown.markdown(markdown_file)

with open('src/template.html', 'r') as template:
  template_file = template.read()

with open('index.html', 'w') as index:
  index.write(template_file)
  index.write('\n')
  index.write(markdown_to_html)
  index.write('\n')
  index.write('\n</body>\n</html>')
