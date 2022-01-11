from django.urls import path
from.views import home,view1,view2,view3,somme
urlpatterns=[
    path('',home,name='home'),
    path('view1',view1,name='view1'),
    path('view2',view2,name='view2'),
    path('view3',view3,name='view3'),
    path('somme',somme,name='somme'),
]