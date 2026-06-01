import pdfplumber


def read_pdf(path):

    try:

        text = ""

        with pdfplumber.open(path) as pdf:

            for page in pdf.pages:

                page_text = page.extract_text()

                if page_text:
                    text += page_text

        return text

    except Exception:
        return ""