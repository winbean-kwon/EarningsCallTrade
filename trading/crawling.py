from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
chrome_options.add_argument('window-size=1920,1080')
driver = webdriver.Chrome(service = Service(ChromeDriverManager().install()), options=chrome_options)
driver.implicitly_wait(5)

driver.get('https://www.earningswhispers.com/calendar?sb=p&d=9&t=all')

driver.implicitly_wait(5)

cookie_check = driver.find_element(By.CLASS_NAME, "accept-policy").click()
specific_time_crawle = driver.find_elements(By.CSS_SELECTOR, 'div.col-12.caltime')
earning_company_name_crawle = driver.find_elements(By.CSS_SELECTOR, 'div.col-12.calticker')
earning_confirmed = driver.find_elements(By.CLASS_NAME, "epsdateconfirmed")
earning_not_confirmed = driver.find_elements(By.CLASS_NAME, "epsdatenotconfirmed")
earning_companies = earning_confirmed + earning_not_confirmed

specific_time = []
earning_company_name = []

#선택자중에 빈 문자열을 반환하는게 있어서 2배로 함
for i in range(0, len(earning_companies)*2):
    if specific_time_crawle[i].text != '':
        specific_time.append(specific_time_crawle[i].text)

# 빈 문자열을 포함하는 것들이 있어서 둘이 합치면 엉키게 됨
for i in range(0, len(earning_companies)):
    if earning_company_name_crawle[i].text != '':
        earning_company_name.append(earning_company_name_crawle[i].text)

total_crawle = {key: value for key, value in zip(earning_company_name,specific_time)}
        
driver.close()