from django.test import TestCase
from blog.models import Post


class PostTest(TestCase):

    def test_str(self):
        my_title = Post(title="Basic test case for title.")
        self.assertEquals(
            str(my_title), 'Basic test case for title.',
        )
