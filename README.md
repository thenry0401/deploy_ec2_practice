# Deploy EC2

## requirements

**Python**
3.6.0

**pip**

```
pip install -r requirements.txt
```

---

## Create secret config files

### Project structure

```
project_folder/
	.config_secret/
		settings_common.json
		settings_debug.json
		settings_deploy.json
	django_app/
	...
	...
```

### settings_common.json example

```json
{
  	"django": {
		"secret_key": "Your django project secret key"
	}
}
```

### settings_debug.json example

```json
{
	"django": {
		"allowed_hosts": [
			"*"
		]
	}
}
```

### settings_deploy.json example

```json
{
	"django": {
		"allowed_hosts": [
			"*"
		]
	}
}
```

---

## runserver

```
# local development

>>> python3 manage.py runserver --settings=config.settings.debug
```