import webbrowser
import requests
import mechanicalsoup
import lxml.html as lh
import pandas as pd

def scrape(url,j):
    count=1
    res=requests.get(url)
    if j<10:
        j="00"+str(j)
    elif j<100:
       j="0"+str(j)
    #change branch / usn here
    usn="1RV16EC"+str(j)
##    print(usn)
##    print(res.text)

    browser=mechanicalsoup.StatefulBrowser()
    browser.open(url)
    browser.select_form()
    browser["usn"]=usn




    browser["captcha"]='10'
    
    browser.submit_selected()
    #print(res.text)
    #browser["captcha"]=str(sum)
    #browser.launch_browser()

    string=browser.get_current_page()
    string1=str(browser.get_current_page())
    #print(string)
    
    if "SGPA" in string1:
        #browser.launch_browser()
    
        usn=string1.find("data-title=\"USN")+20
        name=string1.find("data-title=\"NAME")+21
        sgpa=string1.find("data-title=\"SGPA")+21
        #branch=
        #sem=

        
        #print(usn)
        usn1=string1[usn:]
        #print(usn1)
        usn1=usn1[0:usn1.find("<")]

        name1=string1[name:]
        name1=name1[0:name1.find("<")]

        sgpa1=string1[sgpa:]
        sgpa1=sgpa1[0:sgpa1.find("<")]
        if float(sgpa1)>-1:
            count+=1
            print(str(usn1),str(name1),str(sgpa1))
            
            #print(count)

        #input("Press any key to continue")
        return True





url='http://results.rvce.edu.in'

for j in range(0,220):
    for i in range(50):
        if scrape(url, j)==True:
            break
