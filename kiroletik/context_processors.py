from banners.models import Banner
from flatpages.models import Flatpage
from widgets.models import Widget
from sports.models import Sport


def main_processor(request):
    return {
        'sports': Sport.objects.all(),
        'banner': Banner.objects.active(),
        'flatpages': Flatpage.objects.published(),
        'widgets': Widget.objects.active(),
    }
