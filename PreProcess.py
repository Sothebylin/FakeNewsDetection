import pandas as pd

df = pd.read_csv("虚假新闻检测/train/train.csv")

#rows_with_missing_values = df[df.isnull().any(axis=1)]
# 显示包含缺失值的行,1708 and 6995 Official Account Name 缺失
#print("包含缺失值的行：")
#print(rows_with_missing_values)

df = df.dropna()

# 查看 'label' 列
#print(df['label'].value_counts())

#------------------------------
#对offical account name进行分析
#account_news = df['Ofiicial Account Name'].value_counts()
# 统计每个官方账号的发布假新闻次数 (label = 1)
#fake_news_by_account = df[df['label'] == 1]['Ofiicial Account Name'].value_counts()
# 统计每个官方账号的发布真新闻次数 (label = 0)
#true_news_by_account = df[df['label'] == 0]['Ofiicial Account Name'].value_counts()
# 计算每个官方账号的假新闻比例
#fake_news_ratio_by_account = fake_news_by_account / account_news
#fake_news_ratio_by_account.sort_values(ascending=False).to_csv("各官方账号的假新闻比例.csv", header=True, index=True)

