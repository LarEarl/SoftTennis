from django.contrib import admin
from .models import LeadershipMember, TeamMember, Document, Contact

admin.site.register(LeadershipMember)
admin.site.register(TeamMember)
admin.site.register(Document)
admin.site.register(Contact)