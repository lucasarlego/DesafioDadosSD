import pandas as pd

path = r"C:\Users\arleg\OneDrive\Documentos\DesafioDadosSD\Desafio_1\archive\AdventureWorks_Returns.csv"


df = pd.read_csv(
    path,
    parse_dates=["ReturnDate"],
    dayfirst=True,
    encoding="latin1",
)

df["ReturnDate"] = df["ReturnDate"].dt.strftime("%Y/%m/%d")


new_path = r"C:\Users\arleg\OneDrive\Documentos\DesafioDadosSD\Desafio_1\archive\arquivo_tratado\AdventureWorks_Returns_tratado.csv"
df.to_csv(new_path, index=False)
