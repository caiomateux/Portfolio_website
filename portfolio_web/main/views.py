from django.shortcuts import render
from django.contrib import messages
from .models import (
		UserProfile,
		Portfolio,
		Testimonial,
		ContactProfile
	)

from django.views import generic
from . forms import ContactForm


class IndexView(generic.TemplateView):
	template_name = "index.html"

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		
		testimonials = Testimonial.objects.filter(is_active=True)
		portfolio = Portfolio.objects.filter(is_active=True)
		context["testimonials"] = testimonials
		context["portfolio"] = portfolio
		return context


class ContactView(generic.FormView):
	template_name = "contact.html"
	form_class = ContactForm
	success_url = "/contact"
	
	def form_valid(self, form):
		form.save()
		messages.success(self.request, 'Thank you. We will be in touch soon.')
		return super().form_valid(form)


class PortfolioView(generic.ListView):
	model = Portfolio
	template_name = "portfolio.html"
	paginate_by = 10

	def get_queryset(self):
		return super().get_queryset().filter(is_active=True)


class PortfolioDetailView(generic.DetailView):
	model = Portfolio
	template_name = "portfolio-detail.html"
