from model import QueryInterface


class Factory:
    def __init__(self, queries: dict) -> None:
        self.queries = queries

    def get_query(self, country: str) -> QueryInterface:
        try:
            return self.queries[country]
        except KeyError:
            return "Error"
