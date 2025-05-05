import arrr
from pyscript import document
from dotenv import load_dotenv
load_dotenv()

import os
from supabase import create_client

url = os.environ.get("SUPABASE_URL")
key = os.environ.get("SUPABASE_KEY")
supabase = create_client(url, key)


def translate_english(event):
    input_text = document.querySelector("#english")
    english = input_text.value
    output_div = document.querySelector("#output")
    if english=="114458":
        output_div.innerText = "Hallo, du bist eingeloggt!"
        data = supabase.table("todos").insert(english).execute()
    else:
        output_div.innerText = "Falsch, du nudde!"