#!/usr/bin/env python
# coding: utf-8

# # LawTech_HW1_08141217

# 繳交檔名：LawTech_HW1_學號

# #### 一、字串處理

# 請用「空白鍵」當作切割符，對 `test1`變數做切割，並將Zombie、boys、Vampire這幾個單詞抓出來，使用字串格式化的方式產生下面的句子

# Oh! boys, please don't fear Zombie and Vampire.

# In[52]:


test1 = "Zombie stories are life lessons for boys who don't mind thinking about bodies, but can't cope with emotions. Vampire stories are in many ways sex for the squeamish."


# In[53]:


test1=test1.split(' ')


# In[54]:


test1[18]


# In[57]:


print(f"Oh!{test1[6]},please don't fear {test1[0]} and {test1[18]}")


# #### 二、Index索引練習
# 
# 請將 List 中的數字抓出，並算出總合為多少

# In[31]:


List = [23, 'red', 3, ['15', 'apple', [3, '3.5']], '27', [90, 'fight']]


# In[60]:


List[0]+List[2]+List[3][2][0]+List[5][0]+eval(List[3][0])+eval(List[3][2][1])+eval(List[4])


# #### 三、資料存取練習

# 請設計一個資料結構（dict of list），來儲存以下數據
# 
# 
# Jay--M--170
# 
# Bill--M--189
# 
# Alice--F--160
# 
# May--F--158
# 
# Max--M--185
# 
# Ann--F--148
# 
# Dabby--F--150
# 
# Steve--M--180
# 
# Jet--M--173
# 
# Amy--F--156
# 
# 並計算這10人的身高平均

# `sum()`：合計function
# 

# In[65]:


dict1 = {'Jay':['M',170], 'Bill':['M',189], 'Alice':['F',160], 'May':['F',158], 'Max':['M',185], 'Ann':['F',148], 'Dabby':['F',150], 'Steve':['M',180],'Jet':['M',173], 'Amy':['F',156]}


# In[80]:


(dict1['Jay'][1]+dict1['Bill'][1]+dict1['Alice'][1]+dict1['May'][1]+dict1['Max'][1]+dict1['Ann'][1]+dict1['Dabby'][1]+dict1['Steve'][1]+dict1['Jet'][1]+dict1['Amy'][1])/len(dict1.keys())

