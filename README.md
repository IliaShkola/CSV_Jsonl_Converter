# CSV FineTune Converter
This lightweight app allows you to effortlessly convert your training data from .csv to .jsonl for OpenAI model fine-tuning or .json for Llama (Alpaca structure) models.

![Screenshot 2025-02-21 155933](https://github.com/user-attachments/assets/90e581f5-ad3d-4cd5-b215-3713f1aff002)


Installation
---
1. Clone repository
```
git clone https://github.com/IliaShkola/CSV_Jsonl_Converter.git
```

2. Move to the project folder
```
cd CSV_Jsonl_Converter
```
3. Create new python environment
```
python -m venv myenv
``` 

4. Activate the environment
```
myenv\Scripts\activate
```

5. Upgrade pip
```
python.exe -m pip install --upgrade pip
```

6. Install the libraries
```
pip install -r requirements.txt
```

7. Create an executable with PyInstaller
```
pyinstaller app.spec --noconfirm --clean
```
The executable file will be stored in the 'dist' project folder.

Usage
---
To convert a CSV file to JSONL or JSON, simply drag and drop your .csv file into the designated area. Then, enter the system prompt in the text box and select the output format based on the model you want to fine-tune.
Alpaca models don't require a system prompt.

CSV requirements
---
The .csv file containing training data should include two columns: 'Prompt' and 'Answer'.

![image](https://github.com/user-attachments/assets/619377fb-29e9-4546-8193-063d1840a38b)

Important
---
Please do not use training data from the TestData directory in a real fine-tuning project!
