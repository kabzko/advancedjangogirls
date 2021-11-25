from django.test import TestCase
from django.contrib.auth import get_user_model
from rest_framework.test import APIRequestFactory, force_authenticate
from rest_framework.authtoken.models import Token
from api.views import PostListAPI, PostDraftListAPI, PostDetailAPI, CommentAPI, LoginAPI
from blog.models import Post, Comment
from blog.tests.factory import UserFactory, PostFactory, CommentFactory

from pprint import pp

class PostViewTest(TestCase):
    """Testcase for the post views."""
    def test_get_all_post_object_filtered_published(self):
        """
        Return all published queryset with status code 200
        """
        request_factory = APIRequestFactory()
        
        post = PostFactory()
        post.set_publish()
        expected = [post.get_record()]
        
        User = get_user_model()
        user = User.objects.get(username=post.author)
        
        view = PostListAPI.as_view()
        request = request_factory.get("/post/")
        force_authenticate(request, user=user)
        response = view(request)
        
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, expected)
        
    def test_get_all_post_object_filtered_unpublished(self):
        """
        Return all unpublished queryset with status code 200
        """
        request_factory = APIRequestFactory()
        
        post = PostFactory()
        expected = [post.get_record()]
        
        User = get_user_model()
        user = User.objects.get(username=post.author)
        
        view = PostDraftListAPI.as_view()
        request = request_factory.get("/post/draft/")
        force_authenticate(request, user=user)
        response = view(request)
        
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, expected)
        
    def test_create_new_unpublish_post_instance(self):
        """
        Create a new unpublish post instance and return a response with status code 201
        """
        user = UserFactory()
        request_factory = APIRequestFactory()
        old_count = Post.objects.count()
        
        view = PostDraftListAPI.as_view()
        data = {"author": user.id, "title": "the title", "text": "the text"}
        request = request_factory.post("/post/draft/", data)
        force_authenticate(request, user=user)
        response = view(request)
        
        created_post = Post.objects.order_by("id").last()
        new_count = Post.objects.count()
        
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data["title"], "Success")
        self.assertEqual(response.data["message"], "Post created")
        self.assertEqual(response.data["record"], created_post.get_record())
        self.assertEqual(old_count + 1, new_count)
        
    def test_create_new_unpublish_post_instance_with_empty_form_data(self):
        """
        Create a new unpublish post instance with empty form data and return status code 400
        """
        request_factory = APIRequestFactory()
        
        post = PostFactory()
        User = get_user_model()
        user = User.objects.get(username=post.author)
        
        view = PostDraftListAPI.as_view()
        data = {}
        request = request_factory.post("/post/draft/", data)
        force_authenticate(request, user=user)
        response = view(request)
        
        self.assertEqual(response.status_code, 400)
        
    def test_get_specific_post_object_using_not_exist_pk(self):
        """
        Get specific post object using not existing pk and return status code 404
        """
        pk = 99999
        request_factory = APIRequestFactory()
        
        post = PostFactory()
        User = get_user_model()
        user = User.objects.get(username=post.author)
        
        view = PostDetailAPI.as_view()
        request = request_factory.get("/post/{}/".format(pk))
        force_authenticate(request, user=user)
        response = view(request, pk)
        
        self.assertEqual(response.status_code, 404)
        
    def test_get_specific_post_object(self):
        """
        Get specific post object and return a response with status code 200
        """
        request_factory = APIRequestFactory()
        
        post = PostFactory()
        expected = post.get_record()
        
        User = get_user_model()
        user = User.objects.get(username=post.author)
        
        view = PostDetailAPI.as_view()
        request = request_factory.get("/post/{}/".format(post.pk))
        force_authenticate(request, user=user)
        response = view(request, post.pk)
        
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, expected)
        
    def test_update_specific_post_object(self):
        """
        Update specific post object and return a response with status code 202
        """
        request_factory = APIRequestFactory()
        
        post = PostFactory()
        post.title = "my title"
        post.text = "my text"
        post.save()
        expected = post.get_record()
        
        User = get_user_model()
        user = User.objects.get(username=post.author)

        view = PostDetailAPI.as_view()
        data = {"author": user.id, "title": "my title", "text": "my text"}
        request = request_factory.put("/post/{}/".format(post.pk), data)
        force_authenticate(request, user=user)
        response = view(request, post.pk)
        
        self.assertEqual(response.status_code, 202)
        self.assertEqual(response.data["title"], "Success")
        self.assertEqual(response.data["message"], "Post updated")
        self.assertEqual(response.data["record"], expected)
        
    def test_update_post_specific_object_with_empty_form_data(self):
        """
        Update specific post object with empty form data and return status code 400
        """
        request_factory = APIRequestFactory()
        
        post = PostFactory()
        
        User = get_user_model()
        user = User.objects.get(username=post.author)
        
        view = PostDetailAPI.as_view()
        data = {}
        request = request_factory.put("/post/{}/".format(post.pk), data)
        force_authenticate(request, user=user)
        response = view(request, post.pk)
        
        self.assertEqual(response.status_code, 400)
        
    def test_delete_post_specific_object(self):
        """
        Delete specific post object and return status code 204
        """
        request_factory = APIRequestFactory()
        
        post = PostFactory()
        
        User = get_user_model()
        user = User.objects.get(username=post.author)
        
        view = PostDetailAPI.as_view()
        request = request_factory.delete("/post/{}/".format(post.pk))
        force_authenticate(request, user=user)
        response = view(request, post.pk)
        
        self.assertEqual(response.status_code, 204)
        
    def test_patch_unpublish_to_publish_post(self):
        """
        Patch unpublished post to publish and return a response with status code 202
        """
        request_factory = APIRequestFactory()
        
        post = PostFactory()
        not_expected = post.get_record()
        
        User = get_user_model()
        user = User.objects.get(username=post.author)
        
        view = PostDetailAPI.as_view()
        data = {"action": "publish"}
        request = request_factory.patch("/post/{}/publish/".format(post.pk), data)
        force_authenticate(request, user=user)
        response = view(request, post.pk)
        
        self.assertEqual(response.status_code, 202)
        self.assertEqual(response.data["title"], "Success")
        self.assertEqual(response.data["message"], "Post published")
        self.assertNotEqual(response.data["record"], not_expected)
        
    def test_publish_unpublished_post_using_wrong_action(self):
        """
        Patch unpublished post to publish using wrong action and return a response with status code 204
        """
        request_factory = APIRequestFactory()
        
        post = PostFactory()
        
        User = get_user_model()
        user = User.objects.get(username=post.author)
        
        view = PostDetailAPI.as_view()
        data = {"action": "approve"}
        request = request_factory.patch("/post/{}/publish/".format(post.pk), data)
        force_authenticate(request, user=user)
        response = view(request, post.pk)
        
        self.assertEqual(response.status_code, 204)
        self.assertEqual(response.data, "No action")
        
class CommentViewTest(TestCase):
    """Testcase for the comment views."""
    def test_create_new_unapproved_comment_object(self):
        """
        Create a new unapproved comment object and return a response with status code 201
        """
        request_factory = APIRequestFactory()
        old_count = Comment.objects.count()
        
        post = PostFactory()
        
        User = get_user_model()
        user = User.objects.get(username=post.author)
        
        view = CommentAPI.as_view()
        data = {"post": post.pk, "author": post.author, "text": "the comment"}
        request = request_factory.post("/comment/", data)
        force_authenticate(request, user=user)
        response = view(request)
        
        comment = Comment.objects.filter(post=post).order_by("id").last()
        expected = comment.get_record()
        new_count = Comment.objects.count()

        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data["title"], "Success")
        self.assertEqual(response.data["message"], "Comment created")
        self.assertEqual(response.data["record"], expected)
        self.assertEqual(old_count + 1, new_count)
        
    def test_create_new_unapproved_comment_object_with_empty_form_data(self):
        """
        Create a new unapproved comment object with empty_form_data and return status code 400
        """
        request_factory = APIRequestFactory()
        
        post = PostFactory()
        
        User = get_user_model()
        user = User.objects.get(username=post.author)
        
        view = CommentAPI.as_view()
        data = {}
        request = request_factory.post("/comment/", data)
        force_authenticate(request, user=user)
        response = view(request)

        self.assertEqual(response.status_code, 400)
        
    def test_get_specific_comment_object_using_not_exist_pk(self):
        """
        Get specific comment object using not existing pk and return status code 404
        """
        pk = 99999
        request_factory = APIRequestFactory()
        
        post = PostFactory()
        User = get_user_model()
        user = User.objects.get(username=post.author)
 
        view = CommentAPI.as_view()
        request = request_factory.delete("/comment/{}/".format(pk))
        force_authenticate(request, user=user)
        response = view(request, pk)
        
        self.assertEqual(response.status_code, 404)  
        
    def test_patch_unapprove_to_approve_comment_object(self):
        """
        Patch unapproved comment to approve and return a response with status code 202
        """
        request_factory = APIRequestFactory()

        comment = CommentFactory()
        not_expected = comment.get_record()
        
        User = get_user_model()
        user = User.objects.get(username=comment.author)
        
        view = CommentAPI.as_view()
        data = {"action": "approve"}
        request = request_factory.patch("/comment/{}/".format(comment.pk), data)
        force_authenticate(request, user=user)
        response = view(request, comment.pk)
        
        self.assertEqual(response.status_code, 202)
        self.assertEqual(response.data["title"], "Success")
        self.assertEqual(response.data["message"], "Comment approved")
        self.assertNotEqual(response.data["record"], not_expected)
        
    def test_patch_unapprove_to_approve_comment_object_using_wrong_action(self):
        """
        Patch unapproved comment to approve using wrong action and return a response with status code 204
        """
        request_factory = APIRequestFactory()
        
        comment = CommentFactory()
        User = get_user_model()
        user = User.objects.get(username=comment.author)
        
        view = CommentAPI.as_view()
        data = {"action": "publish"}
        request = request_factory.patch("/comment/{}/".format(comment.pk), data)
        force_authenticate(request, user=user)
        response = view(request, comment.pk)
        
        self.assertEqual(response.status_code, 204)
        self.assertEqual(response.data, "No action")
        
    def test_remove_specific_comment_object(self):
        """
        Remove a specific comment object and return status code 204
        """
        request_factory = APIRequestFactory()
        
        comment = CommentFactory()
        User = get_user_model()
        user = User.objects.get(username=comment.author)
        
        view = CommentAPI.as_view()
        request = request_factory.delete("/comment/{}/".format(comment.pk))
        force_authenticate(request, user=user)
        response = view(request, comment.pk)
        
        self.assertEqual(response.status_code, 204)
        
class LoginAuthenticationTest(TestCase):
    """Testcase for login authentication"""
    def test_login_authentication(self):
        """Login and generate a token"""
        user = UserFactory()
        request_factory = APIRequestFactory()
        
        view = LoginAPI.as_view()
        data = {"username": user.username, "password": "12345678"}
        request = request_factory.post("/api-token-auth/login/", data)
        response = view(request)
        
        token = Token.objects.get(user_id=user.id)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["token"], token.key)
        self.assertEqual(response.data["user_id"], user.id)
        