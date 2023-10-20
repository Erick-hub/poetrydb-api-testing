from get_requests.base_class import BaseClass
import requests
import json


class GetPoems(BaseClass):
    def __init__(self) -> None:
        super().__init__()

    def get_all_titles(self):
        response = requests.get(self.base_url_title)
        return json.loads(response.text)

    def by_title(self, title):
        response = requests.get(self.base_url_title + '/' + title)
        return json.loads(response.text)

    def by_linecount(self, linecount):
        response = requests.get(self.base_url_linecount+'/' + str(linecount))
        return json.loads(response.text)

    def by_lines(self, lines):
        response = requests.get(self.base_url_lines+'/' + lines)
        return json.loads(response.text)


class GetAuthor(BaseClass):
    def __init__(self) -> None:
        super().__init__()

    def get_all_authors(self):
        response = requests.get(self.base_url_author)
        return json.loads(response.text)

    def get_author(self, author):
        response = requests.get(self.base_url_author+'/' + author)
        return json.loads(response.text)
