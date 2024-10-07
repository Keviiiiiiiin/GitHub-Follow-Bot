from django.apps import AppConfig

import back_bone as bb
import os

class GfConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'gf'
    verbose_name = 'GitHub Follower'


    def ready(self):
        env = os.environ.get("FIRST_THREAD")

        # Check if first thread has started since we want to spin it up on the second thread in development.
        if env is not None:
            from .models import Setting

            # Set settings. defaults.
            Setting.create("enabled", "1", True)
            Setting.create("max_scan_users", "10", True)
            Setting.create("wait_time_follow_min", "10", True)
            Setting.create("wait_time_follow_max", "30", True)
            Setting.create("wait_time_list_min", "5", True)
            Setting.create("wait_time_list_max", "30", True)
            Setting.create("scan_time_min", "5", True)
            Setting.create("scan_time_max", "60", True)
            Setting.create("verbose", "1", True)
            Setting.create("user_agent", "GitHub-Follower", True)
            Setting.create("seed", "1", True)
            Setting.create("seed_min_free", "64", True)
            Setting.create("max_api_fails", "5", True)
            Setting.create("lockout_wait_min", "1", True)
            Setting.create("lockout_wait_max", "10", True)
            Setting.create("seed_max_pages", "5", True)

            bb.parser.start()
        else:
            os.environ["FIRST_THREAD"] = 'True'