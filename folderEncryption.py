import pyminizip
import os

files_name = ["C:/All_share/RFP/Field_photography_tender.xls", "C:/All_share/RFP/tender.docx"]
prefix = ["", ""]
zip_name = os.path.join("C:/", "All_share.zip")
password = "Hacked1!"
level = 4
pyminizip.compress_multiple(files_name, prefix, zip_name, password, level)
