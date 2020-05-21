from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView, View
from article.models import Article
from article.forms import ArticleForm
from django.urls import reverse
from account.models import Profile

class IndexView(ListView):
    model = Article
    template_name = 'index.html'
    context_object_name = 'articles'

    def get_queryset(self):
        return Article.objects.all()

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(IndexView, self).get_context_data()
        return context

class ArticleCreateView(CreateView):
    model = Article
    template_name = 'article/create.html'
    form_class = ArticleForm
    # добавлення автора публікації
    def form_valid(self, form):
        profile = Profile.objects.get(user = self.request.user)
        form.instance.author = profile
        return super(ArticleCreateView, self).form_valid(form)

    def get_success_url(self):
        return reverse('detail', args=(self.object.id,))

class ArticleDetailView(DetailView):
    model = Article
    template_name = 'article/detail.html'
    context_object_name = 'article'
    pk_url_kwarg = 'article_id'

class ArticleUpdateView(UpdateView):
    model = Article
    template_name = 'article/update.html'
    form_class = ArticleForm
    pk_url_kwarg = 'article_id'
    def get_success_url(self):
        return reverse('detail', args=(self.object.id,))

class ArticleDeleteView(DeleteView):
    model = Article
    template_name = 'article/delete.html'
    success_url = '/'
    pk_url_kwarg = 'article_id'

#class DisplayView(View):
    #template_name = 'news-and-events.html'
    #def get_queryset(self):
        #return Article.objects.all()