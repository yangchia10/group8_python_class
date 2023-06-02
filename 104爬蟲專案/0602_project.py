import requests
from bs4 import BeautifulSoup
import time
import pandas as pd

class Jobs:    
    def __init__ (self, keyword):
        self.keyword = keyword
        self.data = []

    def getData(self):
        page = 1
        
        data = []

        while True:
            url = f'https://www.104.com.tw/jobs/search/?ro=0&kwop=7&keyword={self.keyword}&expansionType=area%2Cspec%2Ccom%2Cjob%2Cwf%2Cwktm&order=15&asc=0&page={page}&mode=s&jobsource=2018indexpoc&langFlag=0&langStatus=0&recommendJob=1&hotJob=1'
            res = requests.get(url)
            soup = BeautifulSoup(res.text)

            jobs = soup.find_all('article', class_='b-block--top-bord job-list-item b-clearfix js-job-item')

            if not jobs:
            #if jobs==[]:
                break

            print("----------------------")
            print("現在正在讀取第" + str(page) + "頁")
            print("----------------------")


            for job in jobs:
                title = job['data-job-name'].strip()
                company = job('li')[1].text.strip()
                URL = 'https:' + job.find("a", class_='js-job-link')['href']

                dict1 = {"公司名稱": company, "職缺名稱": title, "職缺連結": URL}
                data.append(dict1)

            page += 1
            print(title)


        self.data = data
    def toExcel(self):
        df = pd.DataFrame(columns = self.data[0].keys(), data = self.data)
        path = self.keyword + ".xlsx" #定義檔案路徑 #當檔案名稱有中文要加r
        df.to_excel(path, index = False)
        print('儲存', path)
        
        return self.data
        
           

if __name__ == "__main__":
    keyword = "數據分析業務"
    data = Jobs(keyword)
    data.getData()
    data.toExcel()
    
