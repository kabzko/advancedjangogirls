from django.test import TestCase
from django.contrib.auth import get_user_model
from blog.tests.factory import PostFactory, CommentFactory

class PostModelTest(TestCase):
    """Testcase for the post model."""
    def test_post_return_str(self):
        User = get_user_model()
        user = User.objects.create(username="reuel")
        
        title = "the title"
        
        post = PostFactory.create(title=title)
        
        self.assertEqual(title, str(post))
        self.assertEqual(post.title, str(post))
        
class CommentModelTest(TestCase):
    """Testcase for the comment model."""
    def test_comment_return_str(self):
        User = get_user_model()
        user = User.objects.create(username="reuel")
        
        text = "the comment"
        
        comment = CommentFactory.create(text=text)
        
        self.assertEqual(text, str(comment))
        self.assertEqual(comment.text, str(comment))