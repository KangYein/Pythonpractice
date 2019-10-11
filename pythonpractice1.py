#!/usr/bin/env python
# coding: utf-8

# In[2]:


print("파이썬")


# In[3]:


print("바보")


# In[4]:


a=(2,2)
len(a)


# In[5]:


print("끝")


# In[7]:


food1=input('첫번째 주문하실 음식은 무엇인가요?:')
food2=input('두번째 주문하실 음식은 무엇인가요?:')
print('첫번째 주문하신 음식은 %s 두번째 주문하신 음식은 %s 입니다.' %(food1,food2))


# In[16]:


foodmenu1=input('''
1.짜장면   2울면   3.짬뽕   4.깐풍기   5.칠리새우

1.위 메뉴 중 주문할 메뉴의 번호를 입력하세요:''')
foodmenu2=input('2.위 메뉴의 주문 수량을 입력하세요:')
print('메뉴 번호는 %s 이고 주문 수량은 %s 개 입니다.' %(foodmenu1,foodmenu2))


# In[17]:


5/3


# In[18]:


5//3


# In[19]:


no1 = int( input("첫번째 숫자 입력:"))
no2 = int( input("첫번째 숫자 입력:"))
print(no1+no2)


# In[21]:


no1 = float( input("첫번째 숫자 입력:"))
no2 = float( input("첫번째 숫자 입력:"))
print(no1+no2)


# In[44]:


a=[1, 3, 5, 4, 2]
a.reverse()
a


# In[46]:


a=[1, 3, 5, 4, 2]
a.sort()
a


# In[48]:


a=int(input("숫자를 입력하세요:"))
if a%3==0:
    print(a**2)
else:
    print(0)


# In[61]:


fruits=input("사과,감,귤 중에 어떤 과일 좋아하세요?:")
if fruits=='사과':
    print("Good~")
elif fruits=='감':
    print("Very Good~")
elif fruits=='귤':
    print("So So....")
else:
    print("사과나 감,귤 중에 하나를 입력하세요~~")
    


# In[62]:


fruits=input("사과,감,귤,복숭아 중에 어떤 과일 좋아하세요?:")
if fruits=='사과'or fruits=='감':
    print("Very Good~")
elif fruits=='귤'or fruits=='복숭아':
    print("Good~")
else:
    print("사과나 감,귤,복숭아 중에 하나를 입력하세요~~")


# In[63]:


menu = int(input('''
1.짜장면 - 5,000원          2.짬뽕 - 6,000원
3.군만두 - 8,000원          4.탕수육 - 10,000원 

1. 위 메뉴 중 주문할 메뉴의 번호를 쓰세요:  ''') )

qty = int(input("2. 위 메뉴의 주문 수량을 쓰세요: "))
print("\n")

if (menu == 1):
    print( '주문하신 메뉴는 짜장면이고 주문 수량은 %s 그릇이며 주문금액은 %s 입니다' %(qty , 5000*qty))
elif ( menu == 2) :
    print( '주문하신 메뉴는 짬뽕이고 주문 수량은 %s 그릇이며 주문금액은 %s 입니다' %(qty , 6000*qty))
elif ( menu == 3 ) :
    print( '주문하신 메뉴는 군만두이고 주문 수량은 %s 그릇이며 주문금액은 %s 입니다' %(qty , 8000*qty))
elif ( menu == 4) :
    print( '주문하신 메뉴는 탕수육이고 주문 수량은 %s 그릇이며 주문금액은 %s 입니다' %(qty , 10000*qty))
else :
    print('메뉴선택을 잘못하셨습니다')


# In[66]:


num=int(input("출력을 원하는 구구단을 입력하세요:"))
for i in range(1,10):
    print("%d x %d = %d" %(num,i,num*i))


# In[ ]:


while True:
    menu =int(input('''
    1.짜장면-5000원    2.짬뽕-6000원
    3.군만두-8000원    4.탕수육-10,000원

    1.위 메뉴 중 주문할 메뉴의 번호를 쓰세요:'''))
    num=int(input("2.위 메뉴의 주문수량을 쓰세요:"))
    a=input("추가 주문을 하시겠습니까?:")
    if menu==1:
        menu='짜장면'
        price=5000
    elif menu == 2:
        menu='짬뽕'
        price=6000
    elif menu == 3:
        menu='군만두'
        price=8000
    elif menu == 4:
        menu='탕수육'
        price=10000
    if a=='y' or a=='Y':
        print("주문메뉴는 %s이고 주문수량은 %d 그릇이며 주문금액은 %d 입니다." %(menu,num,num*price))
        continue
    elif a=='n' or a=='N':
        break


# In[ ]:


def a(x,y):
    if x>y:
        print(x-y)
    else:
        print(y-x)
print(a(3,4))


# In[1]:


answer = 'Y'
while ( answer=="Y" or answer == "y") :
    menu = int(input('''
    1.짜장면 - 5,000원          2.짬뽕 - 6,000원
    3.군만두 - 8,000원          4.탕수육 - 10,000원 

    1. 위 메뉴 중 주문할 메뉴의 번호를 쓰세요:  ''') )

    qty = int(input("    2. 위 메뉴의 주문 수량을 쓰세요: "))
    print("\n")
    
    if (menu == 1):
        print( '    주문하신 메뉴는 짜장면이고 주문 수량은 %s 그릇이며 주문금액은 %s 입니다' %(qty , 5000*qty))
    elif ( menu == 2) :
        print( '    주문하신 메뉴는 짬뽕이고 주문 수량은 %s 그릇이며 주문금액은 %s 입니다' %(qty , 6000*qty))
    elif ( menu == 3 ) :
        print( '    주문하신 메뉴는 군만두이고 주문 수량은 %s 그릇이며 주문금액은 %s 입니다' %(qty , 8000*qty))
    elif ( menu == 4) :
        print( '    주문하신 메뉴는 탕수육이고 주문 수량은 %s 그릇이며 주문금액은 %s 입니다' %(qty , 10000*qty))
    else :
        print('    메뉴선택을 잘못하셨습니다')
    print("\n")
    
    answer = input("    3.추가 주문을 하시겠습니까? (Y / N) : ")


# In[26]:


#표 9데이터 프레임) 만들기
import pandas as pd
no=[]
subject_name=[]

no.append(1)
no.append(2)
no.append(3)

subject_name.append('수학')
subject_name.append('과학')
subject_name.append('빅데이터')

subject =pd.DataFrame()
subject['과목번호']=no
subject['과목명']=subject_name
print(subject)

#csv 형식으로 저장하기
subject.to_csv("C:\py_temp\\subject.csv",encoding="utf-8-sig",index=False)
#xls 형식으로 저장하기
subject.to_excel("C:\py_temp\\subject.xls",index=False)

