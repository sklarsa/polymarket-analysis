.PHONY: run-ws
run-ws:
	npx ts-node src/index.ts

.PHONY: update-markets
update-markets:
	poetry run python main.py > active_markets