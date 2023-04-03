import requests
from bs4 import BeautifulSoup
from send_mail import send_email
from .. import secret

def hacker_news():
    url = "https://news.ycombinator.com/"
    response = requests.get(url).text

    soup = BeautifulSoup(response, "lxml")
    titles = soup.find_all(class_="titlelink")
    scores = soup.find_all(class_="score")
    links = [title.get("href") for title in titles]

    #Getting only the int from scores and saving it in score_int_list after that getting the highest int and the index of it
    score_list = [score.text for score in scores]
    score_points_string_list = [score2.split(" ") for score2 in score_list]
    score_int_list = [int(score3[0]) for score3 in score_points_string_list]
    highest_points = max(score_int_list)
    index_highest_points = score_int_list.index(highest_points)

    #Get the link with the hihgest points
    link_with_hihgest_points = links[index_highest_points]

    #Getting the title with the highest points
    titles_list = [title.text for title in titles]
    title_with_highest_points = titles_list[index_highest_points]

    send_email(secret.PERSONAL_EMAIL, 'Hacker News for German from German', f"Hey German,\n\n{title_with_highest_points} is todays title with the highest points it has {highest_points} points! The link to this post is: {link_with_hihgest_points}\n\nLiebe Grüße\nGerman")

if __name__ == "__main__":
    hacker_news()    