import requests
import urllib3
import certifi
from bs4 import BeautifulSoup
import sys

args = sys.argv

if len(args) > 1:
    urlName = args[1]
    url = urlName + "/participation/"
    http = urllib3.PoolManager(
            cert_reqs='CERT_REQUIRED',
            ca_certs=certifi.where())
    r = http.request("GET", url)

    if r.status == 200:
        soup = BeautifulSoup(r.data, "html.parser")

        listOfParticipants = soup.find_all(class_="participation_table_area")

        print("## 参加者")

        for participant in listOfParticipants:
            label = participant.select("table > thead > tr > th > .label_ptype_name")
            print("\n### " + label[0].text + "\n")

            users = participant.find_all(class_="user_info")

            for user in users:
                userName = user.select(".user_info > .display_name > a")
                print("- [ ] " + userName[0].text)
    else:
        print ("NotFound: " + url)

else:
    print("引数にイベントのurlを指定してください。")
