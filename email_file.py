import yagmail
import pandas as pd
from news_ import NewsFeed
from datetime import datetime, timedelta
import time

df = pd.read_excel("mails_list.xlsx")

print(df)
email = yagmail.SMTP(
        user="dailynewsaway@gmail.com",
        password="fevmnjqbyoghghzv")


def send_mail():
    news_feed = NewsFeed(interest=row.interest, from_date=yesterday, to_date=today, language='en')
    email.send(to=row.email,
               subject=f"Daily News Abount {row.interest}",
               contents=f"Hi {row.name} \n See what's on about {row.interest} today. \n {news_feed.get()}")


while True:
    executed = False
    if datetime.now().hour == 8 and datetime.now().minute == 1:

        yesterday = datetime.now() - timedelta(days=1)
        today = datetime.now()

        for index, row in df.iterrows():
            send_mail()
            executed = True

        if executed == False:
            time.sleep(120)


