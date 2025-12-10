from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView, DeleteView, CreateView, UpdateView
from blog_app.models import Record
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class RecordCreateView(LoginRequiredMixin, CreateView):
    model = Record
    fields = ['heading', 'main_info', 'preview', 'publication_attribute']
    template_name = 'blog/record_form.html'
    success_url = reverse_lazy('blog:record_list')

class RecordListView(ListView):
    model = Record
    template_name = 'blog/records.html'
    context_object_name = 'records'

    def get_queryset(self):
        return Record.objects.filter(publication_attribute=True)

class RecordDetailView(LoginRequiredMixin, DetailView):
    model = Record
    template_name = 'blog/record_detail.html'
    context_object_name = 'record'

    def get_object(self, queryset = None):
        obj = super().get_object(queryset)
        obj.viewers += 1
        obj.save()
        return obj

class RecordUpdateView(LoginRequiredMixin, UpdateView):
    model = Record
    fields = ['heading', 'main_info', 'preview', 'publication_attribute']
    template_name = 'blog/record_form.html'
    def get_success_url(self):
        return reverse_lazy('blog:record_detail', kwargs={'pk': self.object.pk})

class RecordDeleteView(LoginRequiredMixin, DeleteView):
    model = Record
    template_name = 'blog/record_confirm_delete.html'
    success_url = reverse_lazy('blog:record_list')