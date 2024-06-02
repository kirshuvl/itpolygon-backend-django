DC = docker compose -p itpolygon-backend

DJANGO_FILE = docker/django.yaml
DJANGO_CONTAINER = django
MANAGE_PY = python3 manage.py


DATABASE_FILE = docker/database.yaml
DATABASE_CONTAINER = database


EXEC = docker exec -i
LOGS = docker logs
ENV = --env-file .env


.PHONY: app
app:
	${DC} -f ${DJANGO_FILE} -f ${DATABASE_FILE} ${ENV} up --build -d

.PHONY: app-logs
app-logs:
	${LOGS} ${DJANGO_CONTAINER} -f

.PHONY: app-down
app-down:
	${DC} -f ${DJANGO_FILE} -f ${DATABASE_FILE} down

.PHONY: database
database:
	${DC} -f ${DATABASE_FILE} ${ENV} up -d

.PHONY: database-logs
database-logs:
	${LOGS} ${DATABASE_CONTAINER} -f

.PHONY: database-down
database-down:
	${DC} -f ${DATABASE_FILE} down

.PHONY: postgres
postgres:
	${EXEC} ${DATABASE_CONTAINER} psql -U postgres

.PHONY: superuser
superuser:
	${EXEC}t ${DJANGO_CONTAINER} ${MANAGE_PY} createsuperuser

.PHONY: migrations
migrations:
	${EXEC} ${DJANGO_CONTAINER} ${MANAGE_PY} makemigrations

.PHONY: migrate
migrate:
	${EXEC} ${DJANGO_CONTAINER} ${MANAGE_PY} migrate

.PHONY: collectstatic
collectstatic:
	${EXEC} ${DJANGO_CONTAINER} ${MANAGE_PY} collectstatic

.PHONY: lint
lint:
	isort . && black . && pflake8 .

.PHONY: check
check:
	${DC} ps

.PHONY: test
test:
	${EXEC} ${DJANGO_CONTAINER} ${MANAGE_PY} test

.PHONY: piplist
piplist:
	${EXEC} ${DJANGO_CONTAINER} pip list
