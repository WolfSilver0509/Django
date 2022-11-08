"""merchex URL Configuration

La liste `urlpatterns` achemine les URL vers les vues. Pour plus d'informations, veuillez consulter :
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Exemples:
Vues des fonctions
    1. Ajouter une importation : à partir des vues d'importation my_app
    2. Ajoutez une URL à urlpatterns : path('', views.home, name='home')
Vues basées sur les classes
    1. Ajouter une importation : depuis other_app.views import Home
    2. Ajoutez une URL à urlpatterns : path('', Home.as_view(), name='home')
Inclure une autre URLconf
    1. Importez la fonction include() : depuis django.urls import include, path
    2. Ajoutez une URL à urlpatterns : path('blog/', include('blog.urls'))

    path :
    Le premier argument est une chaîne de caractères. Il s'agit du chemin URL que nous allons faire correspondre : « about-us/ ».

    Le second argument doit être une fonction de vue que nous avons définie dans views.py. La demande sera transmise à cette vue, et la vue générera une page.
"""
from django.contrib import admin
from django.urls import path
from listings import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', views.hello),
    path('about-us/', views.about_us),
    path('listings/', views.listings),
    path('contact-us/', views.contact_us),
]
