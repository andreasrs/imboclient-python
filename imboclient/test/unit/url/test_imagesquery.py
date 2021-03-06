import imboclient.url.imagesquery

class TestQuery:
    def setup(self):
        return

    def teardown(self):
        return

    def test_query_default(self):
        query = imboclient.url.imagesquery.Query()

        assert query.q_to() == None
        assert query.q_from() == None
        assert query.query() == None
        assert query.metadata() == False
        assert query.limit() == 20
        assert query.page() == 1

    def test_query_custom(self):
        query = imboclient.url.imagesquery.Query()

        query.q_to("to_value").q_from("from_value").query({"query_key": "query_value"}).metadata(True).limit(2).page(3)

        assert query.q_to() == "to_value"
        assert query.q_from() == "from_value"
        assert query.query() == {"query_key": "query_value"}
        assert query.metadata() == True
        assert query.limit() == 2
        assert query.page() == 3

