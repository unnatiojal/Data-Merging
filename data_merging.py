import pandas as pd
import csv

final_data = pd.read_csv('dwarf_stars.csv')
brightest_star_file = pd.read_csv('bright_stars.csv')


final_data['Mass'] = float()
final_data['Radius'] = float()

final_data['Mass'] * 0.000954588
final_data['Radius'] * 0.102763

merge_csv = pd.merge(final_data, brightest_star_file, on="id" )

merge_csv.to_csv('final_scraper.csv')