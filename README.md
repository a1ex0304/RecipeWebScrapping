# What this code does:
- Find the ids for all recipes on the /recipes page
- Navigate and get information from /recipies/[id]/page

Notes about Code:
- BeautifulSoup needs to be used as it takes the html page and turns it into a python object which we can navigate and use

- print(res) throughout the process to ensure that the code is operating properly, it should say "<Response [200]>

- To get the title of each recipe, we inspect element on the website and noticed that the title was the first h1 element of the page, we can use that for the text (same process goes for any element you want to find)

ing_header = soup.find("h2", attrs={"class": "text-3xl font-bold text-[#4e342e] mb-6 flex items-center"})
- Another way to find something is by doing .find, we are using this here because we want to find the "Ingredients" title on each recipe page

ing_header.next_sibling.find_all("span", attrs={"class":"text-[#4e342e] font-medium"})
- Additionally, by looking at the inspect element of the page, we can see that beside the h2 line (Ingredients title) is a div class that has spans in it
- These spans are used for the Ingredient List, thus we use .next_sibling in order to find the next line in the inspect element which is the Ingredient List
- We cant use Divs as it is a placeholder
- We use find.all to get all the ingredients of all the recipes on the website 

To Run Code:
1. Make sure Python is downloaded
2. Create Virtual Environment
- python -m venv venv
- venv/Scripts/activate
3. Installing dependencies
- pip install requests beautifulsoup4

If Permission is denied:
1. Make sure you are in directory that you are allowed to make folders in
2. If still doesnt work then use set-executionpolicy remotesigned
