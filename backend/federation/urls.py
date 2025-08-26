from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import LeadershipMemberViewSet, TeamMemberViewSet, DocumentViewSet, ContactListView

router = DefaultRouter()
router.register(r'leadership', LeadershipMemberViewSet)
router.register(r'team', TeamMemberViewSet)
router.register(r'documents', DocumentViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('contacts/', ContactListView.as_view(), name='contacts'),
]