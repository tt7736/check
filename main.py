from pyscript import document
print("Hello World, from the web!")
output_div = document.querySelector("#textarea")
output_div.innerText = "Hello World, from the web!"