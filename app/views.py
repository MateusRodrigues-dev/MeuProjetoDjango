from django.shortcuts import render

def home_view(request):
    context = { 'nome_empresa': Google

    }
    return render(request,'home.html', context)

def perfil_view(request):
    context = {
        'nome_funcionario': Mateus , 'cargo': ProgramadorJúnior , 'setor': Desenvolvimento 

    },

    return render(request, 'perfil.html', context)