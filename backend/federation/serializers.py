from rest_framework import serializers
from .models import LeadershipMember, TeamMember, Document, Contact

class LeadershipMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = LeadershipMember
        fields = '__all__'

class TeamMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeamMember
        fields = '__all__'

class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = '__all__'

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'