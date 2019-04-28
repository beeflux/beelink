import unittest
from core.post import Post


class TestPost(unittest.TestCase):
    def test_post_type(self):
        post = Post(1)
        assert post.type_display == "Text"

    def test_post_new(self):
        post = Post(1)
        post.post_text("hello my first post")
        self.assertTrue(post.text != "")


if __name__ == '__main__':
    unittest.main()
