import pdfplumber

import re


def extract_skills_resume(CVpdf, skills=['Java', 'Python', 'HTml', 'CSS', 'javascript', 'php', 'R', 'Ruby', 'Perl', 'Matlab', 'Scala', 'Excel', 'Tableau', 'D3.js', 'SAS', 'SPSS', 'D3', 'Hadoop', 'MapReduce', 'Spark', 'Pig', 'Hive', 'Shark', 'Oozie', 'ZooKeeper', 'Flume', 'Mahout', 'SQL', 'NoSQL', 'HBase', 'Cassandra', 'MongoDB', 'Flask', 'Django', 'FastAPI', 'Metabase', 'Azure']):
    """Retourne une liste de compétences du CV qui matchent avec les compétences fournies en paramètre

        Parameters
        ----------
        pdf : File
            Le CV en format pdf.

        skills : list
            Liste des compétences à matcher

        Return
        ------
        matched_skills : list
            Liste des compétences qui matchent avec le cv

        """
    with pdfplumber.open(CVpdf) as pdf:

        text = "".join(page.extract_text() for page in pdf.pages)

        matched_skills = []
        for skill in skills:
            match = re.search(rf'[\s|,|.|;|:]+\b({skill.lower()})\b[\s|,|.|;|:]+',
                              text.lower())
            if match:
                matched_skills.append(match.group(1))

        return matched_skills


# Tests

#print(extract_skills_resume('Cv_Marouan_Boulli_DevIA (1).pdf'))
'''
# Extraire text avec pdfminer

 output_string = StringIO()
    with open(pdf, 'rb') as in_file:
        parser = PDFParser(in_file)
        doc = PDFDocument(parser)
        rsrcmgr = PDFResourceManager()
        device = TextConverter(rsrcmgr, output_string, laparams=LAParams())
        interpreter = PDFPageInterpreter(rsrcmgr, device)
        for page in PDFPage.create_pages(doc):
            interpreter.process_page(page)
'''
'''
total_length = 0
cv_combined = ""
with pdfplumber.open('Cv_Marouan_Boulli_DevIA (1).pdf') as pdf:
    text = "".join(page.extract_text() for page in pdf.pages)
    cv_combined += text

with pdfplumber.open('Cv_Aissa.pdf') as pdf:
    text = "".join(page.extract_text() for page in pdf.pages)
    cv_combined += text

with pdfplumber.open('CV_Modifie_Nolan_1.pdf') as pdf:
    text = "".join(page.extract_text() for page in pdf.pages)
    cv_combined += text

with pdfplumber.open('Cv_ThienVu.pdf') as pdf:
    text = "".join(page.extract_text() for page in pdf.pages)
    cv_combined += text

with pdfplumber.open('CV_Gabriel_CAFERRA_Dev_Data_Junior.pdf') as pdf:
    text = "".join(page.extract_text() for page in pdf.pages)
    cv_combined += text
'''
