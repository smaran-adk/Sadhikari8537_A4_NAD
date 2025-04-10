from django.urls import path 
from django.conf.urls.static import static
from django.conf import settings

from .views import(
    post_list_and_create,

    load_post_data_view,
    like_unlike_post,
    post_detail,
    post_detail_data_view,
    update_post,
    delete_post,
    


    
)

app_name = 'posts'

urlpatterns =[
    path('',post_list_and_create, name='main-board'),
    path('like-unlike/',like_unlike_post, name='like_unlike'),
    path('<pk>/', post_detail, name='post-detail'),
    path('<pk>/update/', update_post, name='post-update'),
    path('<pk>/delete/', delete_post, name='post-delete'),


    path('data/<int:num_posts>/', load_post_data_view, name='posts-data'),
    path ('<pk>/data/', post_detail_data_view, name= 'post-detial-data'),
    
    
    
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)