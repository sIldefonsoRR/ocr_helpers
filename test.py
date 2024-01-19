from llms.jina import Jina
from modules.module_tesseract import Module_Tesseract

local_image_path = "examples/ocr_image.png"
output_json_path = "examples/ocr_image_2.json"
output_txt_path = "examples/ocr_image.txt"

# JINA
jina_worker = Jina()
jina_worker.call_llm(local_image_path, output_json_path)

# PyTesseract
ocr_language = "chi_tra"
tesseract_worker = Module_Tesseract()
tesseract_worker.apply_ocr(local_image_path, output_txt_path,
                           language=ocr_language)
