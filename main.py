import os
from PIL import Image
from PyPDF2 import PdfReader, PdfWriter


def remeta_img(file_name):
    image = Image.open('files/' + file_name)
    image.save('files_without_meta/' + file_name)


def remeta_pdf(file_name):
    reader = PdfReader('files/' + file_name)
    writer = PdfWriter()

    for page in reader.pages:
        writer.add_page(page)

    writer.add_metadata(
        {
            "/Author": "GrottBjorn",
            "/Producer": ""
        }
    )

    with open('files_without_meta/' + file_name, "wb") as f:
        writer.write(f)


directory_with_meta = 'files'
directory_no_meta = 'files_without_meta'

dir_directory = os.listdir(directory_with_meta)
print(f'Список файлов в папке files: ', end='')
print(*dir_directory, sep=', ')

for file in dir_directory:
    if file[-4:] == '.jpg':
        remeta_img(file)
    elif file[-4:] == '.pdf':
        remeta_pdf(file)


