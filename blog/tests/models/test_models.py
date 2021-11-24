from django.test import TestCase
from django.contrib.auth import get_user_model
from blog.models import Post, Comment

class PostModelTest(TestCase):
    
    def test_post_get_record_raise_exception(self):
        User = get_user_model()
        user = User.objects.create(username="reuel")
        
        post = Post.objects.create(author=user, title="the title", text="the text")
        post_string = post.__str__()
        print(post_string)