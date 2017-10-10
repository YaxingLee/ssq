from get_PagesTogether import link_pages
from get_PagesTogether import get_history
import os,re,requests
from bs4 import BeautifulSoup
import pickle
os.chdir(r'd:\ssq')
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
        print "updating..."
        os.remove(r'ssq.pk')
        write_To_File()
        print "Updated."
if __name__ == '__main__':
    check_In()