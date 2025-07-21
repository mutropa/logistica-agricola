from rest_framework import serializers
from core.models import User, Produtor, Comprador, Transportador

class RegistarSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'tipo']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
            tipo=validated_data['tipo']
        )

      
        if user.tipo == 'produtor':
            Produtor.objects.create(user=user)
        elif user.tipo == 'comprador':
            Comprador.objects.create(user=user)
        elif user.tipo == 'transportador':
            Transportador.objects.create(user=user)

        return user
