from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options


chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
chrome_options.add_argument('window-size=1920,1080')
driver = webdriver.Chrome(service = Service(ChromeDriverManager().install()), options=chrome_options)
driver.implicitly_wait(5)



driver.get('https://www.earningswhispers.com/calendar?sb=p&d=9&t=all')

driver.implicitly_wait(5)


cookie_check = driver.find_element(By.CLASS_NAME, "accept-policy").click()
specific_time = driver.find_elements(By.CSS_SELECTOR, 'div.col-12.caltime')
earning_confirmed = driver.find_elements(By.CLASS_NAME, "epsdateconfirmed")
earning_not_confirmed = driver.find_elements(By.CLASS_NAME, "epsdatenotconfirmed")
earning_companies = earning_confirmed + earning_not_confirmed

for i in range(1, len(earning_companies)*2):
    driver.implicitly_wait(10)
    if specific_time[i].text != '':
        print(specific_time[i].text)

driver.close()


# /html/body/form/div[3]/section/ul/li[2]/div[1]/div[4]
# //*[@id="T-BAC"]/div[4]

# /html/body/form/div[3]/section/ul/li[3]/div[1]/div[4]
# //*[@id="T-SCHW"]/div[4]