from django.contrib.auth import update_session_auth_hash

from rest_framework import serializers

from authentication.models import Account

class AccountSerializer(serializers.ModelSerializer):
	password = serializers.CharField(write_only=True, required=False)
	confirm_password = serializers.CharField(write_only=True, required=False)

	class Meta:
		model = Account
		fields = ('id', 'email', 'username', 'created_at', 'updated_at',
				  'first_name', 'last_name', 'tagline', 'password', 'confirm_password',)
		read_only_fields = ('created_at', 'updated_at',)

		def create(self, validated_data):
			# Convert JSON into a Python object.  This is called deserialization.

			return Account.objects.create(**validated_data)

		def update(self, instance, validated_data):
			# Convert JSON into a Python object.  This is called deserialization

			instance.username = validated_data.get('username', instance.username)
			instance.tagline = validated_data.get('tagline', instance.tagline)

			instance.save()

			password = validated_data.get('password', None)
			confirm_password = validated_data.get('confirm_password', None)

			# NOTE: Below password validation NOT RECOMMENDED in a Real-World System Architecture
			if password and confirm_password and password == confirm_password:
				instance.set_password(password)

				# NOTE: We must explicitly save the model after updating the password
				instance.save()

			# When a User's password is updated, their session authentication hash must be explicitly updated.
			# 	If we don't do this here, the user will not be authenticated on their next request,
			#	and would have to to login again.
			update_session_auth_hash(self.context.get('request'), instance)

			return instance