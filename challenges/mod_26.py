from pico_solver import PicoSolver


class Mod26(PicoSolver):

    ciphertext: str = "cvpbPGS{arkg_gvzr_V'yy_gel_2_ebhaqf_bs_ebg13_nSkgmDJE}"

    def get_name(self) -> str:
        return "Mod 26"

    def get_description(self) -> str:
        return "Cryptography can be easy, do you know what ROT13 is?"

    def solve(self) -> str:
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        out = ""
        for i in self.ciphertext:
            letter = i.lower()
            if letter in alphabet:
                letter = alphabet[(alphabet.index(letter) + 13) % 26]
            out += letter if i.lower() == i else letter.upper()
        return out
