from lxml import html
import requests, bs4,re,os

company = 'samsung'
page = requests.get('http://www.geeksforgeeks.org/tag/'+company+'/')
tree = bs4.BeautifulSoup(page.text, "lxml")
os.chdir(os.getcwd())
if not os.path.exists(company):
    os.makedirs(company)
    #print 'made folder'
os.chdir(os.path.join(os.getcwd(),company))
print os.getcwd()
flag = 0
while flag==0:
    flag = 1
    list = tree.select('.entry-title')
    for item in list:
        address = item.select('a')
        addr = address[0]['href']
        data_page = requests.get(addr)
        data_tree = bs4.BeautifulSoup(data_page.text,"lxml")
        title = data_tree.select('.entry-title')
        cleanr = re.compile('<.*?>')
        cleantexttitle = re.sub(cleanr,'' , title[0].text)
        #print cleantexttitle
        data = data_tree.select('.entry-content')
        cleantextbody = re.sub(cleanr,'' , data[0].text)
        #print cleantextbody
        #print os.getcwd()
        #print os.getcwd()
        file = open(cleantexttitle+'.txt','w')
        file.write(cleantextbody.encode('utf-8'))
        file.close()
    next_page_navi = tree.select('.wp-pagenavi')
    #print next_page_navi
    flag = 1
    next_pages = next_page_navi[0].select('a')
    for further in next_pages:
        
        if len(further['class']) == 2 and further['class'][1] == 'larger':
            flag = 0
            page = requests.get(further['href'])
            tree = bs4.BeautifulSoup(page.text,"lxml")
            break
            

    
