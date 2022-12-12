from model import QueryInterface, Result


class GenericQuery(QueryInterface):

    """Defines Snowflake Query processing."""

    def get_query_string(self) -> str:
        """Returns query string."""
        return "SELECT CL form jsdjhjshjdsh"

    def get_results(self, data: dict) -> Result:
        """Returns results from snowflake data."""
        result = Result(name="CL", last_name="EVA", total_purchases=10)
        return result
