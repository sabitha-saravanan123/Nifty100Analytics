import pandas as pd
def load_excel(path):
    return pd.read_excel(path)
if __name__ == "__main__":
    print("Loader ready")