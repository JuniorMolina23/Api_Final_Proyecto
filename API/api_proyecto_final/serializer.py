from rest_framework import serializers

from .models import *

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ('id', 'nombre', 'apellidos', 'email','clave','estado','sexo','direccion','telefono','cargo_id')

class AlmacenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Almacen
        fields = ('id', 'nombre_almacen','estado_almacen','informacion','temperatura')

class CargosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cargos
        fields = ('id', 'nombre_cargo','estado_cargo')

class EPPSerializer(serializers.ModelSerializer):
    class Meta:
        model = EPP
        fields = ('id', 'nombre_epp','imagen','informacion_epp','almacen_id')

class Detalle_almacenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Detalle_almacen
        fields = ('id','fecha','almacen_id','temperatura','usuario_id')

class Detalle_TemperaturaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Detalle_Temperatura
        fields = ('id','almacen_id','temp_ini', 'temp_fin')