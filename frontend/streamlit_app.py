import sys
import os

sys.path.append(
    os.path.dirname(
        os.path.dirname(
            os.path.abspath(__file__)
        )
    )
)

import streamlit as st

from app.uploader import save_uploaded_file
from app.ingest import create_vectorstore
from app.retriever import search_code
from app.reviewer import review_code

st.title("AI Code Reviewer with RAG")

uploaded_file = st.file_uploader(
    "Upload Source Code",
    type=["py", "js", "java", "cpp"]
)

question = st.text_input(
    "Ask Question"
)

if st.button("Analyze"):

    if uploaded_file:

        file_path = save_uploaded_file(
            uploaded_file
        )

        create_vectorstore(
            file_path
        )

        docs = search_code(
            question
        )

        context = "\n".join(
            [doc.page_content for doc in docs]
        )

        result = review_code(
            context,
            question
        )

        st.markdown(result)