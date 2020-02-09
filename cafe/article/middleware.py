from django.urls import reverse
from django.shortcuts import redirect
#middleware створений для перевірики чи залог кор перед створенням статті
class LoginRequiredMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        #Запуск і ініціалізація
    def __call__(self, request):
        response = self.get_response (request)
        path = request.path_info
        article_create_path = reverse('create')
        if not request.user.is_authenticated and path == article_create_path:
            return redirect(reverse('login'))
        return response
