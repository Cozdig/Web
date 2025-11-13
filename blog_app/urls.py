from django.urls import path
from blog_app.apps import BlogAppConfig
from blog_app.views import RecordListView, RecordDetailView, RecordCreateView, RecordDeleteView, RecordUpdateView

# from blog_app.views import

app_name = BlogAppConfig.name

urlpatterns = [
    path('', RecordListView.as_view(), name="record_list"),
    path('create/', RecordCreateView.as_view(), name="record_create"),
    path('<int:pk>/', RecordDetailView.as_view(), name="record_detail"),
    path('edit/<int:pk>/edit/', RecordUpdateView.as_view(), name="record_edit"),
    path('<int:pk>/delete/', RecordDeleteView.as_view(), name="record_delete"),
]
