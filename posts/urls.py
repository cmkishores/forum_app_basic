from django.urls import path
from .views import UpdateView,DetailPostView

urlpatterns = [
	path('',UpdateView.as_view(),name='home'),
	path('detailed/<int:pk>/',DetailPostView.as_view(),name='detailed')
	]