import pandas as pd
from selenium import webdriver   #導入瀏覽器
from selenium.webdriver.common.by import By  #選取瀏覽器
import time
# 读取Excel文件中的特定工作表
data = pd.read_excel('group8_python_class\\104爬蟲專案\\商業分析師.xlsx', sheet_name='Sheet1')


# 选择特定列
column_c_data = data['職缺連結']


driver=webdriver.Chrome('group8_python_class\104爬蟲專案\chromebriver\chromedriver.exe')

# 循环遍历每个链接
for link in column_c_data:
    # 在浏览器中打开链接
    driver.get(link)

    # element = driver.find_element(By.CLASS_NAME,'t3.mb-0')
    # # 获取元素文本
    # text1 = element.text
    time.sleep(5)
    # 使用class name定位所有目标元素
    elements = driver.find_elements(By.CLASS_NAME,'t3.mb-0')
    print('------st')
    # 遍历每个元素并打印文本内容
    for element in elements:
        text1 = element.text
        print('---------------------------')
        print(text1)
        print('---------------------------')
    print('------end')




    # 添加适当的延迟时间，以确保页面加载完成
    time.sleep(5)  # 2秒延迟


#driver.quit()




