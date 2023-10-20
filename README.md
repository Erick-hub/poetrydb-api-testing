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
 
# Poetrydb Api Testcases
- For this list of test cases we'll be using the sample [jubilate_agno.json](https://github.com/Erick-hub/twitch-ui-testing/requirements.txt)
```json
{
   "title": "from Jubilate Agno, Fragment B, lines 695-768",
   "author": "Christopher Smart",
   "lines":["..."]
   "linecount": "77"
}
```

| Tests                      | Objective                                                      | Test Steps                                    | Expected Output                                                                                                             | Validation                                                                                                                                                                                                 |
|----------------------------|----------------------------------------------------------------|-----------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| test_get_all_titles        | Ensure all titles are retrieved                                | - request all titles                          | - list of all titles in the database<br><br>- check last title is our sample poem                                           | - check last title equals "from Jubilate Agno, Fragment B, lines 695-768"<br><br>- check that length of list equals to 3010                                                                                |
| test_get_poem_by_title     | Ensure a specific poem can be retrieved by inputting its title | - request poem, input our sample's title      | - list with a single poem<br><br>- poem's author is equal to our sample's author<br><br>- linecount equals to poem's length | - check length of the list equals to 1<br><br>- check if the author's name matches the expected result<br><br>- get the length of the "lines" field array and check if it matches with the linecount field |
| test_get_poem_by_linecount | Ensure function retrieve poems with specified linecount        | - request poem list by our sample's linecount | - list of poems all possess a linecount equals to the input<br><br>- sample poem is among the results                       | - check linecount field for each poem<br><br>- check if our sample poem is among the retrieved poems                                                                                                       |
| test_get_all_authors       | Ensure all authors are retrieved                               | - request all author                          | - list of all authors in the database<br><br>- list contains our sample author                                              | - check "Christopher Smart" is in the author list<br><br>- check that there is 129 authors in total<br><br>- check the last author is 'William Wordsworth'                                                 |

 






