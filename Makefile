# Site build and local dev environment (see deploy/compose.yaml).

DEV_URL = https://site-dev.darkfox.info/
COMPOSE = docker compose -f deploy/compose.yaml

.PHONY: help serve build dev-build up down ipfs clean

help: ## Show available targets
	@awk 'BEGIN {FS = ":.*## "} /^[a-zA-Z_-]+:.*## / {printf "  %-12s %s\n", $$1, $$2}' $(MAKEFILE_LIST)

serve: ## Hugo dev server with drafts at localhost:1313
	hugo server -D

build: ## Production build (prod baseURL) into public/
	hugo --minify

dev-build: ## Build with dev baseURL into public/
	hugo --minify -b $(DEV_URL)

up: dev-build ## Build for dev and start nginx + kubo sandbox
	$(COMPOSE) up -d

down: ## Stop the sandbox
	$(COMPOSE) down

ipfs: ## Add current public/ to the sandbox IPFS node, print CID
	docker exec ipfs-dev ipfs add -rQ --cid-version 1 /export/site

clean: ## Remove build output
	rm -rf public
