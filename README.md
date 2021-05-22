# EnterpriseChecks
 LINKEDIN AND IPV4 SCRAPPING

# ATENTION!
Every time is scraping the window has to be in an active window if it is on seconds windows may not work.

Created by:NataliaSTH

# STEPS

1.First of all install the requirements.txt and configure the venv with a python interpreter

```
pip install -r requirements.txt
```


2.Download chromedriver and write the path on main.py line 46.

```
driver = webdriver.Chrome('pathwhereisdownloaded/chromedriver')
```

    Version ChromeDriver 89.0.4389.23 

    link download:https://chromedriver.chromium.org/downloads`
    
3.Configure Keys.py by 
```
linkedin_username="your-linkedin-mail"
lnkdn_pwd="linkedin-password"
```

How it works:

    ███████╗███╗░░██╗████████╗███████╗██████╗░██████╗░██████╗░██╗░██████╗███████╗
    ██╔════╝████╗░██║╚══██╔══╝██╔════╝██╔══██╗██╔══██╗██╔══██╗██║██╔════╝██╔════╝
    █████╗░░██╔██╗██║░░░██║░░░█████╗░░██████╔╝██████╔╝██████╔╝██║╚█████╗░█████╗░░
    ██╔══╝░░██║╚████║░░░██║░░░██╔══╝░░██╔══██╗██╔═══╝░██╔══██╗██║░╚═══██╗██╔══╝░░
    ███████╗██║░╚███║░░░██║░░░███████╗██║░░██║██║░░░░░██║░░██║██║██████╔╝███████╗
    ╚══════╝╚═╝░░╚══╝░░░╚═╝░░░╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚═╝╚═════╝░╚══════╝

    ░█████╗░██╗░░██╗███████╗░█████╗░██╗░░██╗
    ██╔══██╗██║░░██║██╔════╝██╔══██╗██║░██╔╝
    ██║░░╚═╝███████║█████╗░░██║░░╚═╝█████═╝░
    ██║░░██╗██╔══██║██╔══╝░░██║░░██╗██╔═██╗░
    ╚█████╔╝██║░░██║███████╗╚█████╔╝██║░╚██╗
    ░╚════╝░╚═╝░░╚═╝╚══════╝░╚════╝░╚═╝░░╚═╝


                        
ENTER THE NAME OF THE ENTERPRISE?

enterprise name

-----------------OPTIONS MENU-------------------

PRESS 1 TO SEARCH PEOPLE THAT WORK IN THE GIVEN ENTERPRISE

PRESS 2 TO SEARCH FOR DOMAINS AND ASN RELATED INFORMATION

select 1 or 2 

Option 1:
If you select option 1 , the program prints all the people that works on the selected enteprise. After finishing the first execution it will ask if you want to print another page.
If selection is no,will ask if you want to save all the information printed on a txt.
If yes it will create the txt 
If no exit

Option 2:
Scraping from ipv4 info the scraping will show all the domains,ASN,description,enterprise..
It will also ask to save it on a txt or exit

