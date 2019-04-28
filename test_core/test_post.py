import unittest
from core.post import Post


class TestPost(unittest.TestCase):
    def setUp(self):
        self.post = Post(1)

    def tearDown(self):
        self.post = None

    def test_post_type(self):
        assert self.post.type_display == "Text"

    def test_post_new(self):
        self.post.post_text("hello my first post")
        self.assertTrue(self.post.text != "")


if __name__ == '__main__':
    unittest.main()
