import pandas as pd

def parse_csv(file_path):
    try:
        df = pd.read_csv(file_path)

        if df.empty:
            return None

        row = df.iloc[0]

        return {
            "full_name": row["name"],
            "emails": [row["email"]],
            "phones": [str(row["phone"])],
            "current_company": row["current_company"],
            "title": row["title"]
        }

    except Exception as e:
        print("CSV Parser Error:", e)
        return None