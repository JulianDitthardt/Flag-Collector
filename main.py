from selenium import webdriver
import pandas as pd



class WebScarper():

     def __init__(self,driver_path,embassy_home,first_embassy,last_embassy):
          self._driver = webdriver.Chrome(driver_path)
          self._embassy_home = embassy_home

          self.first_embassy = first_embassy # Web address of first alphabetical embassy
          self.last_embassy = last_embassy # Web address of last alphabetical embassy





     def get_embassy_sites(self):
          '''
          Returns a list of the contact page of each Australian embassy
          :return:
          '''
          self._driver.get(self._embassy_home)
          aTagsInLi = self._driver.find_elements_by_css_selector('li a')
          record = False
          sites = []

          for a in aTagsInLi:
               if a.get_attribute('href') == self.first_embassy:
                    record = True

               if record == True:
                    sites.append(a.get_attribute('href'))

               if a.get_attribute('href') == self.last_embassy:
                    record = False
          return sites

     def check_email(self):












#
# driver = webdriver.Chrome("/opt/homebrew/bin/chromedriver")
#
# # driver.get('https://www.dfat.gov.au/about-us/our-locations/missions/our-embassies-and-consulates-overseas')
#
# # aTagsInLi = driver.find_elements_by_css_selector('li a')
# #
# # sites = []
# start_embassy = "https://www.dfat.gov.au/about-us/our-locations/missions/australian-embassy-afghanistan"
# # final_embassy = "https://www.dfat.gov.au/about-us/our-locations/missions/Pages/australian-embassy-zimbabwe"
# # record = False
#
# driver.get("https://www.dfat.gov.au/about-us/our-locations/missions/australian-consulate-bosnia-and-herzegovina")
#
#
#
#
#
#
# # for a in aTagsInLi:
# #      if a.get_attribute('href') == start_embassy:
# #           record = True
# #
# #      if record == True:
# #           sites.append(a.get_attribute('href'))
# #
# #      if a.get_attribute('href') == final_embassy:
# #           record = False
# #
# # for i in sites:
# #      print(i)
#
# driver.close()