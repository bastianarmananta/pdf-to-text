import re
import io
import os.path
import fitz
import streamlit as st

from PIL import Image


image = Image.open('temp/pdf-to-txt.png')
st.set_page_config(page_title='PDF Converter', page_icon=image, layout="wide", initial_sidebar_state="auto", menu_items=None)

# make sidebar
with st.sidebar:
    st.image(image)
    st.title("PDF to TXT")
    choice = st.radio(" ", ['Convert', 'Clean'], label_visibility="collapsed")
    st.info("This app helps you to convert pdf to txt and clean your data!")
    st.sidebar.markdown("---")
    st.sidebar.markdown("Developed by [Bastian Armananta](https://www.linkedin.com/in/bastian-armananta/)")

# make condition convert for sidebar menu
if choice == 'Convert':
    st.title('Upload your pdf file')
    uploaded_pdf_files = st.file_uploader(label=' ', accept_multiple_files=True, type=['pdf'], label_visibility="collapsed")

    # make condition if user uploading file
    if uploaded_pdf_files is not None:
        st.info('Expand to see your data')

        # use a buffer to store the text data
        text_data = io.StringIO()

        # loop through each file uploaded by user
        for uploaded_file in uploaded_pdf_files:
            # write the uploaded file to memory
            with io.BytesIO(uploaded_file.read()) as mem_file:
                # use expander to read each file
                with st.expander(uploaded_file.name):
                    read_pdf = fitz.open(stream=mem_file, filetype="pdf")

                    # loop through every page in every uploaded file
                    for page in read_pdf.pages():
                        text = page.get_text()
                        st.write(text)

                        text_data.write(text)
                        text_data.write("\n###############################################################\n")

        # button for downloading all files
        download_pdf_btn = st.download_button(label="Download all data", data=text_data.getvalue(), file_name='merged.txt')

        if download_pdf_btn:
            st.success('File has been merged and converted into txt!')

    else:
        st.warning('Please upload your pdf data!', icon=None)

if choice == 'Clean':
    st.title('Upload your txt file')
    uploaded_txt_files = st.file_uploader("Upload your txt data!", accept_multiple_files=True, type=['txt'], label_visibility='collapsed')

    if uploaded_txt_files is not None:
        for x in uploaded_txt_files:
            with open(x.name, "wb") as f:
                f.write(x.read())

            with st.expander(x.name):
                with open(x.name, "r", encoding='utf-8') as read_txt:
                    content = read_txt.read()
                    st.write(content)

            if st.button('Clean text'):
                # Define regular expression patterns for text to remove
                patterns = [
                    r'BAB\sI{1,}|BAB\s1|BAB\s2|PEN.+|TIN.+|\nDASAR.+',
                    r'Tabel[\s\S]*?\d\..+',
                    r'\n\d\.\d\s{1,}\w{1,}\s.+\n|\d\.\d\.\d\s.+\n|\d\.\d\.\s.+',
                    r'\n\d\s\n|\d\s\n',
                    r'\nTabel\s\d\s\d\s.+',
                    r'^\s+',
                    r'Gambar.+',
                    r'\n[a-z]\s\w.+\n|\n\w\s\n\w.+',
                    r'\[\d+\]',
                    r'\s{1,10}\.',
                    r'\n',
                    r'[^A-Za-z0-9\.\,\#\s]+',
                    r'http://',
                    r'\s{2,}',
                    r'###+',
                    r'\.\s\n\s',
                ]
                
                # Combine regular expression patterns into a single pattern
                pattern = '|'.join(patterns)
                
                # Remove all matched text using the pattern
                content = re.sub(pattern, '', content)
                
                # Remove multiple whitespace and replace with dot
                content = re.sub('\s{1,10}\.', '.', content)

                # Remove multiple whitespace and replace with single space
                content = re.sub('\s{2,}', ' ', content)

                # Subtitute many # with newline
                content = re.sub('###+', '\n', content)

                # Subtitute white space in first character
                content = re.sub('\.\s\n\s', '\n', content)

                with st.expander(f"Cleaned {x.name}"):
                    st.write(content)

                download_txt_btn = st.download_button(label="Download clean txt data", data=content, file_name='Cleaned_txt.txt')

                if download_txt_btn:
                    with open('Cleaned_' + x.name, "w") as f:
                        f.write(content)
                        st.success('File has been cleaned and downloaded!')

#hide streamlit footer
hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 