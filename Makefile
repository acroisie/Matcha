SERVICES = backend frontend database
build:
	docker-compose build $(SERVICES)
up:
	docker-compose up -d $(SERVICES)
down:
	docker-compose down

restart: down up

clean:
	docker-compose down --rmi all --volumes --remove-orphans
prune:
	docker system prune -af --volumes
re: build restart

.PHONY: build up down restart clean prune re create-volume remove-volume
