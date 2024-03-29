from django.contrib import admin
from django.urls import path, include
import portfolio.views
import blogapp.views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', blogapp.views.home, name="home"),
    path('blog/', include('blogapp.urls')),
    path('portfolio/', portfolio.views.portfolio, name="portfolio"),
    path('account/', include('account.urls')),
    path('faker/', blogapp.views.faker, name="faker"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)