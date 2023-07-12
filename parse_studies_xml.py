import pandas as pd
import xmltodict
from datetime import datetime

# Read the XML file
with open('studies.xml', 'r') as xml_file:
    xml_data = xml_file.read()

# Convert XML to a dictionary
data_dict = xmltodict.parse(xml_data)

# Display the dictionary
#print(data_dict['bibdataset']['item'])
# Extract the desired fields from the dictionary
studies = data_dict['bibdataset']['item']

# Define lists to store the extracted data
doi_list = []
pub_date_list = []
title_list = []
abstract_list = []

# Iterate through the studies and extract the fields
for study in studies:
    doi = study['bibrecord']['item-info']['itemidlist']['ce:doi']
    publication_date_year = study['bibrecord']['head']['source']['publicationdate']['year']
    publication_date_moth = study['bibrecord']['head']['source']['publicationdate']['month']
    publication_date_day = study['bibrecord']['head']['source']['publicationdate']['day']
    publication_date_str = f'{publication_date_year}-{publication_date_moth}-{publication_date_day}'
    publication_date = datetime.strptime(publication_date_str, '%Y-%m-%d')
    title = study['bibrecord']['head']['citation-title']['titletext']['#text']
    abstract = study['bibrecord']['head']['abstracts']['abstract']['ce:para']
    
    # Append the extracted fields to the respective lists
    doi_list.append(doi)
    pub_date_list.append(publication_date)
    title_list.append(title)
    abstract_list.append(abstract)

    """print(f"DOI: {doi}")
    print(f"Publication date: {publication_date}")
    print(f"Title: {title}")
    print(f"Abstract: {abstract}")"""

# Create a DataFrame from the extracted data
df = pd.DataFrame({
    'doi': doi_list,
    'publication_date': pub_date_list,
    'title': title_list,
    'abstract': abstract_list
})

# Display the DataFrame
print(df)
