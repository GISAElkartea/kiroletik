from banners.models import Banner
from flatpages.models import Flatpage


def main_processor(request):
    return {
        'banner': Banner.objects.active(),
        'flatpages': Flatpage.objects.published(),
    }
