from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import requests
from PIL import Image
import io

class ImageDownloader:
    def __init__(self, webdriver_path):
        self.webdriver_path = webdriver_path
        self.driver = webdriver.Chrome(self.webdriver_path)
    
    def download_image(self, url, path, filename):
        try:
            image_file = io.BytesIO(requests.get(url).content)
            image = Image.open(image_file)
            with open(f'{path}/{filename}', 'wb') as f:
                try:
                    image.save(f, 'JPEG')
                except:
                    image.save(f, 'PNG')
        except Exception as e:
            print(f'DOWNLOAD FAILED - {e}')

    
    def download_images(self, query, limit, path):
        self.driver.get('https:images.google.com')
        search_bar = self.driver.find_element_by_name('q')
        search_bar.send_keys(query)
        search_bar.send_keys(Keys.RETURN)
        urls = set()

        while len(urls) < limit:
            thumbnails = self.driver.find_elements(By.CLASS_NAME, 'Q4LuWd')
            for thumbnail in thumbnails:
                try:
                    thumbnail.click()
                except:
                    pass
                expanded = self.driver.find_elements(By.CLASS_NAME, 'n3VNCb')
                for image in expanded:
                    if image.get_attribute('src') and 'http' in image.get_attribute('src'):
                        urls.add(image.get_attribute('src'))
                if len(urls) >= limit:
                    break

        self.driver.quit()

        for i, url in enumerate(urls):
            self.download_image(url, path, f'{query}{i+1}.jpg')

        return urls