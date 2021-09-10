"""Configuration settings for this project"""
import tempfile
import os

TMPDIR = os.environ.get("TMPDIR", tempfile.gettempdir())
