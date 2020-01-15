from django.urls import path, include
from myapp.views import index, CustomTemplateView, CustomListView

urlpatterns = [
    path('', CustomTemplateView.as_view(), name='index'),
    path('pers', CustomListView.as_view(), name='persons')
]