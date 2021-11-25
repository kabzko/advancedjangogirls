import factory
import factory.fuzzy

from django.contrib.auth import get_user_model
from blog.models import Post, Comment

User = get_user_model()

class UserFactory(factory.django.DjangoModelFactory):
    
    username = factory.Faker("name")
    password = factory.PostGenerationMethodCall('set_password', '12345678')
    
    class Meta:
        model = User

class PostFactory(factory.django.DjangoModelFactory):
    
    author = factory.SubFactory(UserFactory)
    title = factory.Faker("sentence")
    text = factory.Faker("sentence")
    
    class Meta:
        model = Post
    
class CommentFactory(factory.django.DjangoModelFactory):
    
    post = factory.SubFactory(PostFactory)
    author = factory.SubFactory(UserFactory)
    text = factory.Faker("sentence")
    
    class Meta:
        model = Comment