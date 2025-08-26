from rest_framework import viewsets, generics
from .models import LeadershipMember, TeamMember, Document, Contact
from .serializers import LeadershipMemberSerializer, TeamMemberSerializer, DocumentSerializer, ContactSerializer

class LeadershipMemberViewSet(viewsets.ModelViewSet):
    queryset = LeadershipMember.objects.all()
    serializer_class = LeadershipMemberSerializer

class TeamMemberViewSet(viewsets.ModelViewSet):
    queryset = TeamMember.objects.all()
    serializer_class = TeamMemberSerializer

class DocumentViewSet(viewsets.ModelViewSet):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer

class ContactListView(generics.ListAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer