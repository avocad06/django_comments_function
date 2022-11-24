"""curd_comments URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
# 이미지 파일 - 사용자가 업로드한 파일의 url를 가져오기 위해서
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('articles/', include("articles.urls")),
    path('accounts/', include("accounts.urls")),
    path('', include("core.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# 업로드된 파일의 URL == settings.`MEDIA_URL`
# 위 URL을 통해 참조하는 `파일의 실제 위치` == settings.MEDIA_`ROOT`

# 사용자가 업로드한 파일이 프로젝트 폴더에 업로드 되지만,
# 우리가 사용자에게 제공하기 위해서는 업로드된 파일의 경로로부터 만들어진 URL이 필요하다.