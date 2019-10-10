from operator import itemgetter
import requests

#Make an Api call and store the response
url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(url)
print(f"Status Code: {r.status_code}")


#process information about each submission

submission_ids = r.json()
submission_dicts = []
for submission_id in submission_ids:
    #make seperate api call for each submission
    url = f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json"
    r = requests.get(url)
    #print(f"id: {submission_id}\tstatus: {r.status_code}")
    response_dict = r.json()
    #print(response_dict)
    #Build a dictionary for each article
    submission_dict = {
        'title' : response_dict['title'],
        'hn_link': f"http://news.ycombinator.com/item?id={submission_id}",
        'comments': response_dict.get('descendants', 0),
        'score': response_dict.get('score', 0)
    }
    submission_dicts.append(submission_dict)


submission_dicts = sorted(submission_dicts, key=itemgetter('score'), reverse=True)


top_ten_url = submission_dicts[0:6]

for item in top_ten_url:
    print(f"\nTitle: {item['title']}")
    print(f"Url: {item['hn_link']}")


# for submission_dict in submission_dicts:
#     print(f"\nTitle: {submission_dict['title']}")
#     print(f"Discussion link: {submission_dict['hn_link']}")
#     print(f"Comments: {submission_dict['comments']}")
#     print(f"Score: {submission_dict['score']}")

