import os

SUPPORTED = [".pdf",".docx",".txt",".jpg",".png"]

def scan_folder(folder):

    files = []

    print("\n===================================")
    print("      FILE SCANNING MODULE")
    print("===================================\n")

    for root, dirs, filenames in os.walk(folder):

        for f in filenames:

            if any(f.endswith(ext) for ext in SUPPORTED):
                
                print("Supported File Found :", os.path.join(root, f))
                files.append(os.path.join(root,f))

    return files