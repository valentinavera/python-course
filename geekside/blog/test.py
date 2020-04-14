from django.test import TestCase
from .models import Category, Post
from django.contrib.auth import get_user_model

User = get_user_model()

class DisableCategoryTestCase(TestCase):
    fixtures = ['test_category.json']
    def setUp(self):
        #usuario
        author = User.objects.create_user(username = 'testuser', email='user@test.com', password='abc123')
        #categoría
        self.category= Category.objects.create(name='test category', description='test category description')
        #posts
        self.category.post_set.create(title='Test post 1', text='Test post content 1', author=author)
        self.category.post_set.create(title='Test post 2', text='Test post content 2', author=author)

    def test_disable_category_signal(self):
        #lógica
        self.category.is_active = False
        self.category.save()
        #comprobar los resultados con los resultados esperados
        for post in self.category.post_set.all():
            self.assertFalse(post.is_active)
