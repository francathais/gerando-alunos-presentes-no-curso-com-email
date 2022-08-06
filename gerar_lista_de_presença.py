import pandas as pd
from google.colab import files
import io

qtnLimite = 4
uploaded = files.upload() 
dados= pd.read_csv(io.BytesIO(uploaded['participantess.csv']))
listaEmails = dados.values.tolist()
dictEmailsDTO = dict()
for email in listaEmails:
    if str(email) in dictEmailsDTO:
        dictEmailsDTO[str(email)] = dictEmailsDTO[str(email)] + 1
    else:
        dictEmailsDTO[str(email)] = 1
for email, qtn in dictEmailsDTO.items():
    if qtn >= qtnLimite: 
        print(email)

