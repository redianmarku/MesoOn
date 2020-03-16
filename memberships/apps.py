from django.apps import AppConfig


class MembershipsConfig(AppConfig):
    name = 'memberships'

    def ready(self):
        import memberships.signals
