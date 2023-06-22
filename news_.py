import requests


class NewsFeed:
    base_url = url = "https://newsapi.org/v2/" \
                     "everything?"
    api_key = "f99d79b5ace041bcbf35623860302bb8"

    def __init__(self, interest, from_date, to_date, language):
        self.language = language
        self.from_date = from_date
        self.to_date = to_date
        self.interest = interest

    def get(self):
        url = self._build_url()

        articles = self._get_articles(url)

        email_body = ""
        for article in articles:
            email_body = email_body + f"email_body {article['title']} \n the url is -  {article['url']}" + "\n\n"

        return email_body

    def _get_articles(self, url):
        res = requests.get(url)
        content = res.json()
        articles = content['articles']
        return articles

    def _build_url(self):
        url = f"{self.base_url}" \
              f"qInTitle={self.interest}&" \
              f"from={self.from_date}&" \
              f"to={self.to_date}&" \
              f"language={self.language}&" \
              f"apiKey={self.api_key}"

        return url
