import pandas as pd
from data_quality import calculate_dqi  # ✅ Make sure this matches your actual script name

def test_calculate_dqi():
    data = {
        'Name': ['Alice', 'Bob', None],
        'Age': [25, None, 22],
        'Score': [85, 90, None]
    }
    df = pd.DataFrame(data)
    missing_values, dqi = calculate_dqi(df)
    assert missing_values == 3
    assert round(dqi, 2) == 66.67
