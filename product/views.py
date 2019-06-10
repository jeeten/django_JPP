# from .models import user
from django import forms

from django.shortcuts import render, HttpResponse, redirect
from .models import Product
from django.utils import timezone
from django.views import generic
from django.template import loader
# from django.contrib.auth.model import Use
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login


# Create your views here.


def getProductDetails(request):
    template = loader.get_template('index.html')
    Data = Product.objects.select_related(
        'brandid').select_related('categoryid').all()[:10]

    # output = ', '.join([q for q in Data])

    # logger.debug('DSomething went wrong!')
    # logger.info('ISomething went wrong!')
    # logger.warning('WSomething went wrong!')
    # logger.error('ESomething went wrong!')
    # logger.critical('CriSomething went wrong!')

    # logger.error('Something went wrong!')
    # return HttpResponse(output)

    return HttpResponse(template.render())
    # return HttpResponse(content=Data,content_type="text/html")


class ProductListView(generic.ListView):
    # model = Product
    # context_object_name = 'my_product_list'
    # queryset = Product.objects.all().limit(5)
    # template_name = 'books/my_arbitrary_template_name_list.html'

    model = Product
    # paginate_by = 5  # if pagination is desired
    # context_object_name = 'my_product_list'
    queryset = Product.objects.select_related(
        'brandid').select_related('categoryid').all()[:10]
    # template_name = 'books/my_arbitrary_template_name_list.html'

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['now'] = timezone.now()
    #     return context


def register(request):
    if request.method == "POST":
        # data = request.DATA
        username = request.POST.get('Username')
        data = {"userName": username}

        return HttpResponse(content=data, content_type="text/json")
        # password = request.data['password']
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            pwd = form.changed_data.get("password")

            user = authenticate(username=username, password=pwd)
            login(request, user)
            return redirect('home')
        else:
            form = UserCreationForm()
            return render(request, 'signup.html', {'form': form})
            # return redirect('login')
