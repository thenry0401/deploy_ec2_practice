from .base import *

config_secret_deploy = json.loads(open(CONFIG_SECRET_DEPLOY_FILE).read())

DEBUG = False # 배포모드 이므로 Debug가 False

ALLOWED_HOSTS = config_secret_deploy['django']['allowed_hosts']