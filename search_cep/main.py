"""Module to run the CEP lookup application."""

try:
    from .cep import Cep
    from .__init__ import test_conection
except ImportError:
    from cep import Cep
    from __init__ import test_conection


if __name__ == "__main__":

    while True:

        print("\nCep lookup application.")
        print("\n-----------------------\n")
        if test_conection() is False:
            break
        cep1 = Cep(input("Please inform a cep: "))



        state = input("Do you want to search another Cep? Y/N?")

        if state.lower() == "n":
            break
