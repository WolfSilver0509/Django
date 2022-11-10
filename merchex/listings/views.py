# Create your views here.
"""
Les vues sont des fonctions Python qui doivent remplir les critères suivants :

Le premier paramètre de la fonction est une variable contenant l'objetHttpRequest, et par convention nous le nommons toujours request. Cet objet contient certains attributs utiles liés à la demande. Nous les examinerons plus avant au chapitre Récupérez les données de l'utilisateur avec Django Forms.

La valeur de retour de la fonction est toujours un objetHttpResponse. Ce qu'il contient dépend du type d'application : dans notre application, nous allons placer du HTML dans nos réponses.

"""
from django.http import HttpResponse
from listings.models import Band
from listings.models import Title

from django.shortcuts import render

def hello(request):
    bands = Band.objects.all()
    return render(request, 'listings/hello.html', {'bands': bands})
#     return HttpResponse(f"""
#         <h1>Hello Django !</h1>
#         <p>Mes groupes préférés sont :<p>
#         <ul>
#             <li>{bands[0].name}</li>
#             <li>{bands[1].name}</li>
#             <li>{bands[2].name}</li>
#         </ul>
# """)


def about_us(request):
    return HttpResponse('<h1>About us</h1> <p>Here is the about us page</p>')

def listings(request):
    titles = Title.objects.all()
    return HttpResponse(f""" <h1>Listings</h1> <p>Here is the listings page</p>
                        <p>Mes groupes préférés sont :<p>
        <ul>
            <li>{titles[0].title}</li>
            <li>{titles[1].title}</li>
            <li>{titles[2].title}</li>
            <li>{titles[3].title}</li>
        </ul> """ )

def contact_us(request):
    return HttpResponse('<h1>Contact us</h1> <p>Here is the contact us page</p>')