import fitz


def extract_resume_text(uploaded_file):
    """
    Extract text from a PDF resume.

    Parameters
    ----------
    uploaded_file : UploadedFile
        Streamlit uploaded PDF file.

    Returns
    -------
    str
        Extracted text from the PDF.
    """

    text = ""

    pdf = fitz.open(stream=uploaded_file.read(), filetype="pdf")

    for page in pdf:
        text += page.get_text()

    pdf.close()

    return text.strip()