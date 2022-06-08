from django.urls import path
from properties import views

urlpatterns = [
    path('categories/', views.PropertyCategoryListCreateView.as_view(), name="property-category-list"),
    path('categories/<slug:cat_key>/', views.PropertyCategorySlugRetrieveView.as_view(), name="property-category-slug-list"),
    path('create/', views.PropertyListCreateView.as_view(), name="property-cteate"),
    path('list-by-agent/', views.PropertyListByAgentView.as_view(), name="property-list-by-agent"),
    path('<int:pk>/detail/', views.PropertyRetrieveDestroyAPIView.as_view(), name="property-detail"),
    path('<int:pk>/update/', views.PropertyUpdateAPIView.as_view(), name="property-update"),
    path('housetypes/', views.HouseTypeListCreateView.as_view(), name="house-type-list"),
    path('buildingtypes/', views.BuildingTypeListCreateView.as_view(), name="building-type-list"),
    path('image/create/', views.PropertyImageListCreateView.as_view(), name="property-image-create"),
    path('image/<int:pk>/delete/', views.PropertyImageRetrieveUpdateDestroy.as_view(), name="property-image-delete"),
    path('video/create/', views.PropertyVideoListCreateView.as_view(), name="property-video-create"),
    path('video/<int:pk>/delete/', views.PropertyVideoRetrieveUpdateDestroy.as_view(), name="property-video-delete"),
    path('file/labels/', views.PropertyFileLabelListCreateView.as_view(), name="property-file-label-list"),
    path('file/<int:pk>/update/', views.PropertyImageRetrieveUpdateDestroy.as_view(), name="property-image-update"),

    #EDUCATION FACILITY

    path('edufa/search/', views.EducationFacilitySearchView.as_view(), name="edufa-search"),
    path('edufalevel/list/', views.EduFaLevelListView.as_view(), name="edufalevel-list"),
    path('<int:pk>/edufa/create/', views.EducationFacilityListCreateView.as_view(), name="edufa-create"),
    path('<int:pk>/edufa/create-from-search/', views.EducationFacilityCreateFromSearchView.as_view(), name="edufa-create-from-search"),
    path('edufa/<int:pk>/delete/', views.EducationFacilityRetrieveUpdateDestroyView.as_view(), name="edufa-delete"),

    #TRANSPORT FACILITY

    path('tranfa/search/', views.TransportFacilitySearchView.as_view(), name="tranfa-search"),
    path('tranfacategory/list/', views.TranfaCategoryListView.as_view(), name="tranfacategory-list"),
    path('<int:pk>/tranfa/create/', views.TransportFacilityListCreateView.as_view(), name="tranfa-create"),
    path('<int:pk>/tranfa/create-from-search/', views.TransportFacilityCreateFromSearchView.as_view(), name="tranfa-create-from-search"),
    path('tranfa/<int:pk>/delete/', views.TransportFacilityRetrieveUpdateDestroyView.as_view(), name="tranfa-delete"),
   
   #POINT OF INTEREST

    path('poi/search/', views.POISearchView.as_view(), name="poi-search"),
    path('poicategory/list/', views.POICategoryListView.as_view(), name="poicategory-list"),
    path('<int:pk>/poi/create/', views.POIListCreateView.as_view(), name="poi-create"),
    path('<int:pk>/poi/create-from-search/', views.POICreateFromSearchView.as_view(), name="poi-create-from-search"),
    path('poi/<int:pk>/delete/', views.POIRetrieveUpdateDestroyView.as_view(), name="poi-delete"),
   
   #AMENITY

    path('<int:pk>/amenity/create/', views.PropertyAmenityCreateView.as_view(), name="property-amenity-create"),
    path('amenity/<int:pk>/delete/', views.PropertyAmenityRetrieveUpdateDestroyView.as_view(), name="amenity-delete"),

    #RULE

    path('<int:pk>/rule/create/', views.RuleListCreateView.as_view(), name="property-rule-create"),
    path('rule/<int:pk>/delete/', views.RuleRetrieveUpdateDestroyView.as_view(), name="property-rule-delete"),
    path('rule/<int:pk>/update/', views.RuleRetrieveUpdateDestroyView.as_view(), name="property-rule-update"),

    #LISTING DISCOUNT BY CATEGORY
    path('listing-discount-by-category/list/', views.ListingDiscountByCategoryListCreateView.as_view(), name="listing-discount-by-category-list"),

    #LAND
    path('land/<int:pk>/delete/', views.LandRetrieveUpdateDestroyView.as_view(), name="land-delete"),
    path('land/<int:pk>/update/', views.LandRetrieveUpdateDestroyView.as_view(), name="land-update"),

    #SHAREHOUSE
    path('sharehouse/<int:pk>/delete/', views.ShareHouseRetrieveUpdateDestroyView.as_view(), name="sharehouse-delete"),
    path('sharehouse/<int:pk>/update/', views.ShareHouseRetrieveUpdateDestroyView.as_view(), name="sharehouse-update"),

    #APARTMENT
    path('apartment/<int:pk>/delete/', views.ApartmentRetrieveUpdateDestroyView.as_view(), name="apartment-delete"),
    path('apartment/<int:pk>/update/', views.ApartmentRetrieveUpdateDestroyView.as_view(), name="apartment-update"),
    path('apartment/<int:pk>/detail/', views.ApartmentRetrieveUpdateDestroyView.as_view(), name="apartment-detail"),
    path('apartment/list-by-agent/', views.ApartmentListByAgentView.as_view(), name="apartment-list-by-agent"),

    #APARTMENT UNIT
    path('apartmentunit/<int:pk>/delete/', views.ApartmentUnitRetrieveUpdateDestroyView.as_view(), name="apartment-unit-delete"),
    path('apartmentunit/<int:pk>/update/', views.ApartmentUnitRetrieveUpdateDestroyView.as_view(), name="apartment-unit-update"),
    path('apartmentunit/create/', views.ApartmentUnitCreateView.as_view(), name="apartment-unit-create"),
    # path('apartment/<int:pk>/detail/', views.ApartmentRetrieveUpdateDestroyView.as_view(), name="apartment-detail"),
    path('apartmentunit/list-by-apartment/', views.ApartmentUnitByApartmentView.as_view(), name="apartment-unit-list-by-apartment"),

    #VILLA
    path('villa/<int:pk>/delete/', views.VillaRetrieveUpdateDestroyView.as_view(), name="villa-delete"),
    path('villa/<int:pk>/update/', views.VillaRetrieveUpdateDestroyView.as_view(), name="villa-update"),
    path('villa/<int:pk>/detail/', views.VillaRetrieveUpdateDestroyView.as_view(), name="villa-detail"),
    path('villa/list-by-agent/', views.VillaListByAgentView.as_view(), name="villa-list-by-agent"),

    #CONDOMINIUM
    path('condominium/<int:pk>/delete/', views.CondominiumRetrieveUpdateDestroyView.as_view(), name="condominium-delete"),
    path('condominium/<int:pk>/update/', views.CondominiumRetrieveUpdateDestroyView.as_view(), name="condominium-update"),
    path('condominium/<int:pk>/detail/', views.CondominiumRetrieveUpdateDestroyView.as_view(), name="condominium-detail"),
    path('condominium/list-by-agent/', views.CondominiumListByAgentView.as_view(), name="condominium-list-by-agent"),

    #TRADITIONAL HOUSE
    path('traditionalhouse/<int:pk>/delete/', views.TraditionalHouseRetrieveUpdateDestroyView.as_view(), name="traditionalhouse-delete"),
    path('traditionalhouse/<int:pk>/update/', views.TraditionalHouseRetrieveUpdateDestroyView.as_view(), name="traditionalhouse-update"),
    path('traditionalhouse/<int:pk>/detail/', views.TraditionalHouseRetrieveUpdateDestroyView.as_view(), name="traditionalhouse-detail"),
    path('traditionalhouse/list-by-agent/', views.TraditionalHouseListByAgentView.as_view(), name="traditionalhouse-list-by-agent"),

    #COMMERCIAL PROPERTY
    path('commercialproperty/<int:pk>/delete/', views.CommercialPropertyRetrieveUpdateDestroyView.as_view(), name="commercialproperty-delete"),
    path('commercialproperty/<int:pk>/update/', views.CommercialPropertyRetrieveUpdateDestroyView.as_view(), name="commercialproperty-update"),
    path('commercialproperty/<int:pk>/detail/', views.CommercialPropertyRetrieveUpdateDestroyView.as_view(), name="commercialproperty-detail"),
    path('commercialproperty/list-by-agent/', views.CommercialPropertyListByAgentView.as_view(), name="commercialproperty-list-by-agent"),

    #COMMERCIAL PROPERTY UNIT
    path('commercialpropertyunit/<int:pk>/delete/', views.CommercialPropertyUnitRetrieveUpdateDestroyView.as_view(), name="commercialpropertyunit-delete"),
    path('commercialpropertyunit/<int:pk>/update/', views.CommercialPropertyUnitRetrieveUpdateDestroyView.as_view(), name="commercialpropertyunit-update"),
    path('commercialpropertyunit/create/', views.CommercialPropertyUnitCreateView.as_view(), name="commercialpropertyunit-create"),
    # path('commercialpropertyunit/<int:pk>/detail/', views.CommercialPropertyUnitRetrieveUpdateDestroyView.as_view(), name="commercialpropertyunit-detail"),
    path('commercialpropertyunit/list-by-commercialproperty/', views.CommercialPropertyUnitByCommercialPropertyView.as_view(), name="commercialpropertyunit-list-by-commercialproperty"),

    #SHARE HOUSE
    path('sharehouse/<int:pk>/delete/', views.ShareHouseRetrieveUpdateDestroyView.as_view(), name="sharehouse-delete"),
    path('sharehouse/<int:pk>/update/', views.ShareHouseRetrieveUpdateDestroyView.as_view(), name="sharehouse-update"),
    path('sharehouse/<int:pk>/detail/', views.ShareHouseRetrieveUpdateDestroyView.as_view(), name="sharehouse-detail"),
    path('sharehouse/list-by-agent/', views.ShareHouseListByAgentView.as_view(), name="sharehouse-list-by-agent"),



]