import pandas as pd
import glob

files = glob.glob('data/*.csv')
data_frames = []

for file in files:
    df = pd.read_csv(file)
    data_frames.append(df)

combined_df = pd.concat(data_frames)

combined_df = combined_df[combined_df['product'] == 'pink morsel']

combined_df['price'] = combined_df['price'].replace('[\$,]', '', regex=True).astype(float)
combined_df['sales'] = combined_df['price'] * combined_df['quantity']

final_df = combined_df[['sales', 'date', 'region']]

final_df.to_csv('formatted_data.csv', index=False)

print("Data processing complete! 'formatted_data.csv' has been created.")