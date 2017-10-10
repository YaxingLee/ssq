import sys,os,datetime
import requests
from bs4 import BeautifulSoup
import re
from get_OnePage import get_Together
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
    #return all_Page_list
    list_SSQ = []
    for i in all_Page_list:
        onePage = get_Together(i)
        for o in onePage:
            list_SSQ.append(o)
    return list_SSQ,all_Se
def write_To_File():
    list_SSQ,all_Se = link_pages()
    pickle.dump(list_SSQ,open(r'ssq.pk','wb'))