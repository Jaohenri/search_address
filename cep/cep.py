import requests

while True:
    cep = input("Please inform your cep: ")
    if cep.isdigit():
        break
    print("Invalid cep, must be only numbers.")

response = requests.get(f"https://viacep.com.br/ws/{cep}/json/").json()

# Exibindo o conteúdo da resposta
print(f"State: {response.get('uf')}\n"
      f"City: {response.get('localidade')}\n"
      f"Neighborhood: {response.get('bairro')}\n"
      f"Street: {response.get('logradouro')}\n"
      )
