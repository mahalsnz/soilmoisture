from django.urls import path
from django.conf.urls import url
from django.views.generic import TemplateView
from .views import SiteReadingsView, UploadReadingsFileView, SeasonWizard, OnsiteCreateView, SiteAutocompleteView
from . import views
from .forms import SelectCropRegionSeasonForm, CreateSeasonStartEndForm, CreateRefillFullPointForm, SiteSelectionForm

from .apiviews import ReportList, ReportDetail, SeasonList, SeasonDetail, ReadingTypeList, ReadingTypeDetail \
, FarmList, FarmDetail, ReadingDetail, ReadingList, SiteReadingList, SiteList, SiteDetail

FORMS = [("select_crsf", SelectCropRegionSeasonForm)]

urlpatterns = [
    path('', views.index, name='home'),
    path('sw.js', (
        TemplateView.as_view(
            template_name="sw.js",
            content_type='application/javascript')), name='sw.js'),
    # Reports
    path('reports', views.report_home, name='report_home'),
    path("reports/season_dates", views.report_season_dates, name='report_season_dates'),
    path("reports/missing_reading_types", views.report_missing_reading_types, name='report_missing_reading_types'),
    path("reports/no_meter_reading", views.report_no_meter_reading, name='report_no_meter_reading'),

    path('readings/site/', SiteReadingsView.as_view(), name='site_readings'),
    path('upload_readings_file/', UploadReadingsFileView.as_view(), name='upload_readings_file'),
    path('season_wizard/', SeasonWizard.as_view(FORMS), name='season_wizard'),

    path("vsw_percentage/<int:site_id>/<isodate:date>/", views.vsw_percentage),

    path('readings/onsite/', OnsiteCreateView.as_view(), name='onsite_readings'),
    path('autocomplete_sitenumber', SiteAutocompleteView.as_view(), name='autocomplete_sitenumber'),


    # API
    path("api/report/", ReportList.as_view(), name="reports_list"),
    path("api/report/<int:pk>/", ReportDetail.as_view(), name="reports_detail"),
    path("api/season/", SeasonList.as_view(), name="seasons_list"),
    path("api/season/<int:pk>/", SeasonDetail.as_view(), name="seasons_detail"),
    path("api/reading_type/", ReadingTypeList.as_view(), name="reading_types_list"),
    path("api/reading_type/<int:pk>/", ReadingTypeDetail.as_view(), name="reading_types_detail"),
    path("api/farm/", FarmList.as_view(), name="farms_list"),
    path("api/farm/<int:pk>/", FarmDetail.as_view(), name="farms_detail"),
    path("api/site/", SiteList.as_view(), name="sites_list"),
    path("api/site/<int:pk>/", SiteDetail.as_view(), name="sites_detail"),
    path("api/reading/", ReadingList.as_view(), name="readings_list"),
    path("api/reading/<int:pk>/", ReadingDetail.as_view(), name="readings_detail"),
    path("api/site_reading/<int:pk>/", SiteReadingList.as_view(), name="graph_data"),

    #ajax
    path('ajax/load-sites/', views.load_sites, name='ajax_load_sites'),
    path('ajax/load-site-readings/', views.load_site_readings, name='ajax_load_site_readings'),
    path('ajax/load-graph/', views.load_graph, name='ajax_load_graph'),
    path('ajax/process-site-note/', views.process_site_note, name='ajax_process_site_note'),
    path('ajax/process-reading-recommendation/', views.process_reading_recommendation, name='ajax_process_reading_recommendation'),
    path('ajax/load-onsite-reading/', views.load_onsite_reading, name='ajax_load_onsite_reading'),
    path('ajax/process-onsite-reading/', views.process_onsite_reading, name='ajax_process_onsite_reading'),
]
