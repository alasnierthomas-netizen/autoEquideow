import sys
import privateInfo
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from choix_du_concours import choix_du_concours
from time import sleep
from selenium.common.exceptions import StaleElementReferenceException

from selenium.webdriver.chrome.options import Options
chrome_options = Options()

driver = webdriver.Edge(options=chrome_options)



def attente_implicite(texte: str):
    kill = 0
    while True:
        try:
            return driver.find_element(By.CSS_SELECTOR, texte)
        except:
            sleep(0.01)
            kill += 1
            if kill > 1000:
                sys.exit()

def tentative_clique(texte: str):
    kill = 0
    boucle = True
    while boucle:
        try:
            return driver.find_element(By.CSS_SELECTOR, texte).click()
        except:
            sleep(0.01)
            kill += 1
            if kill > 100:
                boucle = False


def clique_implicite(texte: str, selector = By.CSS_SELECTOR):
    kill = 0
    while True:
        try:
            driver.find_element(selector, texte).click()
            break
        except:
            sleep(0.01)
            kill += 1
            if kill > 1000:
                sys.exit()



def texte_implicite(texte: str):
    kill = 0
    while True:
        try:
            return driver.find_element(By.CSS_SELECTOR, texte).text
            break
        except:
            sleep(0.01)
            kill += 1
            if kill > 1000:
                sys.exit()

driver.get("https://ouranos.equideow.com/")
url = driver.current_url
clique_implicite("button[id='onetrust-reject-all-handler']") # del the kookie pop up
sleep(0.2)
clique_implicite("span[class='btn__label__text']")

#rentre mes identifient puis se connécte
identifient = attente_implicite("input[placeholder='Identifiant']")
assert identifient != "", "merci de mentionner votre identifiant dans le fichier privateInfo.py"
identifient.send_keys(privateInfo.identifiant)
mdp = attente_implicite("input[placeholder='Mot de passe']")
assert mdp != "", "merci de mentionner votre mot de passe dans le fichier privateInfo.py"
mdp.send_keys(privateInfo.password)
clique_implicite("button[name='authentificationSubmit']")
while driver.current_url == url:
    pass
url = driver.current_url
#on vas au ranche pour récupérer le nombre de chevale
assert privateInfo.elevage != "https://ouranos.equideow.com/elevage/chevaux/?elevage=", "merci de mentionner le lien de votre élevage dans le fichier privateInfo.py"
driver.get(privateInfo.elevage)
clique_implicite( ".action.action-style-2")
nombre_cheveaux = int(texte_implicite( "strong.nowrap:not(.display-block)"))
print(nombre_cheveaux)
assert privateInfo.cheval != "https://ouranos.equideow.com/elevage/chevaux/cheval?id=", "merci de mentionner le lien d'un de vos chevaux dans le fichier privateInfo.py"
driver.get(privateInfo.cheval)
#on démare la boucle principale (une itération = un cheval)
for _ in range(nombre_cheveaux):
    #inscrit a une penssion
    try:
        if (attente_implicite("td[class='first top']").find_element(By.CSS_SELECTOR, "a[direction='rtl']").get_attribute("class") == "action action-style-4 competition-trot"):
            classiqueHorse = True
        else:
            classiqueHorse = False
        driver.find_element(By.CSS_SELECTOR, "span[style='background-image:url(//ouranos.equideow.com/media/equideo/image//components/action/2/centre.png);']").click()
        tentative_clique("button[class=ot-pc-refuse-all-handler]")
        driver.find_element(By.CSS_SELECTOR, "span[class='grid-table align-middle font-small']").find_element(By.XPATH, ".//a[text()='60 jours']").click()
        sleep(0.5)
        clique_implicite("img[alt='ce centre propose des abreuvoirs dans tous ses box']")
        clique_implicite("img[alt='ce centre propose des douches dans tous ses box']")
        if (classiqueHorse):
            clique_implicite("img[alt='specialisationclassique']")
        else:
            clique_implicite("img[alt='specialisationwestern']")
        driver.find_element(By.XPATH, "//span[text()='Rechercher']").click()
        driver.find_element(By.CSS_SELECTOR, "tr[class=' odd highlight']").find_element(By.XPATH, ".//strong[text()='1 200']").click()
    except:
        print("le cheval n'as pas besoin de Centre équestre")

    
    clique_implicite( "div[id='mission']")
    race_cheval = texte_implicite( "span.color-style-0")
    chemin_de_comp = choix_du_concours(race_cheval)
    page_avent = driver.current_url # c'est aussi la page principale de notre cheval
    boucle_de_comp = True
    while boucle_de_comp:
        html = driver.page_source
        clique_implicite( f"td.{chemin_de_comp}")
        try:
            pageCharger = False
            sleep(0.1)
            while (pageCharger) : # si la page a charger
                if(driver.page_source == html):
                    pageCharger = True
                else:
                    sleep(0.1)
                    html = driver.page_source
                
            driver.find_element(By.CSS_SELECTOR,"span.grid-cell.align-middle.spacer-right.spacer-small-left") # si pas trouver renvoi une éreure
            driver.get(page_avent)
            boucle_de_comp = False
        except:
            clique_implicite( "button[style='margin-top: 2px']")
    #prend la boufe
    clique_implicite( "a[id='boutonBoire']")
    sleep(0.2)
    clique_implicite( "a[id='boutonCaresser']")
    sleep(0.2)
    clique_implicite( "a[id='boutonPanser']")
    sleep(0.2)
    clique_implicite( "a[id='boutonCarotte']")
    sleep(0.2)
    clique_implicite( "a[id='boutonMash']")
    sleep(0.5)
    clique_implicite( "a[id='boutonNourrir']")
    fourrage = int(texte_implicite( "strong.section-fourrage.section-fourrage-target"))
    sleep(0.2)
    clique_implicite( f"li[data-number='{fourrage}']")

    avoine = int(texte_implicite( "strong.section-avoine.section-avoine-target"))
    attente_implicite( "tr.dashed.section-avoine.section-avoine-content").find_element(By.CSS_SELECTOR, f"li[data-number='{avoine}']").click()

    clique_implicite( "button[id='feed-button']")
    sleep(0.2)
    clique_implicite( "a[id='boutonCoucher']")
    sleep(0.2)
    clique_implicite( "a[id='nav-next']")
    sleep(0.2)

driver.get("https://ouranos.equideow.com/todayobjectives/")
try:
    clique_implicite("//span[@class='btn__label__text' and text()='Valider']", By.XPATH)
    sleep(0.2)
    clique_implicite("//span[@class='btn__label__text' and text()='Ok']", By.XPATH)
    sleep(0.2)
    clique_implicite("//span[@class='btn__label__text' and text()='Valider']", By.XPATH)
    print("");
except:
    sys.exit();


