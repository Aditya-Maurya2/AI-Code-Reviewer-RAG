from app.reviewer import review_code

result = review_code(
    """
def divide(a,b):
    return a/b

print(divide(10,0))
""",
    "Find bug in code"
)

print(result)