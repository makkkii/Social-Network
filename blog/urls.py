from django.conf.urls import url
from blog import views

urlpatterns = [
    url(r'^$', views.PostListView.as_view(), name='post_list'),
    url(r'^post/(?P<pk>\d+)$', views.PostDetailView.as_view(), name='post_detail'),
    url(r'^post/new/', views.PostCreateView.as_view(), name='post_new'),
    url(r'^post/(?P<pk>\d+)/edit/', views.PostUpdateView.as_view(), name='post_edit'),
    url(r'^post/(?P<pk>\d+)/remove/', views.PostDeleteView.as_view(), name='post_remove'),
    url(r'^drafts/', views.DraftListView.as_view(), name='post_drafts_list'),
    url(r'^about/$', views.AboutView.as_view(), name='about'),
]