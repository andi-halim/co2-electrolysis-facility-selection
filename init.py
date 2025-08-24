from pathlib import Path

def main():
    project_root = Path(__file__).parent
    data_dir = project_root / 'data'
    data_dir.mkdir(exist_ok=True)
    print(f"Project root directory: {project_root}")
    print(f"Data directory: {data_dir}")

    # Run pipeline

if __name__ == "__main__":
    main()