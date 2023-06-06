import pandas as pd
import jieba
import os
from collections import Counter
# 讀取 Excel 檔案
df = pd.read_excel('group8_python_class/104爬蟲專案/job_content.xlsx')

# 停用詞檔案所在的資料夾路徑
folder_path = 'group8_python_class\\104爬蟲專案\\stopword'

# 創建一個空集合用於存放停用詞
stopwords = set()
# 斷詞結果列表
words_list = []
# 遍歷資料夾中的檔案
for filename in os.listdir(folder_path):
    file_path = os.path.join(folder_path, filename)
    
    # 讀取每個檔案的停用詞並加入到集合中
    with open(file_path, 'r', encoding='utf-8') as f:
        for word in f:
            stopwords.add(word.strip())
# 創建新的 DataFrame 儲存切詞結果
new_df = pd.DataFrame(columns=['斷詞結果'])
# 將每一行的資料進行斷詞
for index, row in df.iterrows():
    text = row['工作內容']  # 假設你的資料位於特定欄位，需替換為實際的欄位名稱
    
    # 斷詞並過濾停用詞
    words = jieba.cut(text)
    filtered_words = [word.strip() for word in words if word.strip() not in stopwords and word.strip() != ''and word.strip() != '●'and word.strip() != '▍ ']
    # 將切詞結果添加到新的 DataFrame 中
    new_df.loc[index] = [' '.join(filtered_words)]
    
    # 處理斷詞結果，例如存儲到新的資料結構或進行其他操作
    print(filtered_words)

    # 將切詞結果添加到詞列表中
    words_list.extend(filtered_words)

    # 寫入新的 Excel 檔案
    new_df.to_excel('斷詞結果.xlsx', index=False)

# 計算詞頻
word_counts = Counter(words_list)
# 將詞頻結果存儲到 txt 檔案
with open('詞頻結果.txt', 'w', encoding='utf-8') as f:
    for word, count in word_counts.items():
        f.write(f'{word}: {count}\n')