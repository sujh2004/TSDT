from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
                
        # 张三听说有一个在线待办事项的应用
        # 他去看了看首页
        # browser = webdriver.Chrome()
        # browser.get("http://localhost:8000")
        self.browser.get('http://localhost:8080')
        # # 他注意到网页里包含“TO-DO”这个词
        # assert 'To-Do' in browser.title,"Browser title was " + browser.title 
        self.assertIn('To-Do',self.browser.title),"browser title was:" + self.browser.title
        self.fail('Finish the test!')
        # 应用有一个输入待办事项的文本输入框

        # 他在文本输入框中输入了"Buy Flowers"

        # 他按了回车键之后，页面更新了
        # 待办事项表格中显示了“1： Buy flowers"

        # 页面中有显示了一个文本输入框，可以输入其他代办事项"
        # 他输入了“Send a gift to Lisi"

        # 页面再次更新，他的清单上显示了这两个待办事项

        # 张三想知道这个网站是否会记住他的清单
        # 他看到网站为他生成了一个唯一的URL

        # 他访问那个URL，发现他的待办事项列表还在
        # 他满意的离开了

if __name__ == "__main__":
    unittest.main()