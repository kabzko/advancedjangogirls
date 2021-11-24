from django.test import TestCase
from django.contrib.auth import get_user_model
from rest_framework.test import APIRequestFactory
from blog.views import PostListAPI, PostDraftListAPI, PostDetailAPI, CommentAPI
from blog.models import Post, Comment


class PostViewTestCase(TestCase):
    
    def test_get_all_post_object_filtered_published(self):
        """
        Return all published queryset with status code 200
        """
        User = get_user_model()
        user = User.objects.create(username="reuel")
        request_factory = APIRequestFactory()
        
        post = Post.objects.create(author=user, title="the title", text="the text")
        post.publish()
        expected = [post.get_record()]
        
        view = PostListAPI.as_view()
        request = request_factory.get("/post/")
        response = view(request)
        
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, expected)
        
    def test_get_all_post_object_filtered_unpublished(self):
        """
        Return all unpublished queryset with status code 200
        """
        User = get_user_model()
        user = User.objects.create(username="reuel")
        request_factory = APIRequestFactory()
        
        post = Post.objects.create(author=user, title="the title", text="the text")
        expected = [post.get_record()]
        
        view = PostDraftListAPI.as_view()
        request = request_factory.get("/post/draft/")
        response = view(request)
        
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, expected)
        
    def test_create_new_unpublish_post_instance(self):
        """
        Create a new unpublish post instance and return a response with status code 201
        """
        User = get_user_model()
        user = User.objects.create(username="reuel")
        request_factory = APIRequestFactory()
        old_count = Post.objects.count()
        
        view = PostDraftListAPI.as_view()
        data = {"author": user.id, "title": "the title", "text": "the text"}
        request = request_factory.post("/post/draft/", data)
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
        User = get_user_model()
        User.objects.create(username="reuel")
        request_factory = APIRequestFactory()
        
        view = PostDraftListAPI.as_view()
        data = {}
        request = request_factory.post("/post/draft/", data)
        response = view(request)
        
        self.assertEqual(response.status_code, 400)
        
    def test_get_specific_post_object_using_not_exist_pk(self):
        """
        Get specific post object using not existing pk and return status code 404
        """
        pk = 99999
        request_factory = APIRequestFactory()
        
        view = PostDetailAPI.as_view()
        request = request_factory.get("/post/{}/".format(pk))
        response = view(request, pk)
        
        self.assertEqual(response.status_code, 404)
        
    def test_get_specific_post_object(self):
        """
        Get specific post object and return a response with status code 200
        """
        User = get_user_model()
        user = User.objects.create(username="reuel")
        request_factory = APIRequestFactory()
        
        post = Post.objects.create(author=user, title="the title", text="the text")
        expected = post.get_record()
        
        view = PostDetailAPI.as_view()
        request = request_factory.get("/post/{}/".format(post.pk))
        response = view(request, post.pk)
        
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, expected)
        
    def test_update_specific_post_object(self):
        """
        Update specific post object and return a response with status code 202
        """
        User = get_user_model()
        user = User.objects.create(username="reuel")
        request_factory = APIRequestFactory()
        
        post = Post.objects.create(author=user, title="the title", text="the text")
        post.title = "my title"
        post.text = "my text"
        post.save()
        expected = post.get_record()
        
        view = PostDetailAPI.as_view()
        data = {"author": user.id, "title": "my title", "text": "my text"}
        request = request_factory.put("/post/{}/".format(post.pk), data)
        response = view(request, post.pk)
        
        self.assertEqual(response.status_code, 202)
        self.assertEqual(response.data["title"], "Success")
        self.assertEqual(response.data["message"], "Post updated")
        self.assertEqual(response.data["record"], expected)
        
    def test_update_post_specific_object_with_empty_form_data(self):
        """
        Update specific post object with empty form data and return status code 400
        """
        User = get_user_model()
        user = User.objects.create(username="reuel")
        request_factory = APIRequestFactory()
        
        post = Post.objects.create(author=user, title="the title", text="the text")
        
        view = PostDetailAPI.as_view()
        data = {}
        request = request_factory.put("/post/{}/".format(post.pk), data)
        response = view(request, post.pk)
        
        self.assertEqual(response.status_code, 400)
        
    def test_delete_post_specific_object(self):
        """
        Delete specific post object and return status code 204
        """
        User = get_user_model()
        user = User.objects.create(username="reuel")
        request_factory = APIRequestFactory()
        
        post = Post.objects.create(author=user, title="the title", text="the text")
        
        view = PostDetailAPI.as_view()
        request = request_factory.delete("/post/{}/".format(post.pk))
        response = view(request, post.pk)
        
        self.assertEqual(response.status_code, 204)
        
    def test_patch_unpublish_to_publish_post(self):
        """
        Patch unpublished post to publish and return a response with status code 202
        """
        User = get_user_model()
        user = User.objects.create(username="reuel")
        request_factory = APIRequestFactory()
        
        post = Post.objects.create(author=user, title="the title", text="the text")
        not_expected = post.get_record()
        
        view = PostDetailAPI.as_view()
        data = {"action": "publish"}
        request = request_factory.patch("/post/{}/publish/".format(post.pk), data)
        response = view(request, post.pk)
        
        self.assertEqual(response.status_code, 202)
        self.assertEqual(response.data["title"], "Success")
        self.assertEqual(response.data["message"], "Post published")
        self.assertNotEqual(response.data["record"], not_expected)
        
    def test_publish_unpublished_post_using_wrong_action(self):
        """
        Patch unpublished post to publish using wrong action and return a response with status code 204
        """
        User = get_user_model()
        user = User.objects.create(username="reuel")
        request_factory = APIRequestFactory()
        
        post = Post.objects.create(author=user, title="the title", text="the text")
        not_expected = post.get_record()
        
        view = PostDetailAPI.as_view()
        data = {"action": "approve"}
        request = request_factory.patch("/post/{}/publish/".format(post.pk), data)
        response = view(request, post.pk)
        
        self.assertEqual(response.status_code, 204)
        self.assertEqual(response.data, "No action")
        
class CommentViewTestCase(TestCase):
    
    def test_create_new_unapproved_comment_object(self):
        """
        Create a new unapproved comment object and return a response with status code 201
        """
        User = get_user_model()
        user = User.objects.create(username="reuel")
        request_factory = APIRequestFactory()
        
        post = Post.objects.create(author=user, title="the title", text="the text")
        
        view = CommentAPI.as_view()
        data = {"post": post.pk, "author": user, "text": "the comment"}
        request = request_factory.post("/comment/", data)
        response = view(request)
        
        comment = Comment.objects.filter(post=post).order_by("id").last()
        expected = comment.get_record()

        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data["title"], "Success")
        self.assertEqual(response.data["message"], "Comment created")
        self.assertEqual(response.data["record"], expected)
        
    def test_create_new_unapproved_comment_object_with_empty_form_data(self):
        """
        Create a new unapproved comment object with empty_form_data and return status code 400
        """
        User = get_user_model()
        user = User.objects.create(username="reuel")
        request_factory = APIRequestFactory()
        
        Post.objects.create(author=user, title="the title", text="the text")
        
        view = CommentAPI.as_view()
        data = {}
        request = request_factory.post("/comment/", data)
        response = view(request)

        self.assertEqual(response.status_code, 400)
        
    def test_get_specific_comment_object_using_not_exist_pk(self):
        """
        Get specific comment object using not existing pk and return status code 404
        """
        pk = 99999
        request_factory = APIRequestFactory()
 
        view = CommentAPI.as_view()
        request = request_factory.delete("/comment/{}/".format(pk))
        response = view(request, pk)
        
        self.assertEqual(response.status_code, 404)  
        
    def test_patch_unapprove_to_approve_comment_object(self):
        """
        Patch unapproved comment to approve and return a response with status code 202
        """
        User = get_user_model()
        user = User.objects.create(username="reuel")
        request_factory = APIRequestFactory()
        
        post = Post.objects.create(author=user, title="the title", text="the text")
        comment = Comment.objects.create(post=post, author=user, text="the comment")
        not_expected = comment.get_record()
        
        view = CommentAPI.as_view()
        data = {"action": "approve"}
        request = request_factory.patch("/comment/{}/".format(comment.pk), data)
        response = view(request, comment.pk)
        
        self.assertEqual(response.status_code, 202)
        self.assertEqual(response.data["title"], "Success")
        self.assertEqual(response.data["message"], "Comment approved")
        self.assertNotEqual(response.data["record"], not_expected)
        
    def test_patch_unapprove_to_approve_comment_object_using_wrong_action(self):
        """
        Patch unapproved comment to approve using wrong action and return a response with status code 204
        """
        User = get_user_model()
        user = User.objects.create(username="reuel")
        request_factory = APIRequestFactory()
        
        post = Post.objects.create(author=user, title="the title", text="the text")
        comment = Comment.objects.create(post=post, author=user, text="the comment")
        
        view = CommentAPI.as_view()
        data = {"action": "publish"}
        request = request_factory.patch("/comment/{}/".format(comment.pk), data)
        response = view(request, comment.pk)
        
        self.assertEqual(response.status_code, 204)
        self.assertEqual(response.data, "No action")
        
    def test_remove_specific_comment_object(self):
        """
        Remove a specific comment object and return status code 204
        """
        User = get_user_model()
        user = User.objects.create(username="reuel")
        request_factory = APIRequestFactory()
        
        post = Post.objects.create(author=user, title="the title", text="the text")
        comment = Comment.objects.create(post=post, author=user, text="the comment")
        
        view = CommentAPI.as_view()
        request = request_factory.delete("/comment/{}/".format(comment.pk))
        response = view(request, comment.pk)
        
        self.assertEqual(response.status_code, 204)    