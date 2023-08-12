from plyer import notification
# Platform-independent api to use features commonly found on various platforms.
import requests
# Requests module allows you to send HTTP requests using Python.
import time
from bs4 import BeautifulSoup
# Python library for pulling data out of HTML and XML files

def covid_case():
    def notification(title,message):
        notification.notify(
            title = title,
            message = message,
            app_icon = "C://Users//Desktop//CompProject//image.ico",
            timeout = 15
        )

    def casesData(url):
        r = requests.get(url)
        return r.text

    if __name__ == "__main__":
        notification("Suki ","Covid-19 Daily state-wise updates")
        htmlData = casesData("https://web.archive.org/web/20200322141055/https://www.mohfw.gov.in/")
        soup = BeautifulSoup(htmlData, 'html.parser')
        stringData = ""
        for tr in soup.find_all('tbody')[1].find_all('tr'):
            stringData += tr.get_text()
        stringData=stringData[1:]
        itemList=stringData.split('\n\n')
        states=['Karnataka','Delhi','Andhra Pradesh','Bihar','Rajasthan']
        for item in itemList[0:23]:
            dataList=item.split('\n')
            if dataList[1] in states:
                print(dataList)
                nTitle=" Today's Omicron covid_case In India "
                nText= f"State {dataList[1]}\nIndian Nationals: {dataList[2]}Foreign nationals:{dataList[3]}\nCured: {dataList[3]}\nDeaths: {dataList[5]}"
                notification(nTitle,nText)
                time.sleep(2)

covid_case()
