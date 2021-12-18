# Datacamp projects

## Disclaimer

* The certification projects may change over time with updates / fixes etc.
* Try not to copy the solutions presented in this repository, it's purpose is to be a guideline only.

## Projects

| Project name | DC link (ID) |  Python | SQL | Note | Requires a DB |
| --- | --- | --- | --- | --- | --- |
| [What and Where Are the World's Oldest Businesses?](projects/oldest_businesses/notebook.ipynb) | [1168](https://projects.datacamp.com/projects/1168) | ❌ | ✅ | Guided | ✅ |
| [Museum Data Validation](projects/museum_data_validation/notebook.ipynb) | [1327](https://projects.datacamp.com/projects/1327) | ❌ | ✅ | SQL Certification | ✅ |
| [Animal Shelters](projects/animal_shelters/notebook.ipynb) | [1295](https://projects.datacamp.com/projects/1295) | ❌ | ✅ | SQL Certification | ✅ |
| [Analyze International Debt Statistics](projects/international_debt/notebook.ipynb) | [754](https://projects.datacamp.com/projects/754) | ❌ | ✅ | Guided | ✅ |
| [Analyzing TV Data](projects/analyzing_tv_data/notebook.ipynb) | [684](https://projects.datacamp.com/projects/684) | ✅ | ❌ | Guided | ❌ |
| [Exploring the History of Lego](projects/exploring_the_history_of_lego/notebook.ipynb) | [10](https://projects.datacamp.com/projects/10) | ✅ | ❌ | Guided | ❌ |
| [Word Frequency in Classic Novels](projects/word_frequency_in_classic_novels/notebook.ipynb) | [38](https://projects.datacamp.com/projects/38) | ✅ | ❌ | Guided | ❌ |
| [Energy Savings](projects/energy_savings/notebook.ipynb) | [1249](https://projects.datacamp.com/projects/1249) | ✅ | ❌ | Python Certification | ❌ |
| [A Visual History of Nobel Prize Winners](projects/nobel_prize_winners/notebook.ipynb) | [441](https://projects.datacamp.com/projects/441) | ✅ | ❌ | Guided | ❌ |
| [Investigating Netflix Movies and Guest Stars in The Office](projects/netflix_movies/notebook.ipynb) | [1237](https://projects.datacamp.com/projects/1237) | ✅ | ❌ | Guided | ❌ |
| [Recreating John Snow's Ghost Map](projects/john_snows_ghost_map/notebook.ipynb) | [132](https://projects.datacamp.com/projects/132) | ✅ | ❌ | Guided | ❌ |
| [The Android App Market on Google Play](projects/the_android_app_market_on_google_play/notebook.ipynb) | [619](https://projects.datacamp.com/projects/619) | ✅ | ❌ | Guided | ❌ |
| [The GitHub History of the Scala Language](projects/the_github_history_of_the_scala_language/notebook.ipynb) | [163](https://projects.datacamp.com/projects/163) | ✅ | ❌ | Guided | ❌ |
| [Dr. Semmelweis and the Discovery of Handwashing](projects/dr_semmelweis_and_the_discovery_of_handwashing/notebook.ipynb) | [20](https://projects.datacamp.com/projects/20) | ✅ | ❌ | Guided | ❌ |

### Viewing notebooks with external visualisations

Sometimes, when libs like bokeh or folium are used, github notebooks will not display the content correctly

For this, one can use <https://nbviewer.org> and then paste in the full github repo's notebook URL

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
