from django.urls import path

from polls import views

app_name = 'polls'
urlpatterns = [
	path('', views.index, name='index'),
        path('inputPage/', views.input, name='input'),
        path('productInput/',views.productinput,name='productInput'),
        path('query/',views.query,name='query'),
        path('<int:order_id>/', views.detail, name='detail'),
        path('<int:order_id>/results/', views.results, name='results'),
        path('<int:order_id>/vote/', views.vote, name='vote'),
]