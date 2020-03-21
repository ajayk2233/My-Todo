from django.urls import path
from . import views
app_name='todo'
urlpatterns = [
# Todo List Operations
    path('',views.show,name='show'),
    path('<int:id>/',views.show,name='show'),
    path('search/<str:search>/',views.show,name='search'),
    path('details/<int:pk>/',views.Details.as_view(),name='details'),
    path('create/',views.Create.as_view(),name='create'),
    path('update/<int:pk>',views.Update.as_view(),name='update'),
    path('delete/<int:pk>/',views.Delete.as_view(),name='delete'),
    path('export/',views.export,name='export'),
]