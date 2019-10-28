"""URL routing for the topics application."""

from django.urls import path

from . import views

app_name = "topics"
urlpatterns = [
    # eg: /topics/
    path(
        "",
        views.IndexView.as_view(),
        name="index"
    ),
    # eg: /topics/glossary/
    path(
        "glossary/",
        views.GlossaryList.as_view(),
        name="glossary"
    ),
    # eg: /topics/glossary/json/
    path(
        "glossary/json/",
        views.glossary_json,
        name="glossary_json"
    ),
    # eg: /topics/curriculum-integrations/
    path(
        "curriculum-integrations/",
        views.AllCurriculumIntegrationList.as_view(),
        name="all_curriculum_integrations"
    ),
    # eg: /topics/binary-numbers/
    path(
        "<topic_slug>/",
        views.TopicView.as_view(),
        name="topic"
    ),
    # eg: /topics/binary-numbers/integrations/binary-bracelets/
    path(
        "<topic_slug>/integrations/<integration_slug>/",
        views.CurriculumIntegrationView.as_view(),
        name="integration"
    ),
    # eg: /topics/binary-numbers/other-resources/
    path(
        "<topic_slug>/other-resources/",
        views.OtherResourcesView.as_view(),
        name="other_resources"
    ),
    # eg: /topics/binary-numbers/unit-plan/
    path(
        "<topic_slug>/unit_plan_slug>/",
        views.UnitPlanView.as_view(),
        name="unit_plan"
    ),
    # eg: /topics/binary-numbers/unit-plan/description/
    path(
        "<topic_slug>/unit_plan_slug>/description/",
        views.UnitPlanDescriptionView.as_view(),
        name="unit_plan_description"
    ),
    # eg: /topics/binary-numbers/unit-plan/lesson-1/
    path(
        "<topic_slug>/unit_plan_slug>/<lesson_slug>/",
        views.LessonView.as_view(),
        name="lesson"
    ),
    # eg: /topics/binary-numbers/unit-plan/lesson-1/programming/
    path(
        "<topic_slug>/<unit_plan_slug>/<lesson_slug>/programming/",
        views.ProgrammingChallengeList.as_view(),
        name="programming_challenges_list"
    ),
    # eg: /topics/binary-numbers/programming/challenge-1/
    path(
        "<topic_slug>/programming/programming_challenge_slug>",  # noqa: E501
        views.ProgrammingChallengeView.as_view(),
        name="programming_challenge"
    ),
    # eg: /topics/binary-numbers/programming/challenge-1/python-solution/
    path(
        "<topic_slug>/programming/<programming_challenge_slug>/<programming_language_slug>-solution",  # noqa: E501
        views.ProgrammingChallengeLanguageSolutionView.as_view(),
        name="programming_challenge_solution"
    ),
]
