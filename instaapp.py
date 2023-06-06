from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

class InstaBot:
	def __init__(self,username,password):
		self.username = username
		self.password = password
		self.bot = webdriver.Firefox()

	def login(self):
		bot = self.bot
		bot.get('https://instagram.com/')
		time.sleep(3)
		email = bot.find_element_by_name('username')
		password = bot.find_element_by_name('password')
		email.clear()
		password.clear()
		email.send_keys(self.username)
		password.send_keys(self.password)
		password.send_keys(Keys.RETURN)
		time.sleep(3)

	def like_post(self, hashtag):
		bot = self.bot
		bot.get('https://instagram.com/explore/tags/' + hashtag)
		time.sleep(3)

		for i in range(1,5):
			bot.execute_script('window.scrollTo(0,document.body.scrollHeight)')
			time.sleep(2)

			posts = bot.find_elements_by_css_selector('.v1Nh3 a')
			links = [elem.get_attribute('href') for elem in posts]

			print(links)

			for link in links:
				bot.get(link)
				try:
					bot.find_element_by_class_name('fr66n').click()
					time.sleep(10)
				except Exception as ex:
					time.sleep(60)
						

ed = InstaBot('annilltimothy', 'youwishyouknewmypassword')
ed.login()
ed.like_post('travel')
