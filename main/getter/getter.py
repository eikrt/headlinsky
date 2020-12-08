import feedparser
def get_titles_from_xml(feed):
    print("Feed for: " + feed)
    newsfeed = feedparser.parse(feed)
    entries = newsfeed.entries
    titles = []
    for entry in newsfeed['entries']:
        titles.append(entry['title'])
    return titles
def get_titles():
    return get_titles_from_xml("data/news.xml")
