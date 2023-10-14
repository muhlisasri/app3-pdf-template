from fpdf import FPDF
import pandas as pd

df = pd.read_csv("topics.csv")
pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.set_auto_page_break(auto=False)

for index, row in df.iterrows():
    pdf.add_page()
    pdf.set_font(family="Times", style="B", size=24)
    pdf.set_text_color(100,100,100)
    pdf.cell(w=0, h=12, txt=row["Topic"], border=0, ln=1)
    for i in range(21,290, 10):
        pdf.line(10,i, 200,i)

    # Set the footer
    pdf.ln(260)
    pdf.set_font(family="Times", style="I", size=12)
    pdf.set_text_color(100,100,100)
    pdf.cell(w=0,h=12, txt=row["Topic"], border=0, ln=1, align="R")

    for page in range(row["Pages"] - 1) :
        pdf.add_page()

        # Set the footer
        pdf.ln(272)
        pdf.set_font(family="Times", style="I", size=12)
        pdf.set_text_color(100, 100, 100)
        pdf.cell(w=0, h=12, txt=row["Topic"], border=0, ln=1, align="R")
        for i in range(21, 290, 10):
            pdf.line(10, i, 200, i)

pdf.output("Output.pdf")