# CSV-Jsonl Converter
With this small app, you can easily convert your training data from .csv to .jsonl format according to OpenAI specifications.

![image](https://github.com/user-attachments/assets/3fdf9810-a11d-40b5-9210-523dac419d8c)

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

5. Update pip
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
To convert a CSV file to JSONL, simply drag and drop the .csv file into the designated area, enter the system prompt in the text box, and click 'Export JSONL'.

CSV requirements
---
The .csv file containing training data should include two columns: 'Prompt' and 'Answer'.

![image](https://github.com/user-attachments/assets/619377fb-29e9-4546-8193-063d1840a38b)

Important
---
Please do not use training data from the TestData directory in a real fine-tuning project!
