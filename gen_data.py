import pandas as pd
import numpy as np
from pathlib import Path
import os

# Create data directory if it doesn't exist
data_dir = Path(__file__).parent.parent / "data"
data_dir.mkdir(exist_ok=True)

def generate_wells_completion_data():
    """
    Generate wells completion data from 1960-2020
    - Simulates historical well completion patterns
    - Early years (1960-1970): Low activity (0-50 wells)
    - Peak years (1970-1990): High activity (50-600 wells)
    - Recent years (1990-2020): Moderate activity (20-200 wells)
    """
    np.random.seed(42)  # For reproducibility
    
    years = list(range(1960, 2021))
    wells_count = []
    
    for year in years:
        if year < 1970:
            # Early period: Low activity
            count = np.random.randint(0, 50)
        elif 1970 <= year < 1990:
            # Peak period: High activity
            count = np.random.randint(50, 600)
        else:
            # Recent period: Moderate activity
            count = np.random.randint(20, 200)
        wells_count.append(count)
    
    df_wells = pd.DataFrame({
        'Year': years,
        'Completed_Wells': wells_count
    })
    
    # Save to CSV
    df_wells.to_csv(data_dir / 'wells_completion.csv', index=False)
    print("Generated wells completion data")
    return df_wells

def generate_production_data():
    """
    Generate production data for 2008-2015
    - Gas: Main production with peak in 2011
    - Oil: Consistent low production
    - Water: Minimal production
    Values in MCF (Million Cubic Feet)
    """
    years = list(range(2008, 2016))
    
    # Create realistic production curves
    gas_production = [0, 0.2, 0.8, 2.0, 1.8, 1.2, 0.5, 0]  # Peak in 2011
    oil_production = [0, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0]  # Consistent low production
    water_production = [0, 0, 0, 0, 0, 0, 0, 0]  # Minimal water production
    
    df_production = pd.DataFrame({
        'Year': years,
        'Gas_Produced': gas_production,
        'Oil_Produced': oil_production,
        'Water_Produced': water_production
    })
    
    # Save to CSV
    df_production.to_csv(data_dir / 'production_data.csv', index=False)
    print("Generated production data")
    return df_production

def generate_production_summary():
    """
    Generate production summary data with categories and percentages
    Includes different types of wells and their contribution to total production
    """
    categories = [
        'Gas', 'Water', 'Oil',
        'Gas Development', 'Oil Development',
        'Gas Extension', 'Gas Wildcat',
        'Oil Injection', 'Oil Wildcat'
    ]
    
    # Realistic percentages that sum to 100%
    percentages = [
        96.7, 0.807, 2.3,  # Main categories
        54.1, 39.1,        # Development
        3.08, 2.96,        # Gas categories
        0.41, 0.685        # Oil categories
    ]
    
    df_summary = pd.DataFrame({
        'Category': categories,
        'Percentage': percentages
    })
    
    # Save to CSV
    df_summary.to_csv(data_dir / 'production_summary.csv', index=False)
    print("Generated production summary data")
    return df_summary

def generate_geographic_data():
    """
    Generate geographic data for well locations in New York State
    Includes well sites with their coordinates and properties
    """
    well_sites = {
        'Site_Name': ['Well Site A', 'Well Site B', 'Well Site C', 'Well Site D'],
        'Latitude': [42.5, 42.8, 42.3, 42.6],
        'Longitude': [-76.5, -76.2, -76.8, -76.4],
        'Status': ['Active', 'Active', 'Active', 'Active'],
        'Type': ['Gas Production', 'Oil Production', 'Gas Wildcat', 'Water Injection']
    }
    
    df_geographic = pd.DataFrame(well_sites)
    
    # Save to CSV
    df_geographic.to_csv(data_dir / 'geographic_data.csv', index=False)
    print("Generated geographic data")
    return df_geographic

def main():
    """Generate all datasets for the visualization dashboard"""
    print("Generating data files in:", data_dir.absolute())
    
    # Generate all datasets
    wells_df = generate_wells_completion_data()
    production_df = generate_production_data()
    summary_df = generate_production_summary()
    geographic_df = generate_geographic_data()
    
    print("\nData generation complete. Files saved in:", data_dir.absolute())
    print("\nDataset summaries:")
    print("\nWells Completion Data:")
    print(wells_df.describe())
    print("\nProduction Data:")
    print(production_df.describe())
    print("\nProduction Summary:")
    print(summary_df.describe())
    print("\nGeographic Data:")
    print(geographic_df.describe())

if __name__ == "__main__":
    main() 