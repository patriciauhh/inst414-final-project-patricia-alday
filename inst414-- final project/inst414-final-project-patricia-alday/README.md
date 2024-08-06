# inst414-final-project-patricia-alday
# Food Insecurity in Urban Areas 
## Business Problem: 
A non-profit organization is looking to identify food deserts in urban areas of the United States to allocate resources effectively and plan new grocery store locations. Food deserts are areas where residents lack access to nutrious and healthy food source. The organization aims to use data to pinpoint these areas and understand the socio-economic factors contributing to them. 

## Data: 
- USDA Economic Research Service's Food Environment Atlas
- United States Census Bureau’s American Community Survey (ACS)

## Setup Instructions (macOS)
- Fork and clone repository 
- Create a virtual environment using -m venv venv 
- Activate virtual environment source venv/bin/activate 
- .\venv\Scripts\activate 
- to install dependencies pip install -r requirements.txt

## Run the project 
- python main.py in terminal 

## Code Package Structure
analysis/ evaluate.py, model.py 
data/ Data files 
datasets/ ACS and Atlas datasets 
etl/ extract.py, transform.py, load.py
vis/ vis.py
inst414final venv
main.py 
README.md
requirements.txt



