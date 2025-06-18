import os, re
import markdown

with open('README.md') as f:
    readme = f.read()

pattern = re.compile(r'^## \[(.*?)\]\((.*?)\)\n(.*?)(?=^## |\Z)', re.S | re.M)
entries = []
os.makedirs('site/pages', exist_ok=True)
template = open('site/template.html').read()

for match in pattern.finditer(readme):
    name, link, details = match.groups()
    slug = re.sub(r'[^a-zA-Z0-9]+', '-', name.lower()).strip('-')
    html_content = markdown.markdown(details)
    content = template.replace('{{title}}', name).replace('{{content}}', html_content)
    with open(f'site/pages/{slug}.html', 'w') as f:
        f.write(content)
    entries.append((name, f'pages/{slug}.html', link))

# Create index
index_items = '\n'.join(f'<li><a href="{p}">{n}</a> - <a href="{url}">Website</a></li>' for n,p,url in entries)
index_html = f"""<!DOCTYPE html>
<html><head><meta charset='utf-8'><title>Awesome AI Agents</title>
<link rel='stylesheet' href='style.css'></head>
<body><header><h1>Awesome AI Agents</h1></header>
<main class='container'>
<ul>{index_items}</ul>
</main><footer>&copy; 2025 Awesome AI Agents</footer></body></html>"""
open('site/index.html','w').write(index_html)
