from pathlib import Path
import pandas as pd


def find_excel_file(data_dir):
    data_dir = Path(data_dir)
    excel_files = list(data_dir.glob('*.xlsx')) + list(data_dir.glob('*.xls'))
    if not excel_files:
        raise FileNotFoundError(f'No Excel file found in: {data_dir}')
    return excel_files[0]


def load_raw_data(project_root):
    project_root = Path(project_root)
    data_dir = project_root / 'data' / 'v1'
    file_path = find_excel_file(data_dir)
    try:
        df = pd.read_excel(file_path, sheet_name='Telco_Churn')
    except ValueError:
        df = pd.read_excel(file_path)
    return df


def inspect_data(df):
    print('=' * 60)
    print('Dataset shape:')
    print(df.shape)
    print('\nColumns:')
    print(df.columns.tolist())
    print('\nData types:')
    print(df.dtypes)
    print('\nMissing values:')
    print(df.isnull().sum())
    if 'Churn Value' in df.columns:
        print('\nTarget distribution:')
        print(df['Churn Value'].value_counts())