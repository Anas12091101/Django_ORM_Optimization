from django.contrib import admin
from django.urls import path, include
from blog.views import (
    bad_query_foreign_key, good_query_foreign_key,
    bad_query_aggregation, good_query_aggregation,
    bad_query_filtering, good_query_filtering,
    bad_query_many_to_many, good_query_many_to_many,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('bad-query-foreign-key/', bad_query_foreign_key, name='bad_query_foreign-key'),
    path('good-query-foreign-key/', good_query_foreign_key, name='good_query_foreign_key'),
    
    path('bad-query-aggregation/', bad_query_aggregation, name='bad_query_aggregation'),
    path('good-query-aggregation/', good_query_aggregation, name='good_query_aggregation'),

    path('bad-query-filtering/', bad_query_filtering, name='bad_query_filtering'),
    path('good-query-filtering/', good_query_filtering, name='good_query_filtering'),

    path('bad-query-many-to-many/', bad_query_many_to_many, name='bad_query_many_to_many'),
    path('good-query-many-to-many/', good_query_many_to_many, name='good_query_many_to_many'),

    path('silk/', include('silk.urls', namespace='silk')),
]
