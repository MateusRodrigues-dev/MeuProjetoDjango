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

def status_view(request):
    context = {'id_servidor': ServidorAlpha01 ,'status_sistema': Operacional }

        return render(request, 'status.html' , context)


