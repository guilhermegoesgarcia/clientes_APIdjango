from rest_framework import serializers
from clientes.models import Cliente
from clientes.validators import *

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'
    def validate(self,data):
        if not nome_valido(data['nome']):
            raise serializers.ValidationError({'nome':'Não incluir numeros nesse campo'})
        if not cpf_valido(data['cpf']):
            raise serializers.ValidationError({'cpf':'O CPF deve ter 11 dígitos'})
        if not rg_valido(data['rg']):
            raise serializers.ValidationError({'rg':'O Rg deve conter 9 dígitos'})
        if not celular_valido(data['celular']):
            raise serializers.ValidationError({'celular':'O celular deve ter o seguinte modelo 11 91111-9999, respeitando os espassos e traços'})
        return data


