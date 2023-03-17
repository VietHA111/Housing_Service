foo:
	flask --app housing_service init-db
	flask --app housing_service run --debug

init-db:
	flask --app housing_service init-db
	
run:
	flask --app housing_service run --debug

venv:
	. venv/bin/activate