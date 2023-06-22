# f99d79b5ace041bcbf35623860302bb8
from news_ import NewsFeed

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    news_feed = NewsFeed(interest='tesla', from_date="2023-06-20", to_date="2023-06-21", language="en")
    news_feed.get()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
