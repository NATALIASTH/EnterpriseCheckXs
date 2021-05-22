import sys

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
import Keys as Key


def ipv4scrap(str):
    header = {"User-Agent": "Mozilla/5.0 (X11; U; Linux i686) Gecko/20071127 Firefox/2.0.0.11"}

    driver.get('http://ipv4info.com/')
    driver.find_element_by_class_name("ti_form_text")
    driver.maximize_window()
    driver.find_element_by_class_name("ti_form_text").send_keys(str)
    driver.find_element_by_class_name("ti_form_button").send_keys(Keys.ENTER)

    url = driver.current_url

    table = driver.find_element_by_class_name("TB2")

    aux = table.find_elements_by_tag_name('tr')[2:]
    for i in aux:
        print(i.text + '\n')

    txt = input("do you want to save it on a .txt yes/no")
    if txt == 'yes':
        f=open("ipv4.txt", "w")
        for i in aux:
            f.write(i.text)
            f.write('\n')


    print("done")
    main()

    time.sleep(3)

    time.sleep(3)

#path where is the chromedriver
driver = webdriver.Chrome('/Users/piopio/Desktop/chromedriver')
driver.maximize_window()


def linkedin_login():
    driver.get('https://www.linkedin.com/login/')
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID, "username"))).send_keys(Key.linkedin_username)
    driver.find_element_by_id("password").send_keys(Key.lnkdn_pwd)
    driver.find_element_by_class_name("login__form_action_container ").click()
    print(driver.current_url)
    if driver.current_url != "https://www.linkedin.com/feed/":
        driver.get('https://www.linkedin.com/feed/')
        print("olé")
        print(driver.current_url)

    else:
        print("olo")


def find_onSearcher(str):
    driver.find_element_by_class_name("search-global-typeahead__input").send_keys(str)
    driver.find_element_by_class_name("search-global-typeahead__input").send_keys(Keys.ENTER)
    time.sleep(3)
    if not "Personas" in driver.find_elements_by_class_name("mr2")[1].text:
        driver.find_elements_by_class_name("mr2")[0].click()
    else:
        driver.find_elements_by_class_name("mr2")[1].click()
    time.sleep(3)
    i = 1
    nextpage = "Y"
    cont=0;
    auxtxt = []
    while nextpage == "Y":
        time.sleep(3)
        personas = driver.find_elements_by_class_name("reusable-search__result-container")
        print(len(auxtxt))
        for persona in personas:
            personaje = []
            print("register number: ", i)
            nombre = persona.find_elements_by_class_name("app-aware-link")[1].text
            nombre = nombre.split('\n')[0]
            print("Name: ", nombre)
            enlace = persona.find_elements_by_class_name("app-aware-link")[1].get_attribute("href")
            print("Link: ", enlace)
            puesto = persona.find_element_by_class_name("entity-result__primary-subtitle").text
            print("Roll: ", puesto)
            print("________________________")
            personaje.append(nombre)
            personaje.append(enlace)
            personaje.append(puesto)
            auxtxt.append(personaje)
            i = i + 1

        #opcion de no ampliar
        nextpage = input("+ pages? Y / N")
        if nextpage == 'N':
            n = 1
            txt = input("do you want to save it on a .txt yes/no  no=menu:  ")
            if txt == 'yes':
                f = open("Linkedin.txt", "w")
                for varaux in auxtxt:
                    f.write("Name: ")
                    f.write(varaux[0])
                    f.write('\n')
                    f.write("Link:")
                    f.write(varaux[1])
                    f.write('\n')
                    f.write("Roll: ")
                    f.write(varaux[2])
                    f.write('\n')
                    f.write("________________________")
                    f.write('\n')
                    print('ha entrado')
                    n = n + 1


            else:
                main()
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1)
        driver.find_element_by_class_name("artdeco-pagination__button--next").click()


def main():
    print("""\


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


                        """)
    str = ""
    str = input('ENTER THE NAME OF THE ENTERPRISE?' '\n')
    option = input('-----------------OPTIONS MENU-------------------' '\n'
                   'PRESS 1 TO SEARCH PEOPLE THAT WORK IN THE GIVEN ENTERPRISE'
                   '\n'
                   'PRESS 2 TO SEARCH FOR DOMAINS AND ASN RELATED INFORMATION' '\n')
    print(option)

    if option == '1':
        linkedin_login()
        find_onSearcher(str)

    elif option == '2':
        ipv4scrap(str)
    elif option == 'exit':
        exit()

    else:
        print("INVALID INFORMATION, TRY AGAIN")
        main()


main()

