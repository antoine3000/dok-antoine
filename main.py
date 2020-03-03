# dependencies
import os
import shutil
import warnings
from datetime import datetime
from jinja2 import Environment, FileSystemLoader
from markdown2 import markdown
from PIL import Image

# templates
env = Environment(loader=FileSystemLoader('templates'))
home_template = env.get_template('home.html')
index_template = env.get_template('index.html')
article_template = env.get_template('article.html')
flux_template = env.get_template('flux.html')
# misc
content_types = ['posts', 'pages', 'assignments']
base_width = 1200
media_ext = ['jpg', 'jpeg', 'png']
METADATA = {}
folder_html = 'public/'
folder_medias = 'public/medias/'
# Temporary fix
warnings.filterwarnings("ignore", "(Possibly )?corrupt EXIF data", UserWarning)

# Image utility
def image_util(old_file, new_file):
    if not os.path.isfile(new_file):
    # copy the original to public/media
        shutil.copy2(old_file, new_file)
        if new_file.endswith(tuple(media_ext)):
            img = Image.open(new_file)
            # resize the public/img file
            wpercent = (base_width/float(img.size[0]))
            hsize = int((float(img.size[1])*float(wpercent)))
            img = img.resize((base_width, hsize), Image.ANTIALIAS)
            img.save(new_file)

# purge public folder
for file_name in os.listdir(folder_html):
    if file_name.endswith('.html'):
        os.remove(folder_html + file_name)
# for file_name in os.listdir(folder_medias):
#     os.remove(folder_medias + file_name)

# generate articles
for content_type in content_types:
    content_path = 'content/' + content_type
    content_metadata_name = content_type + '_metadata'
    ARTICLES = {}
    ARTICLE_INFO = {}

    for article_dir in os.listdir(content_path):
        dir_path = content_path + '/' + article_dir
        article_slug = article_dir[11:]
        article_date = article_dir[:10]
        ARTICLE_INFO[article_slug] = article_date
        for item in os.listdir(dir_path):
            file_path = os.path.join(dir_path, item)
            if file_path.endswith('.md'):
                 # markdown file
                with open(file_path, 'r') as file:
                    ARTICLES[article_slug] = markdown(
                        file.read(), extras=['metadata', 'tables', 'target-blank-links'])
            else:
                # media file
                media_file_path = 'public/medias/{slug}'.format(slug=article_slug + '-' + item)
                image_util(file_path, media_file_path)

    # reverse order
    ARTICLES = {
        article: ARTICLES[article] for article in sorted(ARTICLES, key=lambda article: datetime.strptime(ARTICLE_INFO.get(article), '%Y-%m-%d'), reverse=True)
    }

    for article in ARTICLES:
        article_metadata = ARTICLES[article].metadata
        if 'tags' in article_metadata:
            tags = [article_metadata['tags']]
        else:
            tags = ''
        if 'thumbnail' in article_metadata:
            thumbnail = article_metadata['thumbnail']
        else:
            thumbnail = ''
        if 'subtitle' in article_metadata:
            subtitle = article_metadata['subtitle']
        else:
            subtitle = ''
        article_data = {
            'title': article_metadata['title'],
            'subtitle': subtitle,
            'content': ARTICLES[article],
            'thumbnail': thumbnail,
            'tags': tags,
            'date': ARTICLE_INFO.get(article),
            'slug': article
        }
        ARTICLES[article].metadata = article_data
        article_html = article_template.render(article=article_data)
        article_file_path = 'public/{slug}.html'.format(
            slug=article_data['slug'])
        os.makedirs(os.path.dirname(article_file_path), exist_ok=True)
        img_tag = '<img src ="medias/' + article_data['slug'] + '-'
        video_tag = '<video controls preload="auto"><source type ="video/mp4" src ="medias/' + article_data['slug'] + '-'
        doc_link = '<a target="_blank" href="medias/' + article_data['slug'] + '-'
        article_html = article_html.replace('<img src="', img_tag)
        article_html = article_html.replace('<video><source src="', video_tag)
        article_html = article_html.replace('<a target="_blank" href="files/', doc_link)
        with open(article_file_path, 'w') as file:
            file.write(article_html)

    METADATA[content_metadata_name] = [
        ARTICLES[article].metadata for article in ARTICLES]

# generate flux
FILES = {}
FLUX = {}
for file in os.listdir('content/flux'):
    file_path = 'content/flux/' + file
    title = file[11:]
    date = file[:10]
    media_file_path = 'public/medias/{slug}'.format(slug='flux-' + title)
    file_data = {
        'title': title,
        'slug': media_file_path,
        'date': date
    }
    FILES[file] = file_data
    image_util(file_path, media_file_path)

FILES = {
    file: FILES[file] for file in sorted(FILES, key=lambda file: datetime.strptime(FILES[file].get('date'), '%Y-%m-%d'), reverse=True)
}
FLUX['flux_metadata'] = [
    FILES[file] for file in FILES
]
flux_html = flux_template.render(flux = FLUX['flux_metadata'])
flux_html = flux_html.replace('<img src="public/', '<img src="')
with open('public/flux.html', 'w') as file:
    file.write(flux_html)


# generate home
home_html = home_template.render(
    posts=METADATA['posts_metadata'],
    pages=METADATA['pages_metadata'],
    assignments=METADATA['assignments_metadata'],
)
with open('public/index.html', 'w') as file:
    file.write(home_html)

# generate index
for key, value in METADATA.items():
    index_html = index_template.render(articles=value)
    index_name = key.replace("_metadata", "")
    filename = 'public/' + index_name + '.html'
    with open(filename, 'w') as file:
        file.write(index_html)

# counting
total_page = 0
total_media = 0
for file_name in os.listdir(folder_html):
    if file_name.endswith('.html'):
        total_page = total_page + 1
for file_name in os.listdir(folder_medias):
        total_media = total_media + 1
print('The website consists of', total_page, 'pages and', total_media, 'medias')
