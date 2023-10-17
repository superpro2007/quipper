start_env:
	docker compose -f local_env/docker-compose.yaml up -d  --build

stop_env:
	docker compose -f local_env/docker-compose.yaml down

clean_env:
	docker container prune -f; \
	docker volume prune -f; \
	docker volume ls -qf dangling=true | xargs -r docker volume rm; \
	docker network prune -f;
