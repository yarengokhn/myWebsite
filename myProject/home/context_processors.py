
from home.models import Settings


def global_settings(request):
    
    settings = Settings.objects.get(pk=1)
    return {
        'settings': settings
    }