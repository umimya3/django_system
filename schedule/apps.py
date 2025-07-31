from django.apps import AppConfig
import os

class ScheduleConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'schedule'

    def ready(self):
         DEBUGモードの時だけ実行
         if os.environ.get('DEBUG') == 'True':
             from django.contrib.auth import get_user_model
             User = get_user_model()
             username = os.environ.get('DJANGO_SUPERUSER_USERNAME', 'admin')
             email = os.environ.get('DJANGO_SUPERUSER_EMAIL', 'admin@example.com')
             password = os.environ.get('DJANGO_SUPERUSER_PASSWORD', 'adminpassword') # ★非常に危険なパスワード！必ず変更すること！

             if not User.objects.filter(username=username).exists():
                 print(f"Creating superuser: {username}")
                 User.objects.create_superuser(username, email, password)
                 print("Superuser created successfully.")
             else:
                 print(f"Superuser {username} already exists.")