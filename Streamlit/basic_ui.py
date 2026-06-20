import streamlit as st

from File_process import FileProcessor


# Implemented a simple function UI due to limited remaining time


def ui():
    st.title("NER Model Processor")
    uploaded_file = st.file_uploader(
        "Pls Upload your TXT file", type=["txt"], accept_multiple_files=False
    )
    if uploaded_file is not None:
        try:
            file_data = uploaded_file.read().decode("utf-8")
            model_result = []
            with st.spinner("Running Secure BERT model:"):
                model_result = FileProcessor().process_text(file_data)
                st.dataframe(model_result)
            basic_filters(model_result)

        except Exception as e:
            st.write(str(e))


def basic_filters(model_result):
    st.markdown("Filter for your use")
    filter1, filter2 = st.columns(2)
    with filter1:
        available_types = list(model_result["entity_group"].unique())
        selected_types = st.multiselect(
            "Filter by Type:", options=available_types, default=available_types
        )

    with filter2:
        search_query = st.text_input("Search a word:", placeholder="Jonathan")

    filter = model_result[model_result["entity_group"].isin(selected_types)]
    if search_query:
        filter = filter[filter["word"].str.contains(search_query, case=False)]

    st.markdown(f"({len(filter)} Shown)")
    st.dataframe(filter)


if __name__ == "__main__":
    ui()
