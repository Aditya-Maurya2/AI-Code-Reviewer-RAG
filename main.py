from app.retriever import search_code
from app.reviewer import review_code

query = input("Ask Question: ")

docs = search_code(query)

context = "\n".join(
    [doc.page_content for doc in docs]
)

result = review_code(
    context,
    query
)

print("\n")
print(result)