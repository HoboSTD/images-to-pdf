#!/usr/bin/python3
import sys, os
from fpdf import FPDF
from PIL import Image, ImageOps

P_WIDTH = 210
P_HEIGHT = 297

def rotate_image(path: str) -> str:
    """
    Applies the EXIF rotation and saves it as a temporary file.
    """

    def create_tmp_path(path: str) -> str:
        """
        Returns a temporary path for this image.
        """

        try:
            slash_index = path.index("/")
            return path[0:slash_index + 1] + "JHBFN29774T4_" + path[slash_index+1:]
        except:
            return "JHBFN29774T4_" + path

    image = Image.open(path)
    image = ImageOps.exif_transpose(image)
    path = create_tmp_path(path)
    image.save(path)
    image.close()

    return path

class PDF(FPDF):

    def add_image(self, path: str):
        """
        Adds an image so that it takes up the whole page.
        """
        self.add_page()
        self.set_auto_page_break(False, 0)
        self.set_xy(0, 0)
        self.set_margins(0, 0)
        path = rotate_image(path)
        self.image(path, link="", w=P_WIDTH, h=P_HEIGHT)
        os.remove(path)

if __name__ == "__main__":

    if len(sys.argv) == 2:
        pdf = PDF()
        try:
            s = input()
            while len(s) > 0:
                pdf.add_image(s)
                s = input()
        except EOFError:
            pass

        name = sys.argv[1]
        if not name.endswith(".pdf"):
            name += ".pdf"

        pdf.output(name, "")
