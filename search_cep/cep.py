"""Module for CEP lookup using the ViaCEP public API."""

import requests

class Cep:
    """Represents a Brazilian CEP and retrieves its address information.

    Upon instantiation, the CEP is validated and queried using the ViaCEP API.
    If the CEP exists, address attributes such as state, city, neighborhood
    and street are populated and displayed.

    Attributes:
        cep (str): Original CEP provided by the user.
        cleaned_cep (str): Validated CEP containing only digits.
        state (str): State (UF) returned by the API.
        city (str): City returned by the API.
        neighborhood (str): Neighborhood returned by the API.
        street (str): Street returned by the API.
    """
    def __init__(self, cep: str) -> None:
        """Initializes a CEP instance and performs an automatic lookup.

        The CEP is validated, queried using the ViaCEP API and, if found,
        the address information is stored in the instance and printed to stdout.

        Args:
            cep (str): CEP (Código de Endereçamento Postal) number.
        """
        self.cep = cep
        self.cleaned_cep: str = self.validate_cep()

        if self.cleaned_cep is not None:
            self.response: dict = self.search_cep()

            if self.response.get("erro"):
                print("The cep inputed doesn't exist.")

            else:
                self.state: str = self.response.get('uf')
                self.city: str = self.response.get('localidade')
                self.neighborhood: str = self.response.get('bairro')
                self.street: str = self.response.get('logradouro')

                self.display_cep()

    def validate_cep(self) -> str:
        """Validates whether the CEP contains only numeric characters.

        Returns:
            str | None: The CEP if it contains only digits, otherwise None.
        """
        if self.cep.isdigit():
            return self.cep

        print("Invalid cep, must be 8 numbers.")

        return None


    def search_cep(self):
        """Queries the ViaCEP API for information about the validated CEP.

        Returns:
            dict: JSON response returned by the ViaCEP API.
        """
        return requests.get(f"https://viacep.com.br/ws/{self.cleaned_cep}/json/", timeout=10).json()

    def display_cep(self):
        """Prints the retrieved address information."""
        print(f"\nState: {self.state}\n"
              f"City: {self.city}\n"
              f"Neighborhood: {self.neighborhood}\n"
              f"Street: {self.street}\n"
             )
