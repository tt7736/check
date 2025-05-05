from pyscript import document

# from dotenv import load_dotenv
# load_dotenv()
#import os
import supabase
url = "https://hmiyzverkplczwioalal.supabase.co"
key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImhtaXl6dmVya3BsY3p3aW9hbGFsIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NDYzNzk5MDgsImV4cCI6MjA2MTk1NTkwOH0.3uRdyRC8A_q9Mk7InN2CAtLSEGd7ffj7C9TNd4shEnA"
db = supabase.create_client(url, key)


def translate_english(event):
    input_text = document.querySelector("#english")
    english = input_text.value
    output_div = document.querySelector("#output")
    if english=="114458":
        output_div.innerText = "Hallo, du bist eingeloggt!"
        data = db.table("todos").insert({"name":english}).execute()
    else:
        output_div.innerText = "Falsch, du nudde!"