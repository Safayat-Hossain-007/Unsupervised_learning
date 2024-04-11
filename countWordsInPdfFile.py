import os
import PyPDF2


# Function to count words in a text
def count_words(text):
    words = text.split()
    return len(words)


# Replace 'path/to/folder' with the actual path to the folder containing PDF files
folder_path = '/home/safayat/Desktop/4 th year 1st semester/Research works/pythonProject/DeepLearning'  # Example path on Linux

# Check if the folder exists
if os.path.exists(folder_path):
    # Iterate over each file in the folder
    for filename in os.listdir(folder_path):
        # Check if the file is a PDF
        if filename.endswith('.pdf'):
            # Get the full path of the PDF file
            pdf_file_path = os.path.join(folder_path, filename)

            # Open the PDF file
            with open(pdf_file_path, 'rb') as file:
                # Create a PDF reader object
                pdf_reader = PyPDF2.PdfReader(file)

                # Initialize word count
                total_words = 0

                # Iterate through each page and extract text
                for page_number in range(len(pdf_reader.pages)):
                    page = pdf_reader.pages[page_number]
                    text = page.extract_text()

                    # Count words in the extracted text
                    page_words = count_words(text)
                    total_words += page_words

                print(f"{filename}: {total_words} words")
else:
    print("Folder does not exist.")
