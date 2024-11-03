from rest_framework import generics
from .models import Docente, NivelDocente, Pago, Curso, CursoDocente, Carrera, Modulo, Administrativo, Grupo, GrupoModulo, HorasClase, HorasClaseGrupoModulo, Alumno, Sesion, Recurso
from .serializers import DocenteSerializer, NivelDocenteSerializer, PagoSerializer, CursoSerializer, CursoDocenteSerializer, CarreraSerializer, ModuloSerializer, AdministrativoSerializer, GrupoSerializer, GrupoModuloSerializer, HorasClaseSerializer, HorasClaseGrupoModuloSerializer, AlumnoSerializer, SesionSerializer, RecursoSerializer

class DocenteList(generics.ListCreateAPIView):
    queryset = Docente.objects.all()
    serializer_class = DocenteSerializer

class DocenteDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Docente.objects.all()
    serializer_class = DocenteSerializer

class NivelDocenteList(generics.ListCreateAPIView):
    queryset = NivelDocente.objects.all()
    serializer_class = NivelDocenteSerializer

class NivelDocenteDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = NivelDocente.objects.all()
    serializer_class = NivelDocenteSerializer

class PagoList(generics.ListCreateAPIView):
    queryset = Pago.objects.all()
    serializer_class = PagoSerializer

class PagoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Pago.objects.all()
    serializer_class = PagoSerializer

class CursoList(generics.ListCreateAPIView):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer

class CursoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer

class CursoDocenteList(generics.ListCreateAPIView):
    queryset = CursoDocente.objects.all()
    serializer_class = CursoDocenteSerializer

class CursoDocenteDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = CursoDocente.objects.all()
    serializer_class = CursoDocenteSerializer

class CarreraList(generics.ListCreateAPIView):
    queryset = Carrera.objects.all()
    serializer_class = CarreraSerializer

class CarreraDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Carrera.objects.all()
    serializer_class = CarreraSerializer

class ModuloList(generics.ListCreateAPIView):
    queryset = Modulo.objects.all()
    serializer_class = ModuloSerializer

class ModuloDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Modulo.objects.all()
    serializer_class = ModuloSerializer

class AdministrativoList(generics.ListCreateAPIView):
    queryset = Administrativo.objects.all()
    serializer_class = AdministrativoSerializer

class AdministrativoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Administrativo.objects.all()
    serializer_class = AdministrativoSerializer

class GrupoList(generics.ListCreateAPIView):
    queryset = Grupo.objects.all()
    serializer_class = GrupoSerializer

class GrupoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Grupo.objects.all()
    serializer_class = GrupoSerializer

class GrupoModuloList(generics.ListCreateAPIView):
    queryset = GrupoModulo.objects.all()
    serializer_class = GrupoModuloSerializer

class GrupoModuloDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = GrupoModulo.objects.all()
    serializer_class = GrupoModuloSerializer

class HorasClaseList(generics.ListCreateAPIView):
    queryset = HorasClase.objects.all()
    serializer_class = HorasClaseSerializer

class HorasClaseDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = HorasClase.objects.all()
    serializer_class = HorasClaseSerializer

class HorasClaseGrupoModuloList(generics.ListCreateAPIView):
    queryset = HorasClaseGrupoModulo.objects.all()
    serializer_class = HorasClaseGrupoModuloSerializer

class HorasClaseGrupoModuloDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = HorasClaseGrupoModulo.objects.all()
    serializer_class = HorasClaseGrupoModuloSerializer

class AlumnoList(generics.ListCreateAPIView):
    queryset = Alumno.objects.all()
    serializer_class = AlumnoSerializer

class AlumnoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Alumno.objects.all()
    serializer_class = AlumnoSerializer

class SesionList(generics.ListCreateAPIView):
    queryset = Sesion.objects.all()
    serializer_class = SesionSerializer

class SesionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Sesion.objects.all()
    serializer_class = SesionSerializer

class RecursoList(generics.ListCreateAPIView):
    queryset = Recurso.objects.all()
    serializer_class = RecursoSerializer

class RecursoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Recurso.objects.all()
    serializer_class = RecursoSerializer
