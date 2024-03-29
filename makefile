package-update:
	build publish package-install

install:
	poetry install

brain-games:
	poetry run brain-games

build:
	poetry build
	
publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --force-reinstall dist/*.whl

make lint:
	poetry run flake8 brain_games
