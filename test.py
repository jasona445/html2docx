from htmldocx import HtmlToDocx

html = """\
<p>Diagnoses:  </p>
<ol id="1">
<li id="a1">Atrial Fibrillation, Paroxysmal (ICD-10 148.0)  </li>
<li id="a2">Palpitations (ICD-10 R00.2)</li>
</ol>

<p>Other points:  </p>

<ol id="2">
<li id="b1" >Hello  </li>
<li id="b2">World</li>
</ol>
"""

docx = HtmlToDocx().parse_html_string(html)
docx.save("test.docx")