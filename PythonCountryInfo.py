# Programmer - python_scripts (Abhijith Warrier)

# PYTHON GUI TO GET THE INFORMATAION ABOUT ALL THE COUNTRIES USING REST Countries API

# Importing necessary packages
import io
import requests
import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
from tkinter.ttk import Combobox

# Defining CreateWidgets() function to create necessary tkinter widgets
def CreateWidgets():
    countryLabel = Label(root, text="SELECT COUNTRY : ", bg="slateblue4")
    countryLabel.grid(row=0, column=0, padx=10, pady=5)
    root.countryList = Combobox(root, width=34, state="readonly", background="black")
    root.countryList.grid(row=0, column=1, padx=5, pady=5)

    getInfoButton = Button(root, text="INFO", command=getCountryInfo)
    getInfoButton.grid(row=1, column=0, padx=5, pady=5, columnspan=2)

    clearButton = Button(root, text="CLEAR", command=clearEntries)
    clearButton.grid(row=1, column=1, padx=5, pady=5, columnspan = 2)

    officialNameLabel = Label(root, text="OFFICIAL NAME : ", bg="slateblue4")
    officialNameLabel.grid(row=2, column=0, padx=10, pady=5)
    root.officialName = Label(root, width=36, bg="black")
    root.officialName.grid(row=2, column=1, padx=10, pady=5)

    capitalLabel = Label(root, text="CAPITAL : ", bg="slateblue4")
    capitalLabel.grid(row=3, column=0, padx=10, pady=5)
    root.capital = Label(root, width=36, bg="black")
    root.capital.grid(row=3, column=1, padx=10, pady=5)

    continentLabel = Label(root, text="CONTINENT : ", bg="slateblue4")
    continentLabel.grid(row=4, column=0, padx=10, pady=5)
    root.continent = Label(root, width=36, bg="black")
    root.continent.grid(row=4, column=1, padx=10, pady=5)

    populationLabel = Label(root, text="POPULATION : ", bg="slateblue4")
    populationLabel.grid(row=5, column=0, padx=10, pady=5)
    root.population = Label(root, width=36, bg="black")
    root.population.grid(row=5, column=1, padx=10, pady=5)

    currencyLabel = Label(root, text="CURRENCY : ", bg="slateblue4")
    currencyLabel.grid(row=6, column=0, padx=10, pady=5)
    root.currency = Label(root, width=36, bg="black")
    root.currency.grid(row=6, column=1, padx=10, pady=5)

    timezoneLabel = Label(root, text="TIMEZONES : ", bg="slateblue4")
    timezoneLabel.grid(row=6, column=0, padx=10, pady=5)
    root.timezones = Label(root, width=36, bg="black")
    root.timezones.grid(row=6, column=1, padx=10, pady=5)

    languagesLabel = Label(root, text="LANGUAGES : ", bg="slateblue4")
    languagesLabel.grid(row=7, column=0, padx=10, pady=5)
    root.languages = Label(root, width=36, bg="black")
    root.languages.grid(row=7, column=1, padx=10, pady=5)

    flagLabel = Label(root, text="FLAG : ", bg="slateblue4")
    flagLabel.grid(row=8, column=0, padx=10, pady=5)
    root.flag = Label(root,  bg="slateblue4")
    root.flag.grid(row=8, column=1, padx=10, pady=5)

    getCountriesList()

# Defining getCountriesList() to get all the Countries' information on app startup
def getCountriesList():
    # Calling the Rest Countries API to fetch all the details regarding all the counties
    countryApiResponse = requests.get("https://restcountries.com/v3.1/all")
    # Declaring global variable
    global countryInfoJson
    # Converting the API response into JSON
    countryInfoJson = countryApiResponse.json()
    # Looping through the JSON response and adding all the countries' names to a list
    countriesList = []
    for country in countryInfoJson:
        countriesList.append(country["name"]["common"])
    # Setting the sorted list to the Combobox Widget
    root.countryList.config(values=sorted(countriesList))

# Defining getCountryInfo() function to get the information of user-selected country
def getCountryInfo():
    # Retrieving and storing the user-selected country from the dropdown
    selectedCountry = root.countryList.get()
    # Looping through the previously retrieved JSON and fetching the info of selected country
    for info in countryInfoJson:
        if info["name"]["common"] == selectedCountry:
            # Retrieving the needed information and stoing in respective variables
            officialName = info["name"]["official"]
            capital = ",".join(info["capital"])
            continent = info["region"]
            population = info["population"]
            currencies = ", ".join(f"{key}" for key, value in info["currencies"].items())
            timezones = ", ".join(info["timezones"])
            languages = ", ".join(f"{value}" for key, value in info["languages"].items())

            # Fetching the Flag of the country from URL received in the JSON
            flagRawData = requests.get(info["flags"]["png"]).content
            # Opening the Flag image using the open() of Image class
            flagImage = Image.open(io.BytesIO(flagRawData))
            # Resizing the Flag using Image.resize()
            resizedFlag = flagImage.resize((int(flagImage.width/2), int(flagImage.height/2)), Image.LANCZOS)
            # Creating object of PhotoImage() class to display the Flag
            countryFlag = ImageTk.PhotoImage(resizedFlag)
            # Configuring the label to display the Flag
            root.flag.config(image=countryFlag)
            # Keeping a reference
            root.flag.photo = countryFlag

            # Showing the new results in the tkinter window
            root.officialName.config(text=officialName, anchor="w", justify=LEFT)
            root.capital.config(text=capital, anchor="w", justify=LEFT)
            root.continent.config(text=continent, anchor="w", justify=LEFT)
            root.population.config(text=population, anchor="w", justify=LEFT)
            root.currency.config(text=currencies, anchor="w", justify=LEFT)
            root.timezones.config(text=timezones, anchor="w", justify=LEFT)
            root.languages.config(text=languages, anchor="w", justify=LEFT)

# Defining clearEntries() to clear the values from the text entries of tkinter window
def clearEntries():
    root.countryList.get()
    root.officialName.config(text="")
    root.capital.config(text="")
    root.continent.config(text="")
    root.population.config(text="")
    root.currency.config(text="")
    root.languages.config(text="")
    root.timezones.config(text="")
    root.flag.config(image="")

# Creating object of tk class
root = tk.Tk()
# Setting the title, background color, windowsize & disabling the resizing property
root.title("PythonCountryInfo")
root.config(background="slateblue4")
root.geometry("515x410")
root.resizable(False, False)
# Calling the CreateWidgets() function
CreateWidgets()
# Defining infinite loop to run application
root.mainloop()
