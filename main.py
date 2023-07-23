import feedparser
# this is the feedparser module
import bs4

# User can input an RSS feed URL
# The program will take the link and return the title, description, and link of the feed

if __name__ == "__main__":
    link = input("Enter an RSS feed URL: ")
    # User inputs the RSS feed URL

    feed = feedparser.parse(link)
    # The feedparser module parses the RSS feed URL

    print("Title: " + feed.feed.title)
    description = bs4.BeautifulSoup(feed.feed.description, "html.parser")
    # The description is in HTML format, so we use the BeautifulSoup module to parse it
    print("Description: " + description.get_text())
    print("Link: " + feed.feed.link)
