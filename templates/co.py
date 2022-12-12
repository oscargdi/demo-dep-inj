from model import QueryInterface, Result


class COQuery(QueryInterface):

    """Defines Snowflake Query processing."""

    def get_query_string(self) -> str:
        """Returns query string."""
        return "SELECT CO hxjhzjhakfhsjdksjdks"

    def get_results(self, data: dict) -> Result:
        """Returns results from snowflake data."""
        result = Result(name="CO", last_name="EVA".lower(), total_purchases=6)
        return result
