import sys
from PyPDF2 import PdfReader, PdfWriter
import argparse

def extract_pages(input_pdf_path, output_pdf_path, start_page, end_page):
    reader = PdfReader(input_pdf_path)
    writer = PdfWriter()

    for i in range(start_page - 1, end_page):
        writer.add_page(reader.pages[i])

    with open(output_pdf_path, 'wb') as output_pdf:
        writer.write(output_pdf)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Extract pages from a PDF file.')
    parser.add_argument('input_pdf_path', type=str, help='Path to the input PDF file')
    parser.add_argument('output_pdf_path', type=str, help='Path for the output PDF file')
    parser.add_argument('start_page', type=int, help='Start page number')
    parser.add_argument('end_page', type=int, help='End page number')

    args = parser.parse_args()

    extract_pages(args.input_pdf_path, args.output_pdf_path, args.start_page, args.end_page)
