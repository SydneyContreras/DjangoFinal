from django.shortcuts import render, redirect, get_object_or_404
from django.template.response import TemplateResponse, HttpResponse
from django.views.generic import DetailView
from project_app.models import appointments
from .forms import appointmentForm
from django.http import HttpResponse
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.views.generic.list import ListView





class AppointmentsDetailView(DetailView):
    template_name = 'appointment_files/view_appointment.html'
    model = appointments
    
def appoint_remove(request, pk):
    appointments_model = get_object_or_404(appointments, pk=pk)
    appointments_model.delete()
    return redirect('view')
  
def index(request):
    return render(request, 'appointment_files/index.html')

def appointment(request):
    return render(request, 'appointment_files/appointment.html')

class appointmentListView(ListView):
    template_name = 'appointment_files/view.html'
    model = appointments
    paginate_by = 5
    context_object_name = 'data'
    
class CreatePostView(CreateView):
    model = appointments
    form_class = appointmentForm
    template_name = 'appointment_files/appointments_form.html'
    success_url = reverse_lazy('view')

    def form_valid(self, form):
        response = super().form_valid(form)
        return response

    def form_invalid(self, form):
        response = super().form_invalid(form)
        return response
