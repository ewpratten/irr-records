import argparse
from pathlib import Path
import sys
from typing import List

def get_all_object_files() -> List[Path]:
    globs = [
        Path("as-set").glob("AS*"),
        Path("aut-num").glob("AS*"),
        Path("mntner").glob("MAINT*"),
        Path("route").glob("*"),
        Path("route6").glob("*"),
    ]
    
    # Collect all files
    files: List[Path] = []
    for g in globs:
        files.extend(g)
    
    return files
    

def main() -> int:
    # Handle program arguments
    ap = argparse.ArgumentParser()
    ap.add_argument("-p", "--password", help="Password to use",
                    required=True, type=str)
    ap.add_argument("-o", "--object", help="Object(s) to process", nargs="+", type=Path)
    args = ap.parse_args()

    # Collect all objects in the subdirs
    object_files = args.object or get_all_object_files()
    objects: List[str] = []
    for f in object_files:
        obj = f.read_text().strip()
        obj += f"\npassword: {args.password}\n"
        objects.append(obj)

    # Print all objects
    for obj in objects:
        print(obj)
        print()

    return 0


if __name__ == "__main__":
    sys.exit(main())
