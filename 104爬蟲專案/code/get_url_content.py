import pandas as pd
import requests
from bs4 import BeautifulSoup
from lxml import html

jobs = pd.read_excel("/Users/chentingen/group8_python_class/數據分析業務.xlsx")

print(jobs)

#修改list資料變成string，因為在excel中比較好處理
def list2string(list_):
    if type(list_) == str:
        return list_
    elif not list_:                 #空list
        return ""
    elif type(list_) == list:
        try:
            output = ",".join(list_)
        except:
            output = ""
        return output
    else:
        print("型態錯誤，非list&str, 回傳空白")
        return ""
    
#從個別職缺的網頁中取得資料
def get_data(url):
    res = requests.get(url)
    tree = html.fromstring(res.text)
    data_dict = {}
    title = tree.xpath("/html/body/div[2]/div/div[1]/div[2]/div/div/div[1]/h1")
    company = tree.xpath("/html/body/div[2]/div/div[1]/div[2]/div/div/div[1]/div/a[1]")
    work = tree.xpath("/html/body/div[2]/div/div[2]/div/div[1]/div[1]/div[2]/div[1]/p")
    title_category = []
    title_category_e = tree.xpath("/html/body/div[2]/div/div[2]/div/div[1]/div[1]/div[2]/div[2]/div[2]/div/div//*/div/div/u")
    for index, n in enumerate(title_category_e):
        title_category.append(n.text)

    salary = tree.xpath("/html/body/div[2]/div/div[2]/div/div[1]/div[1]/div[2]/div[3]/div[2]/div/p")
    work_nature = tree.xpath("/html/body/div[2]/div/div[2]/div/div[1]/div[1]/div[2]/div[4]/div[2]/div")
    location = tree.xpath("/html/body/div[2]/div/div[2]/div/div[1]/div[1]/div[2]/div[5]/div[2]/div/div/span[1]")
    responsibility = tree.xpath("/html/body/div[2]/div/div[2]/div/div[1]/div[1]/div[2]/div[7]/div[2]/div")
    business_trip = tree.xpath("/html/body/div[2]/div/div[2]/div/div[1]/div[1]/div[2]/div[8]/div[2]/div")
    worktime = tree.xpath("/html/body/div[2]/div/div[2]/div/div[1]/div[1]/div[2]/div[9]/div[2]/div")
    weekend = tree.xpath("/html/body/div[2]/div/div[2]/div/div[1]/div[1]/div[2]/div[10]/div[2]/div")
    registration_date = tree.xpath("/html/body/div[2]/div/div[2]/div/div[1]/div[1]/div[2]/div[11]/div[2]/div")
    people_needed = tree.xpath("/html/body/div[2]/div/div[2]/div/div[1]/div[1]/div[2]/div[12]/div[2]/div")
    
    
    data_dict["職務名稱"] = title[0].text
    #data_dict["公司名稱"] = company[0].text #上面好像有了
    data_dict["工作內容"] = work[0].text
    data_dict["職務類別"] = list2string(title_category)
    data_dict["工作待遇"] = salary[0].text
    data_dict["工作性質"] = work_nature[0].text
    data_dict["工作地點"] = location[0].text
    data_dict["管理責任"] = responsibility[0].text
    data_dict["出差外派"] = business_trip[0].text
    data_dict["上班時段"] = worktime[0].text
    data_dict["休假時段"] = weekend[0].text
    data_dict["可上班日"] = registration_date[0].text
    data_dict["需求人數"] = people_needed[0].text
    
    #條件要求
    work_exp = tree.xpath("/html/body/div[2]/div/div[2]/div/div[1]/div[2]/div[2]/div[1]/div[2]/div")
    degree = tree.xpath("/html/body/div[2]/div/div[2]/div/div[1]/div[2]/div[2]/div[2]/div[2]/div")
    major = tree.xpath("/html/body/div[2]/div/div[2]/div/div[1]/div[2]/div[2]/div[3]/div[2]/div")
    language = tree.xpath("/html/body/div[2]/div/div[2]/div/div[1]/div[2]/div[2]/div[4]/div[2]/div/p")
    if not language[0].text: #代表並非"不拘"
        language_set = []
        language_set_e = tree.xpath("/html/body/div[2]/div/div[2]/div/div[1]/div[2]/div[2]/div[4]/div[2]/div//*/a/u")
        for n in language_set_e:
            language_set.append(n.text)
    else:
        language_set = "不拘"
    
    skillset = []
    skillset_e = tree.xpath("/html/body/div[2]/div/div[2]/div/div[1]/div[2]/div[2]/div[5]/div[2]/div//*/a/u")
    for index,n in enumerate(skillset_e):
        if n.text:
            skillset.append(n.text.replace("\u200b", ""))
    work_skill = []
    work_skill_e = tree.xpath("/html/body/div[2]/div/div[2]/div/div[1]/div[2]/div[2]/div[6]/div[2]/div//*/a/u")
    for index, n in enumerate(work_skill_e):
        if n.text:
            work_skill.append(n.text)
    other_requirements = tree.xpath("/html/body/div[2]/div/div[2]/div/div[1]/div[2]/div[3]/div/div[2]/div/div/p")

    data_dict["工作經歷"] = work_exp[0].text
    data_dict["學歷要求"] = degree[0].text
    data_dict["科系要求"] = major[0].text
    data_dict["語文條件"] = list2string(language_set)
    data_dict["擅長工具"] = list2string(skillset)
    data_dict["工作技能"] = list2string(work_skill)
    data_dict["其他條件"] = other_requirements[0].text
    
    #福利相關
    benefit_intro = tree.xpath("/html/body/div[2]/div/div[2]/div/div[1]/div[4]/div[2]/div/p")#div2
    legal_benefit = []
    legal_benefit_e = tree.xpath("/html/body/div[2]/div/div[2]/div/div[1]/div[4]/div[3]/div//*/a")#div3
    for index, n in enumerate(legal_benefit_e):
        legal_benefit.append(n.text)
    other_benefit = []
    other_benefit_e = tree.xpath("/html/body/div[2]/div/div[2]/div/div[1]/div[4]/div[5]/div//*/a")#div5
    for index, n in enumerate(other_benefit_e):
        other_benefit.append(n.text)
    recruit_incentives = tree.xpath("/html/body/div[2]/div/div[2]/div/div[1]/div[4]/div[6]/div/p")#div6
    
    if benefit_intro:
        data_dict["福利介紹"] = benefit_intro[0].text
    data_dict["法定福利"] = list2string(legal_benefit)
    data_dict["其他福利"] = list2string(other_benefit)
    if recruit_incentives:
        data_dict["招募福利"] = recruit_incentives[0].text
        
    return data_dict

#爬取所有頁面的資料
data = []
for i in range(jobs.shape[0]):
    company = jobs["公司名稱"].iloc[i]
    job = jobs["職缺名稱"].iloc[i]
    url = jobs["職缺連結"].iloc[i]
    dict_data_jobs = {
        "公司名稱" : company,
        "職缺名稱" : job,
        "職缺連結" : url
    }
    try:
        job_data = get_data(url)
        job_data = {**dict_data_jobs, **job_data}
        data.append(job_data)
        print(i)
    except:
        continue
    if i ==20:
        break

df = pd.DataFrame(columns = data[0].keys(), data = data)
path = r"測試.xlsx"
df.to_excel(path, index = False)