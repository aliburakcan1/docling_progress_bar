from docling.document_converter import DocumentConverter
import logging

logging.basicConfig(level=logging.NOTSET)
source = "./tests/data/pdf/2206.01062.pdf"

converter = DocumentConverter()
result = converter.convert(source)
print(result.document.export_to_markdown())