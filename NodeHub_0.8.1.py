import csv
import matplotlib.pyplot as plt
import time
from IPython.display import HTML

# Define a dictionary mapping neighborhood names to file paths
neighborhood_files = {
    'San Telmo': {
        'owned': r'C:\Users\bambo\Documents\NodeHub\SanTelmoOwnedProperties\owned.csv',
        'structure': r'C:\Users\bambo\Documents\NodeHub\SanTelmoOwnedProperties\structure.csv',
    },
    'El Sereno': {
        'owned': r'C:\Users\bambo\Documents\NodeHub\LosAngeles\owned_es.csv',
        'structure': r'C:\Users\bambo\Documents\NodeHub\LosAngeles\structure_es.csv',
    },
    'Sherwood Forest': {
        'owned': r'C:\Users\bambo\Documents\NodeHub\SherwoodForest\owned_sf.csv',
        'structure': r'C:\Users\bambo\Documents\NodeHub\SherwoodForest\structure_sf.csv',
    },
    'Sunrise': {
        'owned': r'C:\Users\bambo\Documents\NodeHub\Sunrise\owned_sr.csv',
        'structure': r'C:\Users\bambo\Documents\NodeHub\Sunrise\structure_sr.csv',
    }
    # Add more neighborhoods as needed
}

# Define a function to update the pie chart for a given neighborhood
def update_pie_chart(neighborhood):
    try:
        owned_path = neighborhood_files[neighborhood]['owned']
        structure_path = neighborhood_files[neighborhood]['structure']
    except KeyError:
        print(f"Error: Files for '{neighborhood}' not found.")
        return

    with open(owned_path, 'r') as f:
        owned_reader = csv.DictReader(f)
        owned_properties = sum(1 for row in owned_reader if row['Neighborhood'] in ['SAN TELMO', 'EL SERENO', 'SHERWOOD FOREST', 'SUNRISE'])


    with open(structure_path, 'r') as f:
        structure_reader = csv.DictReader(f)
        structure_properties = sum(1 for row in structure_reader if row['Structure'] == 'completed')

    labels = ['Owned', 'Owned with Structures']
    sizes = [owned_properties, structure_properties]
    colors = ['gray', 'red']

    plt.clf()
    plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90)
    plt.axis('equal')
    plt.title(f'Total Owned Properties vs. Properties with Structures in {neighborhood}')
    plt.show()


# Display the initial pie chart
update_pie_chart('San Telmo')

# Define a loop to update the pie chart every 2 seconds
while True:
    time.sleep(2)
    neighborhood = input('Enter neighborhood to update pie chart (or "quit" to exit): ')
    if neighborhood == 'quit':
        break
    update_pie_chart(neighborhood)