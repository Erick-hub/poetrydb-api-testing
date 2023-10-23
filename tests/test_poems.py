from get_requests.get_poem import GetPoems, GetAuthor
from base_test import BaseTest


class TestPoems(BaseTest):

    def test_get_all_titles(self):
        self.get_poems = GetPoems()
        res = self.get_poems.get_all_titles()
        assert len(res['titles']) == 3010
        assert res['titles'][3009] == self.sample['title']

    def test_get_poem_by_title(self):
        self.get_poems = GetPoems()
        res = self.get_poems.by_title(
            self.sample['title'])
        assert len(res) == 1
        assert res[0]['author'] == self.sample['author']
        assert int(res[0]['linecount']) == len(res[0]['lines'])

    def test_get_poem_by_linecount(self):
        linecount = self.sample['linecount']
        self.get_poems = GetPoems()
        res = self.get_poems.by_linecount(linecount)
        assert self.sample['title'] in [
            x['title'] for x in res]
        for x in res:
            assert int(x['linecount']) == int(linecount)

    def test_get_all_authors(self):

        self.get_author = GetAuthor()
        res = self.get_author.get_all_authors()
        assert len(res['authors']) == 129
        assert res['authors'][128] == 'William Wordsworth'
        assert self.sample['author'] in res['authors']
