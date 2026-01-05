

import requests

class Cep:
    def __init__(self, cep):
        self.cep = cep
        self.cleaned_cep = self.clean_cep()

        if self.cleaned_cep != None:
            self.response = self.search_cep()

            if self.response.get("erro"):
                print("The cep inputed doesn't exist.")
            else:
                self.state = self.response.get('uf')
                self.city = self.response.get('localidade')
                self.neighborhood = self.response.get('bairro')
                self.street = self.response.get('logradouro')
                
                self.display_cep()
        

    def clean_cep(self):
        if self.cep.isdigit() and self.cep.len() == 8:
            return self.cep
        else:
            print("Invalid cep, must be 8 numbers.")
            return None
    
    def search_cep(self):
        self.response = requests.get(f"https://viacep.com.br/ws/{self.cleaned_cep}/json/").json()
        return self.response
    
    def display_cep(self):
        print(f"State: {self.state}\n"
              f"City: {self.city}\n"
              f"Neighborhood: {self.neighborhood}\n"
              f"Street: {self.street}\n"
             )