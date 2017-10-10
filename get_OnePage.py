import sys,os,datetime
import requests
from bs4 import BeautifulSoup
import re,pickle
def get_Onepage(page):
    url="http://kaijiang.zhcw.com/zhcw/html/ssq/list_%d.html" % page
    print "[+] getting %d page information..." %page
    get_Web=requests.get(url)
    soup=BeautifulSoup(get_Web.text,"html.parser")
    # date and serial No.
    tagList=[]
    for i in soup.find_all(align="center",text=re.compile(r'\d{4}')):
        tagList.append(i.string)
    # all Numbers. 6 Red Number. and 1 Blue Number.
    allemList=[]
    for allem in soup.find_all('em'):
        allemList.append(allem.string)
    #List format for No. and date
    #DicTag=[[Ns,Date,R1,R2,R3,R4,R5,R6,B],[]]
    temp_Da_List=[]
    temp_No_List=[]
    for i in range(0,len(tagList)/2):
        temp_b_List=[]
        temp_a_List=[tagList[i*2+1],tagList[i*2]]
        for q in temp_a_List:
            temp_b_List.append(q)
        temp_Da_List.append(temp_b_List)
    #print temp_Da_List
    for o in range(0,len(allemList)/7):
        temp_c_List = []
        for p in range(7):
            temp_c_List.append(allemList[o*7+p])
        temp_No_List.append(temp_c_List)
    List_temp_ssq=get_Together(temp_Da_List,temp_No_List)
#    List_ssq = seq_List(List_temp_ssq)
    return List_temp_ssq
def get_Together(Lista,Listb):
    List_ssq=[]
    if len(Lista)==len(Listb):
        for a in range(len(Lista)):
            List_s = []
            for b in Lista[a]:
                List_s.append(b)
            for c in Listb[a]:
                List_s.append(c)
            List_ssq.append(List_s)
        return List_ssq
    else:
        print "error:two list has different lenght!!!"