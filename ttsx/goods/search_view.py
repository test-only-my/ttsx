# views.py

from haystack.generic_views import SearchView


class MySearchView(SearchView):
    """My custom search view."""
    def get_context_data(self, *args, **kwargs):
        print('------------------------')
        context = super(MySearchView, self).get_context_data(*args, **kwargs)
        # do something
        page_obj = context['page_obj']
        if page_obj.paginator.num_pages <= 5:
            index_list = page_obj.paginator.page_range
        elif page_obj.number <= 2:
            index_list = range(1,5+1)
        elif page_obj.paginator.num_pages - page_obj.number <= 2:
            index_list = page_obj.paginator.page_range[-5:]
        else:
            index_list = range(page_obj.number - 2, page_obj.number + 3)

        context['index_list'] = index_list
        context['logo_search'] = 1
        context['head'] = 1
        return context

