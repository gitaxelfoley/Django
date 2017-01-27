from django.contrib import admin
from .models import Shoe



class ShoeModelAdmin(admin.ModelAdmin):
	list_display = ["brand", "type", "size", "price", "description"]
	list_display_links = ["brand"]
	list_filter = ["brand", "size", "price"]
	search_fields = ["brand", "size"]
	class Meta:
		model = Shoe

admin.site.register(Shoe,ShoeModelAdmin)
