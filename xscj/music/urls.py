from django.urls import path
from . import views

urlpatterns=[
    path("musichome",views.musichome,name='musichome'),
    path('<int:music_id>', views.musicdetail, name='musicdetail'),
    path('<int:music_id>/createmusicreview', views.createmusicreview, name='createmusicreview'),
    path('review/<int:review_id>', views.updatemusicreview, name='updatemusicreview'),
    path('review/<int:review_id>/delete', views.deletemusicreview, name='deletemusicreview'),
]