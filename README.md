# Poetrydb Api Testcases
|

# How to run the project? 
 - Clone github repository in your local system  `git clone https://github.com/Erick-hub/poetrydb-api-testing`
 - Move in twitch-ui-testing repository  `cd poetrydb-api-testing`
 - Create new virtual python environment  `python3 -m venv venv`
 - Activate virtual python environment  `source venv/bin/activate` for linux, `venv\Scripts\activate.bat` for windows
 - Install all the libraries mentioned in [requirements.txt](https://github.com/Erick-hub/twitch-ui-testing/requirements.txt) using  `pip install -r requirements.txt`
 - Run Python file  `python run_tests.py`
 
# Directory Tree
```bash
poetrydb-api-testing/

┣ get_requests/
┃ ┣ __init__.py
┃ ┣ base_class.py
┃ ┗ get_poem.py
┣ tests/
┃ ┣ base_test.py
┃ ┣ conftest.py
┃ ┗ test_poems.py
┣ jubilate_agno.json
┣ requirements.txt
┗ run_tests.py
```
 





