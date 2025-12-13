# dentist cabinet frontend for AllergoProbe.kz

this project is deployed here - https://gmankab.github.io/allergo-probe-dentist

### install uv

```shell
python -m ensurepip
python -m pip install -U uv
```

### run as a desktop app

```shell
uv run flet run
```

### run as a web app

```shell
uv run flet run --web
```

### build webpage

```shell
uv run flet build web
```

### deploying

see `.github/workflows/deploy.yml`

### linting

```shell
uvx ruff check
uvx ty check
```
