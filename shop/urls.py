from django.urls import path
from . views import *

app_name = 'shop'

urlpatterns = [
    path('', index, name='index'),
    path('create/', create, name='create'),
    path("loguser", login_user, name="loguser"),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('signup/', signup, name='signup'),
    path('home/', home, name='home'),
    path('payment/success/', payment_success, name='payment_success'),
    path('payment/error/', payment_error, name='payment_error'),
    path('payment/cancel/', payment_cancel, name='payment_cancel'),
    path('catalog/', catalog_view, name='catalog'),
    path('games/<int:game_id>/info/', game_info, name='game_info'),
    path('developer/', developer_view, name='developer'),
    path('search/', search, name='search'),
    path('games/<int:game_id>/play/', play_game, name='play_game'),
    path('developer/publish/', publish_page_view, name='publish'),
    path('developer/publish_game/', create_game, name='publish_game'),
    path('developer/mygames/', developer_games, name='developer_games'),
    path('developer/games/<int:game_id>/edit/', edit_game, name='editgame'),
    path('developer/games/<int:game_id>/update/', edit_game_update, name='updategame'),
    path('developer/games/<int:game_id>/delete/', edit_game_delete, name='deletegame'),
    path('facebook/', facebook_handler, name='facebook_handler'),


]
