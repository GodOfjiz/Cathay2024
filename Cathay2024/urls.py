"""
https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import include, path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",include("RemoteDatabase.urls")),
    path('api-auth/', include('rest_framework.urls')),
    path('ken_api/', views.hello_world, name='testing'),
    path('ken_api/activity/', views.activity_seeking, name='activity'),
    path('ken_api/route/', views.route_optimize, name='route'),
    #path('ken_api/tickets/', views.tickets_get, name='tickets',
    path('chatbot_chatting/', views.chatbotting, name='chatbot')
]
