from django.test import TestCase
from django.urls import reverse
from .models import Category, Recipe


class RecipeViewsTest(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name="Desserts")
        for i in range(15):
            Recipe.objects.create(
                title=f"Recipe {i}",
                description="Test Desc",
                instructions="Test Inst",
                ingredients="Test Ing",
                category=self.category
            )
            
    def test_main_view(self):
        response = self.client.get(reverse('main'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'main.html')
        self.assertEqual(len(response.context['recipes']), 10)
        
    def test_category_detail_view(self):
        response = self.client.get(reverse('category_detail', kwargs={'id': self.category.id}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'category_detail.html')
        self.assertEqual(response.context['category'], self.category)
