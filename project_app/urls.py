from django.urls import path
from . import views
from project_app.views import AppointmentsDetailView # Assuming AppointmentsDetailView is the correct class name

urlpatterns = [
    path('', views.index, name='index'),
    path('appointment/', views.appointment, name='appointment'),
    path('view/', views.appointmentListView.as_view(), name='view'),
    path('appointmentsdetail/<int:pk>/', AppointmentsDetailView.as_view(), name='appointmentsdetail'),
    path('post/new/', views.CreatePostView.as_view(), name='post_new'),
    path('view/<int:pk>/remove/', views.appoint_remove, name='appoint_remove'),
]
