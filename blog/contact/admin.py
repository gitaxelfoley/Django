from django.contrib import admin
from .models import Contact



class ContactModelAdmin(admin.ModelAdmin):
	list_display = ["email", "text", "date"]
	list_display_links = ["email"]
	list_filter = ["email", "text"]
	search_fields = ["text", "email"]
	class Meta:
		model = Contact

admin.site.register(Contact,ContactModelAdmin)
