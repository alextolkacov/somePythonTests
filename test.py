from selenium import webdriver

driver = webdriver.Chrome(executable_path=r"C:\Users\alektolk\Downloads\chromedriver.exe")
driver.get("https://unicode-table.com/en/")
driver.maximize_window()

INDEX_NAMES = "(.//div[@class = 'mod'])[3]/div/div/g-link/a/div/div[2]/span[1]"
INDEX_PRICE = "(.//div[@class = 'mod'])[3]/div/div/g-link/a/div/div/span[1]/span[1]"
SOURCE = ".//li[@class = 'symb']"

symbols = driver.find_elements_by_xpath(SOURCE)
sym = []

print("{")
for i in symbols:
    b = i.text
    c = i.get_attribute("title").split('|')[0].strip()
    x = str(c).lower().replace("+", "")

    print("\"" + "\\" + x + "\"" + ": " + "\"" + b + "\"" + ",")

print("}")

driver.quit()
