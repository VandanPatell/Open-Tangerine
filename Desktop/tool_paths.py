"""Locate optional, locally installed converters without downloading binaries."""
import os
from pathlib import Path
import shutil


def find_tool(kind, configured=''):
    candidates = [configured] if configured else []
    command = 'ffmpeg' if kind == 'ffmpeg' else 'soffice'
    candidates.append(shutil.which(command))
    if kind == 'office' and os.name == 'nt':
        for root in ('ProgramFiles', 'ProgramFiles(x86)'):
            folder = os.environ.get(root)
            if folder:
                candidates.append(str(Path(folder)/'LibreOffice/program/soffice.com'))
                candidates.append(str(Path(folder)/'LibreOffice/program/soffice.exe'))
    for candidate in candidates:
        if candidate:
            path = Path(candidate)
            if path.is_absolute() and path.is_file() and not path.is_symlink():
                return str(path)
    return ''
