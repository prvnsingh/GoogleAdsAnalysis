from selenium import webdriver
# from selenium.webdriver.support.wait import WebDriverWait
# from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.options import Options
import geckodriver_autoinstaller
from selenium.webdriver.common.by import By
# from selenium.webdriver.support.wait import WebDriverWait
import os
import time


class GetAds():

    def execute(self, url):
        #directory to save ads images
        path = "image/"
        try:
            if os.path.exists(path):
                print("deleting previous ads")
                for ad in os.listdir(path):
                    os.remove(path+ad)
            else:
                os.makedirs(path)
                print("creating folder to store ads")

            #creating a headless firefox window
            fireFoxOptions = Options()
            fireFoxOptions.add_argument("-headless")
            # br = webdriver.Firefox(executable_path=GeckoDriverManager().install(), options=fireFoxOptions)
            geckodriver_autoinstaller.install()
            br = webdriver.Firefox(options=fireFoxOptions)

            print("browsing url :",url)
            br.get(url)
            time.sleep(2)

        # saving the html of the page
            with open('html_source_code.txt', 'w') as f:
                f.write(br.page_source)
                f.close()
            # try:
            #     WebDriverWait(br, 10).until(EC.frame_to_be_available_and_switch_to_it((By.XPATH,"//*[contains(@id,'google_ads_i')]")))
            # except Exception as e:
            #     print(e)

            #checking for elements with google ads
            ads = br.find_elements(by= By.XPATH,value ="//*[contains(@id,'google_ads_i')]")
            for i in range(len(ads)):
                print("ad :",i,ads[i])
                name = path +"ad"+str(i)+".png"
                print(name)
                try:
                    ads[i].screenshot(name)
                    print("ad is saved")
                except Exception as e:
                    print(e)
                    print("Error while saving ad")
            br.close()
        except Exception as e:
            print(e)

# for testing
if __name__ == "__main__":
   i = GetAds()
   #please change the url accordingly
   url = "https://speedtest.net/"
   i.execute(url)


