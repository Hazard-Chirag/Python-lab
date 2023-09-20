from PyPDF2 import PdfWriter,PdfReader
num1=int(input("Enter the page number from pdf 1"))
num2=int(input("Enter the page number from pdf 2"))
pdf1=open("C:\\coding\\Python lab\\1RN21CS047_CHIRAG_JAVA.pdf",'rb')
pdf2=open("C:\\coding\\Python lab\\1RN21CS047_CHIRAG_JAVA.pdf",'rb')
pdf_writer=PdfWriter()
pdf1_reader=PdfReader(pdf1)
page=pdf1_reader.pages[num1-1]
pdf_writer.add_page(page)
pdf2_reader=PdfReader(pdf2)
page=pdf2_reader.pages[num2-1]
pdf_writer.add_page(page)
with open("C:\\coding\\Python lab\\output.pdf",'wb') as output:
    pdf_writer.write(output)
print("Combined succcesffully")

