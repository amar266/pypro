# Create your views here.
from django.views.generic import ListView
from contacts.models import Contact
from django.core.urlresolvers import reverse
from django.views.generic import CreateView
from django.views.generic import UpdateView

class ListContactView(ListView):
        
      model = Contact
      template_name = 'contact_list.html'

class CreateContactView(CreateView):
      model = Contact
      template_name = 'add_contact.html'
    
      def get_success_url(self):
         return reverse('contact-list')
class UpdateContactView(UpdateView):

      model = Contact
      template_name = 'add_contact.html' 
       
      def get_success_url(self):
          return reverse('contact-list')


      

