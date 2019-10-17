from django.urls import path
from django.views.generic import TemplateView

from URLShortner.views import MiniURLView, RedirectURLView

urlpatterns = [
    # ex: /urlshortner/
    path('', TemplateView.as_view(template_name='URLShortner/home.html'), name='home'),
    # ex: /urlshortner/home/
    path('home/', TemplateView.as_view(template_name='URLShortner/home.html'), name='home'),
    # ex: /urlshortner/mini/
    path('mini', MiniURLView.as_view()),
    # ex: /urlshortner/1lUUE
    path('<miniURL>', RedirectURLView.as_view()),
]