import time

from generics.base_test import BaseTest

class Test2(BaseTest):

    def test_2(self):
        print("test 2")
        print(self.page.title())
        time.sleep(3)
