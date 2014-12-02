from banners.models import Banner
from flatpages.models import Flatpage
from widgets.models import Widget


def main_processor(request):
    return {
        'banner': Banner.objects.active(),
        'flatpages': Flatpage.objects.published(),
        'widgets': Widget.objects.active(),
    }
