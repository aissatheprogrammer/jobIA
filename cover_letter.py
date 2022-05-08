import openai
import os
import requests

from dotenv import load_dotenv

load_dotenv()

openai.organization = "org-sz0SCdbsgwE1PZy0iGKtlfkl"
openai.api_key = os.getenv("OPENAI_API_KEY")
openai.Engine.list()


def cover_letter(intitule: str, keywords: str, profil: str key=openai.api_key) -> str:
    """
    Generate a cover letter for a job offer according to its title and keywords


    Parameters
    ----------
    intitule : str
        Title of the job offer
    keywords : str
        Keywords in the description of the job offer
    profil : str
        Profile of the user
    key : str
        Openai API key 

    Returns
    -------
    str
        A cover letter adapted to the informations contained in the job offer

    """
    headers = {'Content-Type': 'application/json',
               'Authorization': f'Bearer {key}'}

    url = 'https://api.openai.com/v1/engines/text-davinci-001/completions'

    body = {
        'prompt': f'Rédige moi une lettre de motivation pour le poste de {intitule} , adaptée à mon profil qui suit : {profil}. Elle doit contenir les mots-clés suivants : {keywords}',
        'max_tokens': 1900
    }

    response = requests.post(url, json=body, headers=headers)

    letter = response.json()['choices'][0]['text']

    return letter
