# views.py
from datetime import date

from haystack.generic_views import SearchView

class MySearchView(SearchView):
    """My custom search view."""
    def get_context_data(self, *args, **kwargs):
        context = super(MySearchView, self).get_context_data(*args, **kwargs)
        # do something
        context['logo_search'] = 1
        context['head'] = 1
        return context

