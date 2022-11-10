
# Kijiji-Ad-Parser

The parser that collect all ads, including pagination from https://www.kijiji.ca/b-apartments-condos/city-of-toronto/c37l1700273 and save to database

The following items are collected from each ad: title,
price,
currency,
data,
image(url),
pagination.

## Installation and running

- Clone the repository

```bash
  git clone https://github.com/themutesinger/Kijiji-Ad-Parser
```

- Go to the directory
```bash
  cd Kijiji-Ad-Parser
```

- Use poetry to install the dependencies
```bash
  poetry install
```

- Run the program from the virtual environment
```bash
  poetry run python parser.py
```
and a database with data will appear in the project directory
