from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('create/', views.createView, name='create'),
    path('edit/<int:id>', views.edit,),
    path('delete/<int:id>', views.deleteView,),
    path('signup/', views.signupView,),
    path('login/', views.loginView, ),
    path('employecreate/', views.employeView, ),
    # path('search/', views.search, ),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
