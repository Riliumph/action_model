from django.urls import path

from sample_app.controller import action_controller as act_con
from sample_app.controller import action_link_controller as act_link_con

urlpatterns = [
    path('v1/actions/', act_con.LC.as_view()),
    path('v1/actions/<int:action_id>', act_con.RUD.as_view()),
    path('v1/actions/<int:action_id>/links', act_con.RUD.as_view()),
    path('v1/action_links/', act_link_con.LC.as_view()),
    path('v1/action_links/<int:action_link_id>', act_link_con.RUD.as_view()),
]
