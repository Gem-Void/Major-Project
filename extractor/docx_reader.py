from docx import Document


def read_docx(path):

    try:

        doc = Document(path)

        text = ""

        for para in doc.paragraphs:
            text += para.text + "\n"

        return text

    except Exception:
        return ""