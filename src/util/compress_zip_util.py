from io import BytesIO
from zipfile import ZipFile, ZIP_DEFLATED


def compress_several_files_to_zip(files: any, filename: str) -> BytesIO:
    buffer = BytesIO()

    with ZipFile(buffer, "w", ZIP_DEFLATED) as zips:
        for name, content in files:
            content.seek(0)
            zips.writestr(name, content.read())

    buffer.seek(0)
    return buffer
