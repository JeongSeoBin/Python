#!/usr/bin/env python
# coding: utf-8

# In[2]:


# 오름차순 정렬 함수
def selectionSortAsc(data):
    for i in range(0, len(data) - 1, 1):
        for j in range(i + 1, len(data), 1):
            if data[i] > data[j]:
                data[i], data[j] = data[j], data[i]
    return data

# 내림차순 정렬 함수
def selectionSortDesc(data):
    for i in range(0, len(data) - 1, 1):
        for j in range(i + 1, len(data), 1):
            if data[i] < data[j]:
                data[i], data[j] = data[j], data[i]
    return data


# In[3]:


for i in range(0, 4, 1):
    for j in range(i + 1, 5, 1):
        print('i = {}, j = {}'.format(i, j))
    # ========================== j
    print('*' * 30)
    # ====================== i
        
data = [8, 3, 4, 9, 1]
for i in range(0, 4, 1):
    for j in range(i + 1, 5, 1):
        # data 리스트의 i 번째 데이터와 j 번째 데이터를 비교해서 i 번째 데이터가 크면 두 
        # 데이터를 교환한다. => 앞에 위치한 데이터가 크면 교환한다. 
        # => 큰 데이터가 뒤로간다. => 오름차순
        # 부등호를 '<'로 변경하면 내림차순으로 정렬된다.
        if data[i] > data[j]:
            # temp = data[i]
            # data[i] = data[j]
            # data[j] = temp
            data[i], data[j] = data[j], data[i]
        # ======================== if
    # ======================== for j => 회전종료
    print('{}회전 결과 : {}'.format(i + 1, data))
    # ======================== for i => 정렬종료
print('정렬 결과 : {}'.format(data))
        
data = [8, 3, 4, 9, 1]
data = selectionSortAsc(data)
print(data)
data = selectionSortDesc(data)
print(data)


# In[4]:


get_ipython().system(' jupyter nbconvert --to script selectionSortModule1.ipynb')

