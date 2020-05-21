from django.shortcuts import render
from menu.models import Category, Meal
from django.views.generic import ListView, TemplateView
# Create your views here.
class CategoryList(ListView):
    model = Category
    queryset = Category.objects.all()
    context_object_name = 'categories'
    template_name = 'menu/menu.html'

class MealList(ListView):
    model = Meal
    context_object_name = 'dishes'
    template_name = 'menu/menu_category.html'

    def get_queryset(self):
        return Meal.objects.filter(category__slug=self.kwargs.get('slug'))

class MenuView(TemplateView):
    template_name = "menu/menu.html"