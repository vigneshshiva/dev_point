from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path,include
from dev_dev import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('custom_user_model.urls')),
    path('accounts/',include('allauth.urls')),
    # path('modal',views.modal),
    path('',views.intro),
    path('home',views.home,name='home'),
    path('ask',views.ask_question_view),
    path('question_view',views.question_view),
    path('detail_url/<int:pk>',views.detail_url_view),
    path('answer',views.answer_question_view),
    path('like',views.like),
    path('answer_list',views.answer_list),
    path('comment',views.comment_view),
    path('like_count',views.like_count),
    path('comment_list_view',views.question_comment_list),
    path('email',views.pacchaiamman),
]
# +static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
# path('answer_like',views.answer_like),
# path('ckeditor',include('ckeditor_uploader.urls')),
