"""Module to run the CEP lookup application."""

from search_cep.cep import Cep
from search_cep.connection import test_connection

if __name__ == "__main__":

    while True:

        print("\nCep lookup application.")
        print("\n-----------------------\n")
        if test_connection() is False:
            break
        cep1 = Cep(input("Please inform a cep: "))



        state = input("Do you want to search another Cep? Y/N?")

        if state.lower() == "n":
            break
