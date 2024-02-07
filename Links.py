from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import json

def get_links(url):
    options = Options()
    options.add_argument("--headless")

    driver = webdriver.Chrome(options=options)

    driver.get(url)

    try :
        cookies = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "didomi-notice-agree-button")))
        cookies.click()
    except:
        pass
    
    links = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "a.tile_title")))
    
    links = list(set(links))
    
    urls = []
    for link in links:
        urls.append(link.get_attribute("href"))
            
    with open("urls.json", "w") as file:
        json.dump(urls, file)
    
if __name__ == "__main__":
    get_links("https://www.cuisineaz.com/categories/desserts-cat48681")
    
    with open("urls.json", "r") as file:
        urls = json.load(file)
    for url in urls:
        print(url)