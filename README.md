Este projeto automatiza a busca de informações de empresas no Google Maps a partir de uma planilha de input (arquivo.xlsx).

**Como usar**

1. Baixe o repositório.
2. Coloque os nomes das empresas no arquivo "Lista de Empresas.xlsx".
3. Execute o arquivo "desafio.exe".
4. Os resultados serão salvos no arquivo "dados.xlsx".
5. O arquivo de input deve estar **NA MESMA PASTA** que o arquivo executável.

**Requisitos**

- Google Chrome instalado.
- ChromeDriver compatível com a versão do Chrome.

**Exemplo de Input**

|  Empresa  |
|-----------|
| Nome 1    |
| Nome 2    |
| Nome 3    |

**Exemplo de Output**

| Empresa       | Endereço       |Rating|
|---------------|----------------|------|
| Nome 1        | Endereço, CEP  | 4.8  |
| Nome 2        | Endereço, CEP  | 4.6  |
| Nome 3        | Endereço, CEP  | 4.7  |
