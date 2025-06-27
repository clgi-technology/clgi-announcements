import os
import sys
from pptx import Presentation
from PIL import Image
import fitz  # PyMuPDF

def pdf_to_pptx(pdf_path, title):
    presentation = Presentation()
    doc = fitz.open(pdf_path)

    for page_num in range(doc.page_count):
        page = doc.load_page(page_num)
        slide = presentation.slides.add_slide(presentation.slide_layouts[5])  # Blank layout
        
        # Add title to slide
        title_box = slide.shapes.title
        title_box.text = f"{title} - Page {page_num + 1}"

        # Render page to image
        pix = page.get_pixmap()
        img_path = f"uploads/page_{page_num}.png"
        pix.save(img_path)

        # Add image to slide
        slide.shapes.add_picture(img_path, 0, 0, width=presentation.slide_width, height=presentation.slide_height)
        os.remove(img_path)

    output_file = f"docs/output/{title.replace(' ', '_')}_presentation.pptx"
    presentation.save(output_file)
    print(f"Presentation saved at {output_file}")
    return output_file

def jpeg_to_pptx(jpeg_path, title):
    presentation = Presentation()
    slide = presentation.slides.add_slide(presentation.slide_layouts[5])
    slide.shapes.add_picture(jpeg_path, 0, 0, width=presentation.slide_width, height=presentation.slide_height)

    output_file = f"docs/output/{title.replace(' ', '_')}_presentation.pptx"
    presentation.save(output_file)
    print(f"JPEG converted and saved at {output_file}")
    return output_file

def main(file_path, title):
    ext = file_path.split('.')[-1].lower()
    if ext == 'pdf':
        return pdf_to_pptx(file_path, title)
    elif ext in ['jpg', 'jpeg']:
        return jpeg_to_pptx(file_path, title)
    else:
        print("Unsupported file type")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python generate_slides.py <file_path> <title>")
        sys.exit(1)

    file_path = sys.argv[1]
    title = sys.argv[2]
    main(file_path, title)
