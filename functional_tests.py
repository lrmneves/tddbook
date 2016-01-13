from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):
	
	def setUp(self):
		self.browser = webdriver.Firefox()
		self.browser.implicity_wait(3)
	def tearDown(self):
		self.browser.quit()

	def test_can_start_a_list_and_retrieve_it_later(self):
		#Checking homepage of app
		self.browser.get('http://localhost:8000')

		#Check the title
		self.assertIn('To-Do',self.browser.title) 
		self.fail("Finish the test!")

		#enter to-do list


		#Read Chapters

		#after enter, page updates and show 1: Read Chapters as an item

		#there is a textbox inviting other itens

		#enter Write Reading Summary

		#page updates and show both itens

		#look for unique url


if __name__ == '__main__':
	unittest.main(warnings="ignore")