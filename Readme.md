# PDF Generation using csv files

* Here we have used csv file to get the data.
* Topics.csv is used for Title/topics.

# ________________***PDF Generation using data from CSV***________________

from fpdf import FPDF
import pandas as pd

# Creating a PDF object
pdf = FPDF(orientation='p', unit="mm", format="A4")

# Setting the font for the PDF
pdf.set_font(family="Arial", style="B", size=12)

# Importing the pandas library

# Reading data from the CSV file
df_pdf = pd.read_csv("Topics.csv", sep=",")

# Iterating over each row in the DataFrame
for index, row in df_pdf.iterrows():
    # Extracting the topic from the current row
    topic = row["Topic"]
    
    # Adding a new page to the PDF
    pdf.add_page()
    
    # Adding a cell with the topic text to the PDF
    pdf.cell(w=0, h=12, txt=topic, border=0, ln=1)

# Saving the generated PDF document
pdf.output("output.pdf")