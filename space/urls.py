from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.message_list, name='message_list'),
    url(r'^api/mark_read$', views.mark_read, name='message_id'),
    url(r'^False$', views.mark_all_not_read, name='message_id'),
    url(r'^json$', views.json_out_all_messages, name='json_out_all_message'),
    url(r'^api/get_messages$', views.json_out_new_messages, name='json_out_new_messages'),
]
