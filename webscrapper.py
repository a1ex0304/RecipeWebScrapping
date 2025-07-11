import requests #make a http request from the source (all information)
from bs4 import BeautifulSoup

URL_ENDPOINT = "https://pizza-site-six.vercel.app"

res = requests.get(URL_ENDPOINT+"/recipes") #get the information and put under res variable
soup = BeautifulSoup(res.text) #Passed in the html value into the constructor of this class
#We made a Python object which is easier to navigate through

anchor_list=soup.find_all("a", attrs={"class":"inline-block mt-4 px-4 py-2 bg-[#d32f2f] text-white rounded-lg hover:bg-[#b71c1c] transition-colors duration-300"})#Find all anchor tags from the "View Recipe" Button

recipes = {} #Make dictonary to store all information about recipes

for anchor in anchor_list:
    res = requests.get(URL_ENDPOINT+anchor["href"]) #This gets the link of the detail page of every recipe
    soup = BeautifulSoup(res.text, "html.parser") #This puts all of the links of the detail pages of the recipe into a Python Object making it easier to navigate through
    
    #Name
    recipe_title = soup.h1.text #Get the title of each recipe
    
    #Recipe
    recipe_img = soup.img["src"] #Get the image of each recipe

    #Find the Headers for Ingredients and Instructions
    headers = soup.find_all("h2", attrs={"class": "text-3xl font-bold text-[#4e342e] mb-6 flex items-center"})
    ing_header = headers[0] #Get the first occurance of the header
    ins_header = headers[1] #Get the second occurance of the header

    #Ingredients
    ingredients = ing_header.next_sibling.find_all("span", attrs={"class":"text-[#4e342e] font-medium"})
    
    recipe_ingredients = [] #Store all ingredients in this
    for ingredient in ingredients: #This for loop allows us just to print the ingredient name and none of the unwanted html parts
        recipe_ingredients.append(ingredient.text)

    #Instruction and Instruction List
    instructions = ins_header.next_sibling.find_all("p", attrs={"class":"text-[#6d4c41] leading-relaxed pt-1"})

    recipe_instructions = []
    for instruction in instructions:
        recipe_instructions.append(instruction.text)

    recipes[anchor["href"]] = {
        "name": recipe_title,
        "img": recipe_img,
        "ingredients": recipe_ingredients,
        "instructions": recipe_instructions,
        #We are going to add each name, image, ingredient list and instruction list of each recipe into the dictionary
    }
    
print(recipes)