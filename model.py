import abc
import dataclasses


@dataclasses.dataclass
class Result:

    name: str
    last_name: str = ""
    total_purchases: int = 0


class QueryInterface(abc.ABC):

    """Defines Snowflake Query processing."""

    @abc.abstractmethod
    def get_query_string(self) -> str:
        """Returns query string."""

    @abc.abstractmethod
    def get_results(self, data: dict) -> Result:
        """Returns results from snowflake data."""
