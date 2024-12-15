from django.shortcuts import render

def es_planificador(func):
    def wrap(request, *args, **kwargs):
        if request.user.is_authenticated and request.user.rol.nombre == 'Planificador':
            return func(request, *args, **kwargs)
        return render(request, '403.html', status=403)  
    return wrap

def es_operario(func):
    def wrap(request, *args, **kwargs):
        if request.user.is_authenticated and request.user.rol.nombre == 'Operario':
            return func(request, *args, **kwargs)
        return render(request, '403.html', status=403)  
    return wrap

def es_admin(func):
    def wrap(request, *args, **kwargs):
        if request.user.is_authenticated and request.user.rol.nombre == 'Administrador':
            return func(request, *args, **kwargs)
        return render(request, '403.html', status=403) 
    return wrap

