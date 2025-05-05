import arrr
from pyscript import document
from supabase import create_client
# from dotenv import load_dotenv
# load_dotenv()

#import os


def translate_english(event):

    url = "https://hmiyzverkplczwioalal.supabase.co"
    key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImhtaXl6dmVya3BsY3p3aW9hbGFsIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NDYzNzk5MDgsImV4cCI6MjA2MTk1NTkwOH0.3uRdyRC8A_q9Mk7InN2CAtLSEGd7ffj7C9TNd4shEnA"
    supabase = create_client(url, key)
    
    input_text = document.querySelector("#english")
    english = input_text.value
    output_div = document.querySelector("#output")
    if english=="114458":
        output_div.innerText = "Hallo, du bist eingeloggt!"
        data = supabase.table("todos").insert(english).execute()
    else:
        output_div.innerText = "Falsch, du nudde!"