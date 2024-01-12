from django.urls import path
from .views import (
    CompanyListView,CompanyDetialView
    ,UnitDetialView, UnitListView
    ,BranchView, BranchDetialView
    ,DepartmentListView, DepartmentDetialView
    ,DivisionView, DivisionDetialView
)

urlpatterns = [
    path('companie',CompanyListView.as_view(),name="company-list"),
    path('companie/<int:pk>',CompanyDetialView.as_view(),name="company-detail"),

    path('unit',UnitListView.as_view(),name="unit-list"),
    path('unit/<int:pk>',UnitDetialView.as_view(),name="unit-detail"),

    path('branch',BranchView.as_view(),name="branch-list"),
    path('branch/<int:pk>',BranchDetialView.as_view(),name="branch-detail"),

    path('department',DepartmentListView.as_view(),name="department-list"),
    path('department/<int:pk>',DepartmentDetialView.as_view(),name="department-detail"),

    path('division',DivisionView.as_view(),name="division-list"),
    path('division/<int:pk>',DivisionDetialView.as_view(),name="division-detail"),

]