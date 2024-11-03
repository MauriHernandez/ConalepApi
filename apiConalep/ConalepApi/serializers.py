from rest_framework import serializers
from .models import Docente, NivelDocente, Pago, Curso, CursoDocente, Carrera, Modulo, Administrativo, Grupo, GrupoModulo, HorasClase, HorasClaseGrupoModulo, Alumno, Sesion, Recurso

class DocenteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Docente
        fields = '__all__'

class NivelDocenteSerializer(serializers.ModelSerializer):
    class Meta:
        model = NivelDocente
        fields = '__all__'

class PagoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pago
        fields = '__all__'

class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = '__all__'

class CursoDocenteSerializer(serializers.ModelSerializer):
    class Meta:
        model = CursoDocente
        fields = '__all__'

class CarreraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carrera
        fields = '__all__'

class ModuloSerializer(serializers.ModelSerializer):
    class Meta:
        model = Modulo
        fields = '__all__'

class AdministrativoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Administrativo
        fields = '__all__'

class GrupoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Grupo
        fields = '__all__'

class GrupoModuloSerializer(serializers.ModelSerializer):
    class Meta:
        model = GrupoModulo
        fields = '__all__'

class HorasClaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = HorasClase
        fields = '__all__'

class HorasClaseGrupoModuloSerializer(serializers.ModelSerializer):
    class Meta:
        model = HorasClaseGrupoModulo
        fields = '__all__'

class AlumnoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alumno
        fields = '__all__'

class SesionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sesion
        fields = '__all__'

class RecursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recurso
        fields = '__all__'
