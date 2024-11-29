from django.test import TestCase
from django.contrib.auth.models import User
from blog.models import Post,Category

class Test_Create_Post(TestCase):
    @classmethod
    def setUpTestData(cls):
        test_category = Category.objects.create(name='django')
        test_user = User.objects.create_user(
            username='testuser1',
            password='12345'
        )

        test_post = Post.objects.create(category_id=1, title='Post title', excerpt='Post excerpt', content='Post content', slug='post-title', author_id=1, status="published")

    def test_blog_content(self):
        post=Post.postobjects.get(id=1)
        cat=Category.objects.get(id=1)
        author=User.objects.get(id=1)
        self.assertEqual(str(post), "Post title")
        self.assertEqual(str(cat), "django")
        self.assertEqual(str(author), "testuser1")