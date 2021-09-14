from selenium import webdriver
from selenium import common
import pandas as pd



class WebScarper():

     def __init__(self,driver_path,embassy_home,first_embassy,last_embassy):
          self._driver = webdriver.Chrome(driver_path)
          self._embassy_home = embassy_home

          self.first_embassy = first_embassy # Web address of first alphabetical embassy
          self.last_embassy = last_embassy # Web address of last alphabetical embassy





     def _get_embassy_sites(self):
          '''
          Returns a list of the contact page of each Australian em
          :return:
          '''
          self._driver.get(self._embassy_home)
          aTagsInLi = self._driver.find_elements_by_css_selector('li a')
          record = False
          sites = {}

          for a in aTagsInLi:
               if a.get_attribute('href') == self.first_embassy:
                    record = True

               if record == True:
                    sites[a.text] = a.get_attribute('href')

               if a.get_attribute('href') == self.last_embassy:
                    record = False

          return sites



     def find_emails(self):
          '''
          Finds the stored email address for each consulate.
          '''
          emails = {}
          site_list = self._get_embassy_sites()

          for country,site in site_list.items():
               self._driver.get(site)
               try:
                    mail = self._driver.find_element_by_xpath('//*[@id="bodyContent"]/div/div/div[2]/div/ol/li/div[1]/div[2]/div[1]/div[2]/p/a')
                    emails[country] = mail.get_attribute('href')
               except common.exceptions.NoSuchElementException:
                    pass

               print(emails)


     def complete(self):
          self._driver.close()

if __name__ == '__main__':
     driver = "/opt/homebrew/bin/chromedriver"
     home = 'https://protocol.dfat.gov.au/Public/MissionsInAustralia'
     start_embassy = "https://protocol.dfat.gov.au/Public/Missions/4"
     final_embassy = "https://protocol.dfat.gov.au/Public/Missions/222"

     web = WebScarper(driver,home,start_embassy,final_embassy)
     web.find_emails()
     web.complete()










)