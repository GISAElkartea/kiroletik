from django.views.generic import DetailView

from .models import Flatpage


class FlatpageDetail(DetailView):
    queryset = Flatpage.objects.published()
    context_object_name = 'flatpage'


flatpage_detail = FlatpageDetail.as_view()
