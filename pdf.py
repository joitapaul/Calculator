# from PyPDF2 import PdfWriter

# merger = PdfWriter()

# pdfs = []
# n = int(input("How mny pdfs do you want to merge?\n"))

# for i in range(0,n):
#     name = input("Enter the name of {i +1} pdf :")
#     pdfs.append(name)

# for in pdfs:
#     merger.append(pdf)

# merger.write("merged-pdf.pdf")
# merger.close()
from PyPDF2 import PdfMerger

merger = PdfMerger()

pdfs = []
n = int(input("How many PDFs do you want to merge?\n"))

for i in range(n):
    name = input(f"Enter the name of PDF {i + 1} (with .pdf extension): ")
    pdfs.append(name)

for pdf in pdfs:
    merger.append(pdf)

merger.write("merged-pdf.pdf")
merger.close()
print("PDFs have been successfully merged into 'merged-pdf.pdf'")
