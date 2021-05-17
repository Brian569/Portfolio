serve:
	python manage.py runserver ${port}

migrations:
	python manage.py makemigrations

migrate:
	python manage.py migrate

shell:
	python manage.py shell

user:
	python manage.py createsuperuser