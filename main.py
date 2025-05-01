import arrr
from pyscript import document


def translate_english(event):
    input_text = document.querySelector("#english")
    english = input_text.value
    output_div = document.querySelector("#output")
    if english=="114458":
        output_div.innerText = "Hallo, du bist eingeloggt!"
    else:
        output_div.innerText = "Falsch, du nudde!"