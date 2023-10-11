from pico_solver import PicoSolver
import requests


class ObedientCat(PicoSolver):

    def get_description(self) -> str:
        return "This file has a flag in plain sight (aka \"in-the-clear\")."

    def solve(self) -> str:
        return requests.get("https://mercury.picoctf.net/static/2d24d50b4ebed90c704575627f1f57b2/flag").text.strip()

    def get_name(self) -> str:
        return "Obedient Cat"
