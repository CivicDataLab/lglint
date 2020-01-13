# lglint

Interpretation of Legal documents

## Installation

### Poetry

```
pip install poetry
```

## Usage

Install package
```
poetry install
```

### Converting PDFs to text

Run the command below to understand the usage of the file
```
poetry run python scripts/pdf2txt.py --help
```

### Running pipeline

copy config.json.sample to config.json

update the variables in config.json

run
```
poetry run python main.py
```