from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, get_user_model
from .form import RegisterCustomerForm

User = get_user_model()

def register_customer(request):
    if request.method == 'POST':
        form = RegisterCustomerForm(request.POST)
        if form.is_valid():
            var = form.save(commit=False)
            var.is_customer = True
            var.username = var.email
            var.name = form.cleaned_data.get('name')  # Salvar o nome completo
            var.sector = form.cleaned_data.get('sector')        # Salvar o setor
            var.save()
            messages.success(request, 'Conta criada. Faça o login')
            return redirect('login')
        else:
            messages.warning(request, 'Algo deu errado. Preencha os dados corretamente')
            return redirect('register-customer')
    else:
        form = RegisterCustomerForm()
        context = {'form': form}
        print(context)
        return render(request, 'accounts/register_customer.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None and user.is_active:
            login(request,user)
            return redirect('dashboard')
        else:
            messages.warning(request,'Algo deu errado. Preecha os dados corretamente')
            return redirect('login')
    else:
        return render(request,'accounts/login.html')

def logout_user(request):
    logout(request)
    messages.success(request,'Sessão finalizada. Faça o login novamente para continuar')
    return redirect('login')
