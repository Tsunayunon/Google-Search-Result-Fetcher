from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By  # By sınıfını import et

# Chrome tarayıcısını başlat
driver = webdriver.Chrome()
try:
    # Google'a git
    driver.get("https://www.google.com.tr/")
    # Arama kutusunu bul ve "BTK Akademi" yaz
    search_box = driver.find_element(By.NAME, "q")
    search_box.send_keys("YOUTUBE")
    search_box.send_keys(Keys.RETURN)  # Enter tuşuna bas
    # İlk sonucun başlığını ve URL'sini al
    first_result = driver.find_element(By.CSS_SELECTOR, "h3")
    title = first_result.text
    url = first_result.find_element(By.XPATH, "..").get_attribute("href")
    # Sonucu ekrana yazdır
    print("Başlık:", title)
    print("URL:", url)
except Exception as e:
    print("Hata oluştu:", str(e))
finally:
    # Tarayıcıyı kapat
    driver.quit()  # Bu satırı yorumdan çıkarınca çalışacaktır
