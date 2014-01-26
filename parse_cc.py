from bs4 import BeautifulSoup
from gmail import Gmail
import email
from wordpress_xmlrpc import Client, WordPressPost
from wordpress_xmlrpc.methods.posts import GetPosts, NewPost
from wordpress_xmlrpc.methods.users import GetUserInfo
from wordpress_xmlrpc.methods.demo import SayHello
import yaml
import baker

CHUNK_MIN = 500
TITLE_MIN = 10
CONFIG_FILE = 'yamzam.yml'

def _get_title(bottom_child):
    """
    See if we can find the title for this section of HTML
    """
    try:
        subchild = bottom_child.children.next()
        return _get_title(subchild)
    except:
        return str(bottom_child)

def _get_table_content(table):
    """
    Weed out table entries from the html
    """
    output = ''
    for child in table.children:
        if child.name in ['tr', 'td', 'table', 'tbody']:
            new_output = _get_table_content(child)
            output += new_output
        else:
            try:
                output += str(child)
            except UnicodeEncodeError:
                pass
    return output

def _make_post(client, title, content):
    """
    Make a post on the wordpress site for this content item.
    """
    print 'MAKING POST FOR:', title
    post = WordPressPost()
    post.title = title
    post.content = content
    post.terms_names = {
      'post_tag': ['test', 'firstpost'],
      'category': ['Introductions', 'Tests']
    }
    post.publish = True
    client.call(NewPost(post))

def parse_and_post(htmldoc, client):
    """
    Main entry point for parsing the email
    """
    soup = BeautifulSoup(htmldoc)
    tables = soup.find_all('table')
    for table in tables:
        title = _get_title(table)
        content = _get_table_content(table)
        if len(title) < TITLE_MIN or len(content) < CHUNK_MIN:
            continue
        _make_post(client, title, content)

def _get_an_email(gmail_configs, index):
    """
    Log in to gmail using credentials from our config file and retrieve
    an email from our sender with a given index-number.
    """
    g = Gmail()
    g.login(gmail_configs['username'], gmail_configs['password'])
    msg = g.inbox().mail(sender=gmail_configs['source_address'])[index]
    msg.fetch()
    raw_message = msg.message
    html_body = ''
    if raw_message.get_content_maintype() == "multipart":
        for content in raw_message.walk():
            print content.get_content_type()
            if content.get_content_type() == "text/html":
                html_body = content.get_payload(decode=True)
    return html_body

@baker.command
def fetch_and_post(index):
    """
    Main entry point. Use this to fetch an email from gmail and create wordpress
    posts. The email needs to be in constant-contact format.
    """
    index = int(index)
    configs = yaml.load(open(CONFIG_FILE).read())
    wp_configs = configs['wordpress']
    gmail_configs = configs['gmail']
    client = Client(wp_configs['url'], wp_configs['username'], wp_configs['password'])

    htmldoc = _get_an_email(gmail_configs, index)
    parse_and_post(htmldoc, client)

baker.run()
