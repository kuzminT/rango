from django.conf.urls import url
from . import views
from registration.backends.simple.views import RegistrationView

# app_name = 'rango'

# app_name = 'rango'


class MyRegistrationView(RegistrationView):
    # def get_success_url(self, user):
    #     # return '/rango/'
    #     return url('register_profile')

    success_url = 'register_profile'


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^about/', views.about, name='about'),
    url(r'^add_category/$', views.add_category, name="add_category"),
    url(r'^category/(?P<category_name_slug>[\w\-]+)/$', views.show_category, name='category'),
    url(r'^category/(?P<category_name_slug>[\w\-]+)/add_page/$', views.add_page, name='add_page'),
    # url(r'^register/$',
    #     views.register,
    #     name='register'),
url(r'^register/$',
        MyRegistrationView.as_view(),
        name='registration_register'
        ),
    url(r'^register_profile/$', views.register_profile, name='register_profile'),
    url(r'^login/$', views.user_login, name='login'),
    url(r'^logout/$', views.user_logout, name='logout'),
    url(r'restricted/', views.restricted, name='restricted'),
    url(r'^profile/(?P<username>[\w\-]+)/$', views.profile, name='profile'),
    url(r'^profiles/$', views.list_profiles, name='list_profiles')
]

