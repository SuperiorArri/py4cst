import py4cst.cst_file_utils as cfu
import pathlib

# CST files are custom type of archive, the contained files can be extracted
#  with this script

out_dir = 'path/to/output/dir'
cst_file = cfu.decode('path/to/project.cst')

for file_name, ent in cst_file.items():
    dst = pathlib.Path(out_dir, file_name)
    dst.parent.mkdir(parents=True, exist_ok=True)
    dst.write_bytes(ent.content)
