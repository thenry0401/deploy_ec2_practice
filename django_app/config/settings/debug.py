from .base import *

config_secret_debug = json.loads(open(CONFIG_SECRET_DEBUG_FILE).read())

# Static URLs
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static_root')

DEBUG = True # 디버그모드니까 Debug가 True
ALLOWED_HOSTS = config_secret_debug['django']['allowed_hosts']