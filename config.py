import os

class Config:
    UPLOADS_DIR = "uploads"
    ALLOWED_FILES = {
        "ttf",
        "pdf",
        "otf",
        "woff",
        "woff2",
        "png",
        "jpg",
        "jpeg",
        "klwp",
        "tiff",
        "gif",
        "webm",
        "md",
        "pptx",
        "ppsx",
        "odt",
        "odp",
        "docx",
        "xslx",
        "txt",
        "gz",
        "bz2",
        "xz",
        "tar",
        "zip",
        "opus",
        "flac",
        "mp3",
    }
    SECRET_KEY = os.urandom(24)
    FILENAME_LEN = 5
