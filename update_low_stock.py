from gql import gql, Client
from gql.transport.requests import RequestsHTTPTransport

transport = RequestsHTTPTransport(
    url="http://localhost:8000/graphql",
    verify=False,
    retries=3,
)

client = Client(transport=transport, fetch_schema_from_transport=True)

query = gql("""
query {
  products(lowStock: true) {
    id
    name
    stock
  }
}
""")

def run():
    try:
        result = client.execute(query)
        for product in result['products']:
            print(f"Low stock: {product['name']} (Stock: {product['stock']})")
    except Exception as e:
        print("Error connecting to GraphQL server:", e)
