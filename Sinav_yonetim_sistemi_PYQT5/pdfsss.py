from fpdf import FPDF
import sys

pdf = FPDF()
# compression is not yet supported in py3k version
pdf.compress = False
pdf.add_page()
# Unicode is not yet supported in the py3k version; use windows-1252 standard font
pdf.set_font('Arial', '', 14)
pdf.ln(10)
pdf.write(5, 'hello world %s şçüğáéíóúüñ' % sys.version)

pdf.output('py3k.pdf', 'F')