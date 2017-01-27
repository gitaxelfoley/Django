from django.conf.urls import url
from .views import (
	shoe_list,
	shoe_adidas,
	shoe_nike,
	shoe_puma,
	shoe_detail,
	)

urlpatterns = [
	url(r'^$', shoe_list, name='shoe'),
	url(r'^(?P<shoe_id>[0-9]+)/$', shoe_detail, name='shoe_id'),
	url(r'^adidas/$', shoe_adidas, name='adidas'),
	url(r'^nike/$', shoe_nike, name='nike'),
	url(r'^puma/$', shoe_puma, name='puma'),

]
