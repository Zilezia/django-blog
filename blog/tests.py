from django.test import TestCase
from django.utils import timezone

from blog.models import Post, Comment

class PostModelTest(TestCase):
    def test_recent_pub_with_future_post(self):
        future_post = Post(pub_date=timezone.now() + timezone.timedelta(days=7))
        self.assertIs(future_post.recent_pub(), False)
    def test_recent_pub_with_past_post(self):
        past_post = Post(pub_date=timezone.now() - timezone.timedelta(days=0.5))
        self.assertIs(past_post.recent_pub(), True)

class CommentModelTest(TestCase):
    def test_comment_str_representation(self):
        comment = Comment(comment="Test comment.")
        self.assertIs(str(comment), "Test comment.")
    def test_comment_assoc_post(self):
        post = Post.objects.create(title="Test Post", content="Test content", author="Test author", pub_date=timezone.now())
        comment = Comment.objects.create(post=post, comment="Test comment.")
        self.assertIs(comment.post, post)
