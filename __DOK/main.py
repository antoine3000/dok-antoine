import os
import shutil
from markdown2 import markdown
from PIL import Image
from jinja2 import Environment, FileSystemLoader
from bs4 import BeautifulSoup
from datetime import datetime
from feedgen.feed import FeedGenerator
import rcssmin
import sass
import yaml

c = 'content/'
m = 'public/medias/'
a = "public/assets/"
env = Environment(loader=FileSystemLoader('__DOK/templates'))
scss_file = "assets/css/main.scss"
scss_map = {scss_file: "public/assets/main.css"}
css_map = {"public/assets/main.css": "public/assets/main.min.css"}
fonts_path_dok = '__DOK/assets/fonts/'
fonts_path_user = 'assets/fonts/'
fonts_public = 'public/assets/fonts/'

articles = {}
flux = {}
tags = {}

print('')
print('--------------------------')
print('Dok')
print('--------------------------')


def contains_folder(folder):
    items = os.listdir(folder)
    contains_folder = False
    for item in items:
        if os.path.isdir(folder + '/' + item):
            contains_folder = True
    return contains_folder


def image_process(origin, destination):
    if not os.path.isfile(destination):
        shutil.copy2(origin, destination)
        image_max_size = 1200
        fill_color = '#FFFFFF'
        if destination.endswith(tuple(['jpg', 'jpeg', 'png'])):
            img = Image.open(destination)
            if img.mode in ('RGBA', 'LA'):
                background = Image.new(img.mode[:-1], img.size, fill_color)
                background.paste(img, img.split()[-1])
                img = background
            wpercent = (image_max_size/float(img.size[0]))
            hsize = int((float(img.size[1])*float(wpercent)))
            img = img.resize((image_max_size, hsize), Image.ANTIALIAS)
            img.save(destination)


def article_items(slug, path):
    article_content_list = os.listdir(path)
    for item in article_content_list:
        item_path = path + '/' + item
        if item.endswith('.md'):
            with open(item_path, 'r') as file:
                md = markdown(file.read(), extras=[
                    'metadata', 'tables', 'target-blank-links', 'toc'])
                articles[slug]['content'] = md
        elif not os.path.isdir(item_path):
            media_path = m + slug + '-' + item
            image_process(item_path, media_path)


def metadata(article, slug, level, parent=None):
    article_metadata = articles[slug]['content'].metadata
    article_metadata['title'] = article_metadata['title']
    article_metadata['content'] = articles[slug]['content']
    article_metadata['slug'] = slug
    publication_date = datetime.strptime(
        article[:10], '%Y-%m-%d').strftime('%d/%m/%Y')
    article_metadata['publication_date'] = publication_date
    if 'last_update' in article_metadata:
        article_metadata['last_update'] = datetime.strptime(
            article_metadata['last_update'], '%Y-%m-%d').strftime('%d/%m/%Y')
    else:
        article_metadata['last_update'] = publication_date
    article_metadata['level'] = level
    if articles[slug]['content'].toc_html:
        article_metadata['toc'] = articles[slug]['content'].toc_html
    if 'tags' in article_metadata:
        article_tags = article_metadata['tags'].split(', ')
        articles[slug]['content'].metadata['tags'] = article_tags
    if parent is not None:
        article_metadata['parent'] = parent
    articles[slug]['metadata'] = article_metadata
    return article_metadata


def wrap(to_wrap, wrap_in):
    contents = to_wrap.replace_with(wrap_in)
    wrap_in.append(contents)


def html_update(html, slug):
    img_tag = '<img loading="lazy" src ="medias/' + slug + '-'
    video_tag = '<video controls preload="auto"><source type ="video/mp4" src ="medias/' + slug + '-'
    file_link = '<a target="_blank" class="link-file" href="medias/' + slug + '-'
    html = html.replace('<img src="', img_tag)
    html = html.replace('<video><source src="', video_tag)
    html = html.replace('<p><video', '<video')
    html = html.replace('</video></p>', '</video>')
    html = html.replace('<table>', '<div class="table"><table>')
    html = html.replace('</table>', '</table></div>')
    html = html.replace('<a target="_blank" href="file:', file_link)
    html = html.replace('<p>TODO:', '<p class="todo">To do:')
    html = html.replace('href="button:', 'class="btn" href="')
    # figure
    soup = BeautifulSoup(html, 'lxml')
    for img_tag in soup.findAll('img'):
        caption = soup.new_tag('figcaption')
        caption.append(img_tag['alt'])
        img_tag.append(caption)
        fig_tag = soup.new_tag("figure")
        img_src = img_tag['src']

        if "large:" in img_src:
            fig_tag['class'] = 'lg'
            img_tag['src'] = img_src.replace('large:', '')
        elif "small:" in img_src:
            fig_tag['class'] = 'sm'
            img_tag['src'] = img_src.replace('small:', '')
        else:
            fig_tag['class'] = 'md'

        if ":flux" in img_src:
            img_tag['src'] = img_tag['src'].replace(':flux', '')
            image_flux(str(img_tag['src']), slug)

        wrap(img_tag, fig_tag)
    html = str(soup)
    if (soup.select('.article--sub')):
        articles_sub = soup.select('.article--sub')
        for article_sub in articles_sub:
            article_sub_slug = article_sub.get('id')
            article_imgs = article_sub.select('img')
            article_vids = article_sub.select('video source')
            article_files = article_sub.select('.link-file')
            for article_img in article_imgs:
                article_sub_img_src = article_img['src'].replace(
                    'medias/' + slug, 'medias/' + article_sub_slug)
                article_img['src'] = article_sub_img_src
            for article_vid in article_vids:
                article_sub_vid = article_vid['src'].replace(
                    'medias/' + slug, 'medias/' + article_sub_slug)
                article_vid['src'] = article_sub_vid
            for article_file in article_files:
                article_sub_file = article_file['href'].replace(
                    'medias/' + slug, 'medias/' + article_sub_slug)
                article_file['href'] = article_sub_file
    html = str(soup)
    html = html.replace('<p><figure', '<figure')
    html = html.replace('</img></figure></p>', '</figure>')
    html = html.replace('</img></figure>', '</figure>')
    html = html.replace('</figure></p>', '</figure>')
    return (html)


def content_order(list):
    list.sort()
    for item in list:
        if item == '.DS_Store':
            list.remove(item)


def image_flux(image, slug):
    container = articles[slug]['metadata']['title']
    if (os.path.isfile('public/' + image)) and (not image in flux):
        flux[image] = {}
        flux[image]['image'] = image
        flux[image]['link'] = slug
        flux[image]['container'] = container


# Make directories if they don't exist
if not os.path.exists(m):
    os.makedirs(m)

if not os.path.exists(a):
    os.makedirs(a)

if not os.path.exists(fonts_public):
    os.makedirs(fonts_public)

# get everything
content_0 = os.listdir(c)
content_order(content_0)
for folder in content_0:
    # level 1
    folder_slug = folder[11:]
    articles[folder_slug] = {}
    article_items(folder_slug,  c + folder)
    articles[folder_slug]['metadata'] = metadata(folder, folder_slug, 1)
    if contains_folder(c + folder):
        # level 2
        content_1 = os.listdir(c + folder)
        content_order(content_1)
        for subfolder in content_1:
            if os.path.isdir(c + folder + '/' + subfolder):
                subfolder_slug = folder_slug + "-" + subfolder[11:]
                articles[subfolder_slug] = {}
                article_items(subfolder_slug,  c + folder + '/' + subfolder)
                articles[subfolder_slug]['metadata'] = metadata(
                    subfolder, subfolder_slug, 2, folder_slug)

articles_metadata = [articles[article]['metadata'] for article in articles]

print("⁂  Data: Collected")
print("⁂  Images: Processed")

# Re-organize the stuff I need
for article in articles:
    article_metadata = articles[article]['metadata']
    if 'tags' in article_metadata:
        # tags
        article_tags = article_metadata['tags']
        for tag in article_tags:
            tag = tag.strip()
            if not tag in tags:
                tags[tag] = []
            tags[tag].append(article_metadata)
    if 'parent' in article_metadata:
        parent = article_metadata['parent']
        parent_metadata = articles[parent]['metadata']
        articles[article]['metadata']['parent'] = []
        articles[article]['metadata']['parent'].append(parent_metadata)
        if not 'childs' in parent_metadata:
            parent_metadata['childs'] = []
        parent_metadata['childs'].append(articles[article]['metadata'])
print("⁂  Tags: Organized")

# Settings
settings_file = 'settings.yml'
with open('__DOK/' + settings_file, 'r') as file:
    settings = yaml.load(file, Loader=yaml.FullLoader)
if os.path.isfile(settings_file):
    with open(settings_file, 'r') as file:
        settings_user = yaml.load(file, Loader=yaml.FullLoader)

settings.update(settings_user)

# Generate article pages
article_template = env.get_template('article.html')
for article in articles:
    article_metadata = articles[article]['metadata']
    article_url = 'public/' + article_metadata['slug'] + '.html'
    article_html = article_template.render(
        article=article_metadata, settings=settings)
    article_html_updated = html_update(article_html, article_metadata['slug'])
    with open(article_url, 'w') as file:
        file.write(article_html_updated)
print("⁂  Article pages: Created")

# Generate tag pages
tag_template = env.get_template('tag.html')
for tag in tags:
    tag_url = 'public/' + tag + '.html'
    tag_html = tag_template.render(
        title=tag, articles=tags[tag], settings=settings)
    with open(tag_url, 'w') as file:
        file.write(tag_html)
print("⁂  Tag pages: Created")

# Generate Flux page
flux_metadata = [flux[item] for item in flux]
flux_metadata.reverse()
flux_template = env.get_template('flux.html')
flux_html = flux_template.render(articles=flux_metadata, settings=settings)
flux_slug = settings['flux']['slug']
with open('public/' + flux_slug + '.html', 'w') as file:
    file.write(flux_html)
print("⁂  " + flux_slug + ": Created")

# Reverse order
articles_metadata.reverse()

# Generate content page
content_template = env.get_template('content.html')
content_html = content_template.render(
    articles=articles_metadata, tags=tags, settings=settings)
with open('public/content.html', 'w') as file:
    file.write(content_html)
print("⁂  Content page: Created")

# Generate home page
home_template = env.get_template('home.html')
home_html = home_template.render(articles=articles_metadata, settings=settings)
with open('public/index.html', 'w') as file:
    file.write(home_html)
print("⁂  Home page: Created")

# Generate RSS feed
fg = FeedGenerator()
main_url = settings['main_url']
fg.title(settings['title'])
fg.author({'name': settings['author_name']})
fg.link(href=main_url, rel='alternate')
fg.subtitle(settings['description'])
fg.language(settings['language'])
rssfeed = fg.rss_str(pretty=True)

for article in articles_metadata:
    if 'last_update' in article.keys():
        date = article['last_update']
    else:
        date = article['publication_date']
    if not "draft" in article.values():
        fe = fg.add_entry()
        fe.title(article['title'])
        fe.link(href=main_url + '/' + article['slug'] + '.html')
        fe.author({'name': settings['author_name']})
        fe.pubDate(datetime.strptime(date,
                                     '%d/%m/%Y').strftime('%a %b %d %H:%M:%S %Y') + ' +0200')
        fe.description(article['content'][:800] + '...')
fg.rss_file('public/rss.xml')
print("⁂  RSS Feed: Updated")

# Scss to css


def compile_scss(scss):
    for source, dest in scss.items():
        mode = 'a' if os.path.exists(dest) else 'w'
        with open(dest, "w") as outfile:
            outfile.write(sass.compile(filename=source))


def minify_css(css):
    for source, dest in css.items():
        with open(source, "r") as infile:
            with open(dest, "w") as outfile:
                outfile.write(rcssmin.cssmin(infile.read()))


# Copy fonts to public
if os.path.isdir(fonts_path_user):
    fonts_path = fonts_path_user
else:
    fonts_path = fonts_path_dok

fonts = os.listdir(fonts_path)
for font_file in fonts:
    if not os.path.isfile(fonts_public + font_file):
        shutil.copy2(fonts_path + font_file, fonts_public + font_file)

# Compile, minimize css
if os.path.isfile(scss_file):
    compile_scss(scss_map)
    print("⁂  SCSS: compiled")
    minify_css(css_map)
    print("⁂  CSS: minified")

print('--------------------------')
print('And voilà.')
print('--------------------------')
print('')
