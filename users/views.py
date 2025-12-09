import os

from dotenv import load_dotenv
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.core.mail import send_mail

from .forms import CustomUserCreationForm


# Create your views here.
load_dotenv(override=True)

class RegisterView(CreateView):
    template_name = 'user/register.html'
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('catalog:home')

    def form_valid(self, form):
        user = form.save()
        self.send_welcome_email(user.email)
        return super().form_valid(form)

    def send_welcome_email(self, user_email):
        subject = "Добро пожаловать на наш сервис"
        message = "Спасибо за регистрацию"
        from_email = os.getenv('EMAIL')
        recipient_list = [user_email, ]
        send_mail(subject, message, from_email, recipient_list)