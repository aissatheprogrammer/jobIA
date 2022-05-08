import os
import requests

from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential

import pdfplumber


def extract_entities(cog_key, cog_endpoint, CVpdf):
    """ Extrait les entités d'un document pdf donné en paramètre

        Parameters
        ----------
        cog_key : str
            Clé secrète de l'API

        cog_endpoint : str
            Endpoint de l'API

        pdf : File
            Le CV en format pdf.

        Return
        ------
        result_dict : dict
            Dictionnaire contenant les résultats de la NER

    """
    # Authenticate the client using your key and endpoint
    def authenticate_client():
        ta_credential = AzureKeyCredential(cog_key)
        text_analytics_client = TextAnalyticsClient(
            endpoint=cog_endpoint,
            credential=ta_credential)
        return text_analytics_client

    client = authenticate_client()

    # Extraction du texte du pdf

    with pdfplumber.open(CVpdf) as pdf:
        text = "".join(page.extract_text() for page in pdf.pages)

    # Fonction d'appel de l'API qui extrait les skills du cv

    def entity_recognition(client):

        try:
            documents = [
                {
                    "id": "1",
                    "language": "fr",
                    "text": text,
                }
            ]

            result = client.recognize_entities(documents=documents)[0]

            #print("Named Entities:\n")

            result_dict = {"resultats": []}

            for entity in result.entities:
                # print("\tText: \t", entity.text, "\tCategory: \t", entity.category, "\tSubCategory: \t", entity.subcategory,
                # "\n\tConfidence Score: \t", round(entity.confidence_score, 2), "\tLength: \t", entity.length, "\tOffset: \t", entity.offset, "\n") # Convertir en dico

                res = {
                    'text': entity.text,
                    'category': entity.category,
                    'subcategory': entity.subcategory,
                    'confidence_score': entity.confidence_score,
                    'length': entity.length,
                    'offset': entity.offset,
                }

                result_dict["resultats"].append(res)

        except Exception as err:
            print("Encountered exception. {}".format(err))

        return result_dict

    return entity_recognition(client)


def extract_skills_from_entities(entities):
    """ Extrait les skills des entités résultats de l'appel d'API 

        Parameters
        ----------
        entities : dict
            Dictionnaire contenant une liste des dictionnaires correspondant aux différentes entités

        Return
        ------
        skills : list
            Liste des compétences extraites des entités

    """

    skills = []

    for entity in entities['resultats']:
        if entity['category'] == 'Skill' and entity['confidence_score'] > 0.9:
            skills.append(entity['text'])

    return skills
