from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout

from djangoblog.models import Blog


class IndexView(generic.ListView):
    template_name = 'djangoblog/blog/index.html'
    context_object_name = 'last_post_list'

    def get_queryset(self):
        return Blog.objects.order_by('-posted')[:5]

class DetailView(generic.DetailView):
    model = Blog
    template_name = 'djangoblog/blog/detail.html'

    


def login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            # Redirect to a success page.
        else:
            # Return a 'disabled account' error message
            ...
    else:
        # Return an 'invalid login' error message.
        ...

def logout_view(request):
    logout(request)
    # Redirect to a success page.

