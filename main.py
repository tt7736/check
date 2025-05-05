import arrr
from pyscript import document


def translate_english(event):
    input_text = document.querySelector("#english")
    english = input_text.value
    output_div = document.querySelector("#output")
    output_div.innerText = arrr.translate(english)

def save(event):
    input_text = document.querySelector("#english")
    english = input_text.value
    from supabase import create_client

    url = "https://hmiyzverkplczwioalal.supabase.co"
    key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImhtaXl6dmVya3BsY3p3aW9hbGFsIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NDYzNzk5MDgsImV4cCI6MjA2MTk1NTkwOH0.3uRdyRC8A_q9Mk7InN2CAtLSEGd7ffj7C9TNd4shEnA"
    supabase = create_client(url, key)
    data = supabase.table("todos").insert({"name":english}).execute()

