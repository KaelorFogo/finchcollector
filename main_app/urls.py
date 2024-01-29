from django.urls import path
from . import views
# routes

urlpatterns = {
  path('', views.home, name='Home'),
  path('about/', views.about, name="About"),
  path('finches/', views.finches_index, name="index"),
  path('finches/<int:finch_id>/', views.finches_detail, name='detail'),
}