from django.urls import path, re_path
from django.views.generic import TemplateView
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from .views import *
from django.conf import settings
from django.conf.urls.static import static
from django.views.decorators.cache import cache_page

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView)


schema_view = get_schema_view(
    openapi.Info(
        title='Любой текст',
        default_version='v 0.0.1',
        description='Документация по API к ресурсу',
        terms_of_service='https://www.google.com/policies/terms',
        contact=openapi.Contact(email='demuratov12@gmail.com'),
        license=openapi.License(name='BSD License')
    ),
    public=True,
    permission_classes=[permissions.AllowAny, ]
)





urlpatterns = (
    # path('', index, name='index'),
    path('', Index.as_view(), name='index'),
    # path('category/<int:pk>/', category_list, name='category_list'),
    path('category/<int:pk>', ArticleByCategory.as_view(), name='category_list'),
    path('post/<int:pk>/', PostDetail.as_view(), name='post_detail'),
    path('add_article/', AddPost.as_view(), name='add'),
    path('post/<int:pk>/update', PostUpdate.as_view(), name='post_update'),
    path('post/<int:pk>/delete', Postdelet.as_view(), name='delete_post'),
    path('search/', SearchResult.as_view(), name='search'),
    path('password/', UserChangePassword.as_view(), name='change_password'),
    


    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('register/', register, name='register'),
    path('add_comment/<int:post_id>', add_comment, name='add_comment'),
    path('profile/<int:user_id>', profile, name='profile'),

    # API
    path('post/api', CookingAPI.as_view(), name='CookingAPI'),
    path('post/api/<int:pk>', CookingAPIDetail.as_view(), name='CookingAPIDetail'),
    path('categories/api/', CookingCategoryAPI.as_view(), name='CookingCategoryAPI'),
    path('categories/api/<int:pk>', CookingCategoryAPIDetail.as_view(), name='CookingCategoryAPIDetail'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),


    # Swagger
        path(
        "swagger-ui/",
        TemplateView.as_view(
            template_name="swagger/swagger_ui.html",
            extra_context={"schema_url": "openapi-schema"},
        ),
        name="swagger-ui",),

        re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=1), name='schema-json')


)

