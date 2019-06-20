import webbrowser
import requests
import mechanicalsoup
import lxml.html as lh
import pandas as pd

import xlsxwriter
workbook = xlsxwriter.Workbook('EC_2019.xlsx')
worksheet = workbook.add_worksheet()
row=1


def scrape(url,j):
    global row
    count=1
    res=requests.get(url)
    if j<10:
        j="00"+str(j)
    elif j<100:
       j="0"+str(j)
    #change branch / usn here
    usn="1RV18EC"+str(j)


    browser=mechanicalsoup.StatefulBrowser()
    browser.open(url)
    browser.select_form()
    browser["usn"]=usn




    browser["captcha"]='10'
    
    browser.submit_selected()


    string=browser.get_current_page()
    string1=str(browser.get_current_page())
    #print(string)
    
    if "SGPA" in string1:
        col=0
        l1=[]
        th=string1.find("<td ")+4
        string2=string1
        string2=string2.replace('<b>','')
        
        while th !=3:
            string2 =string2[th:]            
            th1=string2
            
            th1=th1[th1.find(">")+1:]
            #print(string2)
            th1=th1[0:th1.find("<")]
            #print(th1)
            l1.append(th1)
            th=string2.find("<td ")+4
        print(l1)
        
        for x in l1:
            worksheet.write_string(row,col,x)
            col+=1
        row+=1    
        
        
        


        
        count+=1
        #l.append(l1)
            

        return True





url='http://results.rvce.edu.in'

for j in range(0,200):
    for i in range(50):        
        if scrape(url, j)==True:
            break
print("COMPLETEEEEEEEEE")
workbook.close()

