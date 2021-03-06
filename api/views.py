from blog.models import Post, Comment
from blog.serializers import PostSerializer, CommentSerializer
from django.http import Http404
from django.utils import timezone
from django.core.exceptions import ObjectDoesNotExist
# from django.contrib.auth import authenticate, login, logout
from rest_framework.views import APIView
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import status


class PostListAPI(APIView):
    permission_classes = []
    """Retrieve published post instance."""

    def get(self, request, format=None):
        """List all published post"""
        posts = Post.objects.filter(
            published_date__lte=timezone.now()).order_by("-published_date")
        published_post_list = []
        for post in posts:
            published_post_list.append(post.get_record())
        return Response(published_post_list)


class PostDraftListAPI(APIView):
    """Create and retrieve unpublished post instance."""

    def get(self, request, format=None):
        """List all unpublished post"""
        posts = Post.objects.filter(
            published_date__isnull=True).order_by("-created_date")
        published_post_list = []
        for post in posts:
            published_post_list.append(post.get_record())
        return Response(published_post_list)

    def post(self, request, format=None):
        """Create a new unpublished post"""
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            post = serializer.save()
            record = post.get_record()
            response = {
                "title": "Success",
                "message": "Post created",
                "record": record
            }
            return Response(response, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PostDetailAPI(APIView):
    """Retrieve, update and delete post instance."""

    def get_object(self, pk):
        """Check post pk if exist"""
        try:
            return Post.objects.get(pk=pk)
        except Post.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        """Retrieve post"""
        post = self.get_object(pk)
        response = post.get_record()
        return Response(response)

    def patch(self, request, pk, format=None):
        """Patch unpublish post to publish"""
        data = request.data
        action = data["action"]
        if (action == "publish"):
            post = self.get_object(pk)
            post.set_publish()
            record = post.get_record()
            response = {
                "title": "Success",
                "message": "Post published",
                "record": record
            }
            return Response(response, status=status.HTTP_202_ACCEPTED)
        else:
            return Response("No action", status=status.HTTP_204_NO_CONTENT)

    def put(self, request, pk, format=None):
        """Update post"""
        post = self.get_object(pk)
        serializer = PostSerializer(post, data=request.data)
        if (serializer.is_valid()):
            post = serializer.save()
            record = post.get_record()
            response = {
                "title": "Success",
                "message": "Post updated",
                "record": record
            }
            return Response(response, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        """Delete post"""
        post = self.get_object(pk)
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CommentAPI(APIView):
    """Create, retrieve, update and delete unapproved comment instance."""

    def post(self, request, format=None):
        """Create comment"""
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            comment = serializer.save()
            record = comment.get_record()
            response = {
                "title": "Success",
                "message": "Comment created",
                "record": record
            }
            return Response(response, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get_object(self, pk):
        """Check comment pk if exist"""
        try:
            return Comment.objects.get(pk=pk)
        except Comment.DoesNotExist:
            raise Http404

    def patch(self, request, pk, format=None):
        """Patch unapproved comment to approve"""
        data = request.data
        action = data["action"]
        if (action == "approve"):
            comment = self.get_object(pk)
            comment.set_approve()
            record = comment.get_record()
            response = {
                "title": "Success",
                "message": "Comment approved",
                "record": record
            }
            return Response(response, status=status.HTTP_202_ACCEPTED)
        else:
            return Response("No action", status=status.HTTP_204_NO_CONTENT)

    def delete(self, request, pk, format=None):
        """Remove comment"""
        comment = self.get_object(pk)
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class LoginAPI(ObtainAuthToken):
    """Login and generate auth token"""

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(
            data=request.data, context={"request": request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            "token": token.key,
            "user_id": user.pk,
            "email": user.email
        })


class LogoutAPI(APIView):
    """Logout and destroy auth token"""

    def post(self, request, *args, **kwargs):
        try:
            request.user.auth_token.delete()
        except (AttributeError, ObjectDoesNotExist):
            pass
        return Response({
            "detail": "Successfully logged out."
        })

# class Login(ObtainAuthToken):
#     def post(self, request, format=None):
#         user = authenticate(request, username="reuel", password="chidori23")
#         if user != None:
#             login(request, user)
#             token, created = Token.objects.get_or_create(user=request.user)
#             return Response({
#                 'token': token.key,
#                 'user_id': user.pk,
#                 'email': user.email
#             })

# class Logout(APIView):
#     def post(self, request, format=None):
#         request.user.auth_token.delete()
#         logout(request)
#         return HttpResponse(request.user)

# class RetrieveToken(APIView):
#     def post(self, request, format=None):
#         if request.user.is_authenticated:
#             return request.user.auth_token
