from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.views import View

# def index(request, pid):
#     pizza = Pizza.objects.get(id=pid)
#     return HttpResponse(
#         content={
#             'id': pizza.id,
#             'title': pizza.title,
#             'description': pizza.description,
#         }
#     )


class SignupView(View):
    template_name = 'signup.html'
    def post(self, request):
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username,password=password)
            login(request, user)
            return redirect('/')
    def get(self, request):
        return render(request, self.template_name, {'form':
        UserCreationForm()})
