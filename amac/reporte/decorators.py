from django.core.exceptions import PermissionDenied

def es_planificador(func):
    def wrap(request, *args, **kwargs):
        if request.user.is_authenticated and request.user.rol.nombre == 'Planificador':
            return func(request, *args, **kwargs)
        raise PermissionDenied
    return wrap
 
def es_operario(func):
    def wrap(request, *args, **kwargs):
        if request.user.is_authenticated and request.user.rol.nombre == 'Operario':
            return func(request, *args, **kwargs)
        raise PermissionDenied
    return wrap

def es_admin(func):
    def wrap(request, *args, **kwargs):
        if request.user.is_authenticated and request.user.rol.nombre == 'Administrador':
            return func(request, *args, **kwargs)
        raise PermissionDenied
    return wrap
