import os
import re
from pathlib import Path

POSTS_DIR = Path('posts')
SITE_DIR = Path('site')
TEMPLATE_PATH = Path('templates/base.html')

# Simple markdown to HTML converter
def md_to_html(md_text: str) -> str:
    html_lines = []
    for line in md_text.splitlines():
        line = line.rstrip()
        if line.startswith('### '):
            html_lines.append(f'<h3>{line[4:]}</h3>')
        elif line.startswith('## '):
            html_lines.append(f'<h2>{line[3:]}</h2>')
        elif line.startswith('# '):
            html_lines.append(f'<h1>{line[2:]}</h1>')
        elif line:
            html_lines.append(f'<p>{line}</p>')
        else:
            html_lines.append('')
    return '\n'.join(html_lines)


def load_template() -> str:
    with open(TEMPLATE_PATH, 'r', encoding='utf-8') as f:
        return f.read()


def render_page(title: str, content: str, template: str) -> str:
    return template.format(title=title, content=content)


def generate_blog():
    SITE_DIR.mkdir(exist_ok=True)
    template = load_template()
    posts = []
    for md_file in POSTS_DIR.glob('*.md'):
        with open(md_file, 'r', encoding='utf-8') as f:
            md_text = f.read()
        # Title is first line without '# '
        first_line = md_text.splitlines()[0]
        title = re.sub(r'^#\s+', '', first_line)
        html_content = md_to_html(md_text)
        post_filename = md_file.stem + '.html'
        html_page = render_page(title, html_content, template)
        with open(SITE_DIR / post_filename, 'w', encoding='utf-8') as f:
            f.write(html_page)
        posts.append((title, post_filename))

    # Generate index.html
    index_items = '\n'.join(
        f'<li><a href="{filename}">{title}</a></li>' for title, filename in posts
    )
    index_content = f'<h2>Posts</h2>\n<ul>\n{index_items}\n</ul>'
    index_page = render_page('Home', index_content, template)
    with open(SITE_DIR / 'index.html', 'w', encoding='utf-8') as f:
        f.write(index_page)


if __name__ == '__main__':
    generate_blog()
