import pypdf # biblioteca para manipulação de PDFs

def extract_text_from_pdf(pdf_file):
    """
    Função para extrair texto de um PDF carregando no Streamlit.

    Parâmetros:
    pdf_file (UploadeFile): Arquivo PDF carregado pelo Streamlit.

    Retorna:
    str: Texto extraído do PDF.
    """

    reader = pypdf.PdfReader(pdf_file) # Cria um objeto para 

    # Percorre todas as paginas e extrai o texto
    text = "\n".join(page.extract_text() for page in reader.pages)

    return text #Retorna o texto extraído