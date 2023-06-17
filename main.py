# ________________***PDF Generation using data from CSV***________________

from fpdf import FPDF

pdf = FPDF(orientation='p', unit="mm", format="A4")


pdf.set_font(family="Arial", style="B", size=12)

import pandas as pd

df_pdf = pd.read_csv("Topics.csv", sep=",")

for index, row in df_pdf.iterrows():
    topic = row["Topic"]
    pdf.add_page()
    pdf.cell(w=0, h=12, txt=topic, border=0,ln=1)

pdf.output("output.pdf")