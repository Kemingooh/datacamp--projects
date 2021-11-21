# Datacamp projects

## Disclaimer

* The certification projects may change over time with updates / fixes etc.
* Try not to copy the solutions presented in this repository, it's purpose is to be a guideline only.

## Projects

| Project name | DC link (ID) |  Python | SQL | Note | Requires a DB |
| --- | --- | --- | --- | --- | --- |
| [What and Where Are the World's Oldest Businesses?](projects/oldest_businesses/notebook.ipynb) | [1168](https://projects.datacamp.com/projects/1168) | ❌ | ✅ | Guided | ✅ |
| [Museum Data Validation](projects/museum_data_validation/notebook.ipynb) | [1327](https://projects.datacamp.com/projects/1327) | ❌ | ✅ | SQL Certification | ✅ |
| [Animal Shelters: SQL Certification](projects/animal_shelters/notebook.ipynb) | [1295](https://projects.datacamp.com/projects/1295) | ❌ | ✅ | SQL Certification | ✅ |
| [Analyze International Debt Statistics](projects/international_debt/notebook.ipynb) | [754](https://projects.datacamp.com/projects/754) | ❌ | ✅ | | ✅ |
| [Analyzing TV Data](projects/analyzing_tv_data/notebook.ipynb) | [684](https://projects.datacamp.com/projects/684) | ✅ | ❌ | Guided | ❌ |
| [Exploring the History of Lego](projects/exploring_the_history_of_lego/notebook.ipynb) | [10](hhttps://projects.datacamp.com/projects/10) | ✅ | ❌ | Guided | ❌ |
| [Word Frequency in Classic Novels](projects/word_frequency_in_classic_novels/notebook.ipynb) | [38](hhttps://projects.datacamp.com/projects/38) | ✅ | ❌ | Guided | ❌ |
| [Energy Savings](projects/energy_savings/notebook.ipynb) | [1249](https://projects.datacamp.com/projects/1249) | ✅ | ❌ | Guided | ❌ |

### Requirements

* Docker (Only for projects that require a DB)
* Python 3.7+

### Prepare venv

Download the repository, if you have not already

```sh
git clone https://github.com/jpuris/datacamp--projects.git
```

cd into the cloned repostiory

```sh
cd datacamp--projects
```

Make sure your python3 has virtualenv package installed

```sh
python3 -m pip install virtualenv
```

Create and activate python virtual environment

```sh
python3 -m venv venv
source venv/bin/activate
```

Install required python packages

```sh
pip install -r requirements.txt
```

Only applicable for the projects that require DB setup

### Loading project data

*Only applicable for the projects that require DB setup* *!*

Start PostgreSQL server in a docker container

```sh
docker compose -f database/docker/docker-compose.yaml up
```

Run the ETL job for the project

```sh
python projects/<chosen project>/db_setup.py
```

Example successful output

```txt
datacamp--projects on  main [!] via 🐍 v3.9.8 (venv)
❯ python projects/animal_shelters/db_setup.py
Establishing connection with DB
Done
Running
Done
Establishing connection with DB
Done
Loading data from '/Users/jp/git/datacamp--projects/projects/animal_shelters/assets/data/sponsored_pets.csv' into 'sponsored_animals'
Done
Establishing connection with DB
Done
Loading data from '/Users/jp/git/datacamp--projects/projects/animal_shelters/assets/data/age_costs.csv' into 'age_costs'
Done
Establishing connection with DB
Done
Loading data from '/Users/jp/git/datacamp--projects/projects/animal_shelters/assets/data/location_costs.csv' into 'location_costs'
Done
Establishing connection with DB
Done
Loading data from '/Users/jp/git/datacamp--projects/projects/animal_shelters/assets/data/size_costs.csv' into 'size_costs'
Done
Establishing connection with DB
Done
Loading data from '/Users/jp/git/datacamp--projects/projects/animal_shelters/assets/data/animal_data.csv' into 'animals'
Done
```
