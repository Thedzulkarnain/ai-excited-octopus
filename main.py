import hashlib
import shutil
from pathlib import Path

SRC = Path(__file__).with_name("art.jpg")
OUT = Path("/output/entry.png")

OUT.parent.mkdir(parents=True, exist_ok=True)
shutil.copyfile(SRC, OUT)
digest = hashlib.sha256(OUT.read_bytes()).hexdigest()
print(f"wrote {OUT} ({OUT.stat().st_size} bytes) sha256={digest}")
