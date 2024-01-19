from .module_base import Module_Base
from PIL import Image
import pytesseract
from unidecode import unidecode


class Module_Tesseract(Module_Base):

    def __init__(self) -> None:
        super().__init__()

    def apply_ocr(self, local_image_path, output_file_path, language='en'):
        text = \
            unidecode(((pytesseract.image_to_string(Image.open(local_image_path), # noqa
                                                    lang=language))))
        with open(output_file_path, 'w') as fp:
            fp.write(text)
