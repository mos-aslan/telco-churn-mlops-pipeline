from pathlib import Path
import argparse
import json
from datetime import datetime

import pandas as pd

from src.inference import (
    predict_from_feature_dataframe,
    predict_from_raw_dataframe
)


PROJECT_ROOT = Path(__file__).resolve().parent


def get_paths():
    paths = {
        'project_root': PROJECT_ROOT,
        'data_dir': PROJECT_ROOT / 'data',
        'data_v1_dir': PROJECT_ROOT / 'data' / 'v1',
        'data_v2_dir': PROJECT_ROOT / 'data' / 'v2',
        'data_v3_dir': PROJECT_ROOT / 'data' / 'v3',
        'src_dir': PROJECT_ROOT / 'src',
        'models_dir': PROJECT_ROOT / 'models',
        'final_model_dir': PROJECT_ROOT / 'models' / 'final_model',
        'reports_dir': PROJECT_ROOT / 'reports',
        'pipeline_reports_dir': PROJECT_ROOT / 'reports' / 'final_pipeline_runs',
    }
    return paths


def ensure_pipeline_output_dirs():
    paths = get_paths()
    output_dir = paths['pipeline_reports_dir']
    output_dir.mkdir(parents=True, exist_ok=True)
    return output_dir


def check_project_readiness():
    paths = get_paths()

    required_paths = {
        'project_root': paths['project_root'],
        'data_v1_dir': paths['data_v1_dir'],
        'data_v2_dir': paths['data_v2_dir'],
        'data_v3_dir': paths['data_v3_dir'],
        'src_dir': paths['src_dir'],
        'models_dir': paths['models_dir'],
        'final_model_dir': paths['final_model_dir'],
        'src_inference_py': paths['src_dir'] / 'inference.py',
        'src_features_py': paths['src_dir'] / 'features.py',
        'final_model': paths['final_model_dir'] / 'final_model.joblib',
        'final_metadata': paths['final_model_dir'] / 'final_model_metadata.json',
        'feature_names': paths['final_model_dir'] / 'feature_names.json',
        'decision_threshold': paths['final_model_dir'] / 'decision_threshold.json',
        'sample_input_features': paths['final_model_dir'] / 'sample_input_features.csv',
    }

    rows = []
    for name, path in required_paths.items():
        rows.append({
            'Item': name,
            'Path': str(path),
            'Exists': path.exists()
        })

    readiness_df = pd.DataFrame(rows)

    output_dir = ensure_pipeline_output_dirs()
    readiness_path = output_dir / 'project_readiness_check.csv'
    readiness_df.to_csv(readiness_path, index=False)

    all_ready = bool(readiness_df['Exists'].all())

    summary = {
        'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'all_required_items_exist': all_ready,
        'readiness_table': str(readiness_path)
    }

    summary_path = output_dir / 'project_readiness_summary.json'
    with open(summary_path, 'w', encoding='utf-8') as file:
        json.dump(summary, file, indent=4)

    print('=' * 80)
    print('PROJECT READINESS CHECK')
    print('=' * 80)
    print(readiness_df.to_string(index=False))
    print('\nAll required items exist:', all_ready)
    print('Readiness table saved:', readiness_path)
    print('Readiness summary saved:', summary_path)

    if not all_ready:
        raise FileNotFoundError('Some required project files or folders are missing.')

    return readiness_df


def describe_final_model():
    paths = get_paths()
    metadata_path = paths['final_model_dir'] / 'final_model_metadata.json'
    threshold_path = paths['final_model_dir'] / 'decision_threshold.json'
    feature_names_path = paths['final_model_dir'] / 'feature_names.json'

    with open(metadata_path, 'r', encoding='utf-8') as file:
        metadata = json.load(file)

    with open(threshold_path, 'r', encoding='utf-8') as file:
        threshold_data = json.load(file)

    with open(feature_names_path, 'r', encoding='utf-8') as file:
        feature_names = json.load(file)

    description = {
        'model_name': metadata.get('model_name'),
        'model_status': metadata.get('model_status'),
        'dataset_version': metadata.get('dataset_version'),
        'decision_threshold': threshold_data.get('decision_threshold'),
        'feature_count': len(feature_names),
        'champion_test_metrics': metadata.get('champion_test_metrics'),
        'final_model_path': str(paths['final_model_dir'] / 'final_model.joblib')
    }

    output_dir = ensure_pipeline_output_dirs()
    description_path = output_dir / 'final_model_description.json'
    with open(description_path, 'w', encoding='utf-8') as file:
        json.dump(description, file, indent=4)

    print('=' * 80)
    print('FINAL MODEL DESCRIPTION')
    print('=' * 80)
    print(json.dumps(description, indent=4))
    print('\nDescription saved:', description_path)

    return description


def predict_sample():
    paths = get_paths()
    sample_path = paths['final_model_dir'] / 'sample_input_features.csv'

    if not sample_path.exists():
        raise FileNotFoundError(f'Sample input file not found: {sample_path}')

    sample_df = pd.read_csv(sample_path)

    predictions = predict_from_feature_dataframe(
        sample_df,
        project_root=PROJECT_ROOT
    )

    output = pd.concat(
        [sample_df.reset_index(drop=True), predictions.reset_index(drop=True)],
        axis=1
    )

    output_dir = ensure_pipeline_output_dirs()
    output_path = output_dir / 'sample_prediction_from_pipeline.csv'
    output.to_csv(output_path, index=False)

    print('=' * 80)
    print('SAMPLE PREDICTION')
    print('=' * 80)
    print(predictions.to_string(index=False))
    print('\nSample prediction saved:', output_path)

    return output


def predict_csv(input_path, input_type, output_path=None):
    input_path = Path(input_path)

    if not input_path.exists():
        raise FileNotFoundError(f'Input CSV file not found: {input_path}')

    df_input = pd.read_csv(input_path)

    if input_type == 'features':
        predictions = predict_from_feature_dataframe(
            df_input,
            project_root=PROJECT_ROOT
        )
    elif input_type == 'raw':
        predictions = predict_from_raw_dataframe(
            df_input,
            project_root=PROJECT_ROOT
        )
    else:
        raise ValueError("input_type must be either 'features' or 'raw'.")

    output = pd.concat(
        [df_input.reset_index(drop=True), predictions.reset_index(drop=True)],
        axis=1
    )

    output_dir = ensure_pipeline_output_dirs()

    if output_path is None:
        output_path = output_dir / 'batch_prediction_from_pipeline.csv'
    else:
        output_path = Path(output_path)

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output.to_csv(output_path, index=False)

    print('=' * 80)
    print('BATCH PREDICTION')
    print('=' * 80)
    print('Input:', input_path)
    print('Input type:', input_type)
    print('Rows predicted:', len(output))
    print('Output saved:', output_path)

    return output


def main():
    parser = argparse.ArgumentParser(
        description='Final reproducible pipeline for Telco Customer Churn prediction.'
    )

    parser.add_argument(
        '--mode',
        required=True,
        choices=['check', 'describe', 'predict-sample', 'predict-csv'],
        help='Pipeline mode to run.'
    )

    parser.add_argument(
        '--input',
        required=False,
        help='Input CSV path for predict-csv mode.'
    )

    parser.add_argument(
        '--input-type',
        required=False,
        choices=['features', 'raw'],
        default='features',
        help='Input data type for predict-csv mode.'
    )

    parser.add_argument(
        '--output',
        required=False,
        help='Optional output CSV path for predict-csv mode.'
    )

    args = parser.parse_args()

    if args.mode == 'check':
        check_project_readiness()
    elif args.mode == 'describe':
        describe_final_model()
    elif args.mode == 'predict-sample':
        predict_sample()
    elif args.mode == 'predict-csv':
        if args.input is None:
            raise ValueError('--input is required when mode is predict-csv.')
        predict_csv(
            input_path=args.input,
            input_type=args.input_type,
            output_path=args.output
        )


if __name__ == '__main__':
    main()
