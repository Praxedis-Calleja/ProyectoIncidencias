from django.http import HttpResponse
from .models import Usuarios  # usa el nombre exacto que generó inspectdb


def ping(request):
    return HttpResponse("✅ Django responde OK")

def prueba_bd(request):
    u = Usuarios.objects.first()
    return HttpResponse(f"Primer usuario: {getattr(u, 'nombre', '—')}") if u else HttpResponse("No hay usuarios.")
