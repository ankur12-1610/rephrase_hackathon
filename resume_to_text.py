# importing required modules
from PyPDF2 import PdfReader
 
# creating a pdf reader object
reader = PdfReader('Ankur_Resume.pdf')
 
# printing number of pages in pdf file
print(len(reader.pages))
 
# getting a specific page from the pdf file
page = reader.pages[0]
 
# extracting text from page
text = page.extract_text()
print("Extracting text from the uplaoded file...")
print("----------------------------------"+"The extracted text is:"+"----------------------------------")
print(text)
f = open("resume_text.txt", "w")
f.write(text)
f.close()