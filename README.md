# -DATA-PIPELINE-DEVELOPMENT

*COMPANY*: CODTECH IT SOLUTIONS

*NAME*: CHITTAMSETTY NAGA VIJAY SAI

*INTERN ID*: CT08DZ1376

*DOMAIN*: DATA SCIENCE

*DURATION*: 8 WEEKS

*MENTOR*:  NEELA SANTHOSH KUMAR 


*DESCRIPTION*:

Task1-DataPipeline/
├─ data/
│ ├─ your_dataset.csv # Raw input dataset
│ └─ processed_dataset.csv # Output after preprocessing
├─ data_pipeline.py # Main Python script
├─ requirements.txt # Python dependencies
└─ README.md # Project documentation


##🛠️ Requirements
- **Python 3.8+**
- pandas
- scikit-learn
- numpy  
(Optional) `openpyxl` if you use Excel (`.xlsx`) files.

Install everything:
```bash
pip install -r requirements.txt


##How to Run

1.Clone this repository:
git clone https://github.com/<your-username>/Task1-DataPipeline.git
cd Task1-DataPipeline

2.Place your dataset:
Put your CSV/Excel file in the data/ folder (an example file is provided).

3.Execute the pipeline:
python data_pipeline.py

The cleaned dataset will be saved to:
data/processed_dataset.csv


##🔄 Pipeline Steps

1.Extract:
Reads input CSV/Excel with pandas.

2.Transform:
Handle missing values.
Numeric columns: mean imputation.
Categorical columns: most-frequent imputation.
Encode categorical features with LabelEncoder.
Scale numeric features with StandardScaler.

3.Load:
Saves final DataFrame to processed_dataset.csv.


##🧩 Example Dataset
data/your_dataset.csv (sample):

Name    	Age	Gender	 Salary	  Department
Alice	    25	Female	 50000	    HR
Bob	      30	Male	   60000	   IT
Charlie		    Male	   55000	   IT
Diana	    28	Female		         HR
Edward	  35	Male	   72000	   Finance


#3🖥️ Core Code Snippet
import pandas as pd
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.impute import SimpleImputer

df = pd.read_csv("data/your_dataset.csv")

# Impute numeric columns
num_imputer = SimpleImputer(strategy="mean")
df[df.select_dtypes(include=["number"]).columns] = \
    num_imputer.fit_transform(df.select_dtypes(include=["number"]))

# Encode categorical columns
for col in df.select_dtypes(include="object").columns:
    df[col] = LabelEncoder().fit_transform(df[col])

# Scale features
scaler = StandardScaler()
df[df.columns] = scaler.fit_transform(df)

df.to_csv("data/processed_dataset.csv", index=False)
print("✅ Pipeline complete.")


##📜 Deliverables

data_pipeline.py – automated ETL script

data/processed_dataset.csv – cleaned & transformed output

README.md – this documentation


##🙌 Credits

Internship: CODTECH Data Science Internship

Tools: Python, pandas, scikit-learn


---

### 💡 How to Use
1. Save the text above as `README.md` in your repository root.
2. Commit & push to GitHub:
   ```bash
   git add README.md
   git commit -m "Add complete README for Task 1"
   git push


*OUTPUT*:

| Name |     Age | Gender |  Salary | Department |
| ---: | ------: | -----: | ------: | ---------: |
|    0 | -1.1832 |    1.0 | -0.8780 |        0.0 |
|    1 |  0.1690 |   -1.0 | -0.0606 |        1.0 |
|    2 |  0.1690 |   -1.0 | -0.4693 |        1.0 |
|    3 | -0.5071 |    1.0 |  0.0000 |        0.0 |
|    4 |  1.3523 |   -1.0 |  1.4079 |        2.0 |



