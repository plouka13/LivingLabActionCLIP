import json
import pandas as pd

creator = 'JH'

# Load the JSON data
with open(f'./{creator}_elan_export.json') as f:
    data = json.load(f)

# Extract the relevant information
annotations = []
for item in data['contains']:
    for annotation in item['first']['items']:
        if annotation['type'] == 'Annotation':
            annotation_value = annotation['body']['value']
            if annotation_value != '':  # Ignore empty annotations
                time_value = annotation['target']['selector']['value']
                start_time, end_time = time_value.split('=')[1].split(',')
                annotations.append({
                    'start_time': float(start_time),
                    'end_time': float(end_time),
                    'annotation': annotation_value,
                    'data_type': item['label']
                })

# Create a DataFrame
df = pd.DataFrame(annotations)

# Display the DataFrame
print(df)

# Save the DataFrame to a JSON file
df.to_json(f'./{creator}_annotations.json', orient='records', lines=True)
