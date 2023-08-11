import streamlit as st
import PyPDF2
from main import generate_presentation_using_topic

# Streamlit configuration
st.set_page_config(
    page_title="PDF to PPT Converter",
    page_icon=":open_file_folder:"
)


def pdf_ext(file):
    pdfReader = PyPDF2.PdfReader(file)
    extracted_text = ""
    
    for pageObj in pdfReader.pages:
        extracted_text += pageObj.extract_text()
        
    return extracted_text

def main():
    st.title("PDF Text Extractor")
    uploaded_file = st.file_uploader("Upload a PDF file", type=["pdf"])
    
    if uploaded_file is not None:
        st.sidebar.title("File Info")
        st.sidebar.text(f"Uploaded file: {uploaded_file.name}")
        
        extracted_text = pdf_ext(uploaded_file)
        generate_presentation_using_topic(extracted_text)


        
        st.header("Extracted Text")
        st.write(extracted_text)
        
if __name__ == "__main__":
    main()
