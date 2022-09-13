from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from Main.forms import NoteCreationForm, NoteEditForm, UserRegistrationForm
from .models import Note

class LoginUser(LoginView):
    template_name = 'login_page.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('home_page')

class RegisterUser(FormView):
    template_name = 'register_page.html'
    form_class = UserRegistrationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('home_page')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegisterUser, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('tasks')
        return super(RegisterUser, self).get(*args, **kwargs)

class HomePage(LoginRequiredMixin, ListView):
    model = Note
    context_object_name = 'notes'
    template_name = 'home_page.html'
    ordering = ['-last_updated']
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['notes'] = context['notes'].filter(user=self.request.user)
        search_input = self.request.GET.get('search_area') or ''
        if search_input:
            context['notes'] = context['notes'].filter(note_title__icontains=search_input)

        context['search_input'] = search_input
        return context

class DeleteNote(DeleteView):
    model = Note
    context_object_name = 'note'
    template_name = 'delete_confirmation.html'
    success_url = reverse_lazy('home_page')

class ViewNote(LoginRequiredMixin, UpdateView):
    model = Note
    form_class = NoteCreationForm
    context_object_name = 'note'
    template_name = 'view_note.html'
    success_url = reverse_lazy('home_page')

class CreateNote(LoginRequiredMixin, CreateView):
    model = Note
    form_class = NoteCreationForm
    template_name = 'create_note.html'
    success_url = reverse_lazy('home_page')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(CreateNote, self).form_valid(form)