from django.shortcuts import render , redirect
from order.models import Order
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from order.form import OrderForm
from django.urls import reverse


# Create your views here.
class OrderView(ListView):
    model = Order
    template_name = 'index.html'
    context_object_name = 'orders'

    def get_queryset(self):
        return Order.objects.all()

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(OrderView, self).get_context_data()
        return context

class OrderCreateView(CreateView):
    model = Order
    template_name = 'order/reservation.html'
    context_object_name = 'order'
    form_class = OrderForm

    def get_success_url(self):
        return reverse('order_detail', args=(self.object.id,))

class OrderUpdateView(UpdateView):
    model = Order
    template_name = 'order/update.html'
    form_class = OrderForm
    pk_url_kwarg = 'order_id'

    def get_success_url(self):
        return reverse('detail', args=(self.object.id,))

class OrderDeleteView(DeleteView):
        model = Order
        template_name = 'order/delete.html'
        success_url = '/'
        pk_url_kwarg = 'order_id'

class OrderDetailView(DetailView):
    model = Order
    template_name = 'order/detail.html'
    context_object_name = 'order'
    pk_url_kwarg = 'order_id'

