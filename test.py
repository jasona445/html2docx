from htmldocx import HtmlToDocx

html = """\
<p>Diagnoses:  </p>
<ol>
<li>Atrial Fibrillation, Paroxysmal (ICD-10 148.0)  </li>
<li>Palpitations (ICD-10 R00.2)</li>
</ol>

<p>Other points:  </p>

<ol>
<li>Hello  </li>
<li>World</li>
</ol>
"""

docx = HtmlToDocx().parse_html_string(html)
docx.save("test.docx")