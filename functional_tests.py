from selenium import webdriver
import unittest


class NewVisitorTest(unittest.TestCase):

	def setUp(self):
		self.browser = webdriver.Firefox()

	def tearDown(self):
		self.browser.quit()

	def test_can_start_a_list_and_retrieve_it_later(self):
		#Jack heard about a cool new to-do website and goes to check
		#out its homepage
		self.browser.get('http://localhost:8000')

		#He notices page title and header mention to-do lists
		self.assertIn('To-Do', self.browser.title)
		self.fail('Finish the test')

		#He is invited to enter a to-do item straight away

		#He enters "Buy peacock feathers", his hobby is fly fishing 
		#lures

		#When he hits enter, page updates and the page now lists
		#"1: Buy peacock feathers" as an item in a to-do list

		#The text box inviting him to add another item is still there.
		#He enters "Use peacock feathers to make a fly"

		#Page again updates, shows both items on his list

		#Jack wonders if the page will remember his list even if he
		#refreshes the page, notices unique URL generated by the site

		#He refreshes the page, his list is still there

		#The end

if __name__ == '__main__':
	unittest.main(warnings='ignore')
