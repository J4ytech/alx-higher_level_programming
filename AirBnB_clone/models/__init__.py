#!/usr/bin/python3
"""Creates the storage object."""

from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()