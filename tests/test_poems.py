from get_requests.get_poem import GetPoems, GetAuthor
from base_test import BaseTest


class TestPoems():

    def test_get_all_titles(self):
        self.get_poems = GetPoems()
        res = self.get_poems.get_all_titles()
        assert len(res['titles']) == 3010
        assert res['titles'][3009] == "from Jubilate Agno, Fragment B, lines 695-768"

    def test_get_poem_by_title(self):
        self.get_poems = GetPoems()
        res = self.get_poems.by_title(
            "from Jubilate Agno, Fragment B, lines 695-768")
        assert res[0]['author'] == "Christopher Smart"
        assert int(res[0]['linecount']) == len(res[0]['lines'])

    def test_get_poem_by_linecount(self):
        self.get_poems = GetPoems()
        res = self.get_poems.by_linecount(77)
        assert "from Jubilate Agno, Fragment B, lines 695-768" in [
            x['title'] for x in res]

    def test_get_all_authors(self):

        self.get_author = GetAuthor()
        res = self.get_author.get_all_authors()
        assert len(res['authors']) == 129
        assert res['authors'][128] == 'William Wordsworth'
        assert "Christopher Smart" in res['authors']
