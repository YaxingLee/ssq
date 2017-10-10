""" 
first, get all pages and all Serial No.;
second,get all date on one page;( return list List_ssq )
third, sort date on one page;
forth, link all date on every pages,save date in d:\ssq directory;
fifth, check date every time when run;
list like [[ ... ]]
"""
import sys,os,datetime
import requests
from bs4 import BeautifulSoup
import re,pickle
os.chdir(r'd:\ssq')
def get_No_Onepage(pages):
    url="http://kaijiang.zhcw.com/zhcw/html/ssq/list_%d.html" % pages
    print "[+] getting %d page information..." %pages
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
    List_ssq = seq_List(List_temp_ssq)
    return List_ssq
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
def seq_List(ListA):                                     
    for m in range(len(ListA)-1):                        
        for i in range(1,len(ListA)):                    
            if ListA[i][0] < ListA[i-1][0]:              
                ListA[i-1],ListA[i] = ListA[i],ListA[i-1]
    return ListA                                         
def get_history():
    url = "http://kaijiang.zhcw.com/zhcw/html/ssq/list.html"
    beautyText = BeautifulSoup(requests.get(url).text, "html.parser")
    be = beautyText.find(class_='pg')
    No_Pages = be.strong.string
    No_Se = be.strong.next_sibling.next_sibling.string
    #No_Pages is the Nombers of Pages;No_Se is all Se No.
    return No_Pages,No_Se
def link_pages():
    all_Pages_temp,all_Se_temp = get_history()
    all_Pages = int(all_Pages_temp)
    all_Se = int(all_Se_temp)
    all_Page_list = [ i for i in range(1,all_Pages+1) ]
    all_Page_list.reverse()
    #return all_Page_list
    list_SSQ = []
    for i in all_Page_list:
        onePage = get_No_Onepage(i)
        for o in onePage:
            list_SSQ.append(o)
    return list_SSQ,all_Se
def write_To_File():
    list_SSQ,all_Se = link_pages()
    pickle.dump(list_SSQ,open(r'ssq.pk','wb'))
def get_Last_Se():
    url = "http://kaijiang.zhcw.com/zhcw/html/ssq/list.html"
    beautyText = BeautifulSoup(requests.get(url).text, "html.parser")
    Last_Se = beautyText.find(align="center",text=re.compile(r'\d{7}')).string
    return Last_Se
def check_In():
    print "Checking ... "
    Last_Se = get_Last_Se()
    geted_List = pickle.load(open(r'ssq.pk','r'))
    geted_Se = geted_List[len(geted_List)-1][0]
    if Last_Se == geted_Se:
        print "All information is updated , enjoy !"
    else:
        print "You need update your datebase!!!"