from django.urls import path

from sample_app.controller import action, action_link, map, palette

urlpatterns = [
    path('v1/actions/', action.LC.as_view()),
    path('v1/actions/<int:action_id>', action.RUD.as_view()),
    path('v1/action_links/', action_link.LC.as_view()),
    path('v1/action_links/<int:action_link_id>',
         action_link.RUD.as_view()),
    path('v1/palettes/', palette.LC.as_view()),
    path('v1/maps/', map.LC.as_view()),
]
