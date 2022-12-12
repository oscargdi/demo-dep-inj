from factory import Factory
from templates.co import COQuery
from templates.generic import GenericQuery

co_implementation = COQuery()
generic_implementation = GenericQuery()

queries = {"co": co_implementation}

factory = Factory(queries)

country = input("Country: ")  # this should come from header

query = factory.get_query(country)

print(query.get_query_string())

data = {"name": "EVA", "country": country}  # snowflake_client.execute(query_string)


result = query.get_results(data)

print(result)
print(f"Hola {result.name.lower()}")
