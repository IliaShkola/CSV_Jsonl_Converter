import sys
import csv
import json
import os
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QLabel, QVBoxLayout, QWidget, QPlainTextEdit, QPushButton
from PyQt5.QtCore import Qt


class DragDropWidget(QLabel):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setAcceptDrops(True)
        self.setText("Drag & Drop CSV File Here")
        self.setAlignment(Qt.AlignCenter)
        self.setStyleSheet("border: 2px dashed #aaa; padding: 20px; font-size: 14px;")

        # Store a reference to parent to avoid NoneType crashes
        self.parent_widget = parent

    def dragEnterEvent(self, event):
        """Handles drag enter event."""
        if event.mimeData().hasUrls():
            event.acceptProposedAction()

    def dropEvent(self, event):
        """Handles file drop event."""
        for url in event.mimeData().urls():
            file_path = url.toLocalFile()
            if file_path.endswith(".csv"):
                if self.parent_widget:
                    self.parent_widget.load_csv_file(file_path)
                return
        QMessageBox.warning(self, "Invalid File", "Please drop a valid CSV file.")


class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.csvFile = None
        self.csv_data = None
        self.initUI()

    def initUI(self):
        """Initialize UI with drag and drop functionality."""
        self.setWindowTitle("CSV FineTune Converter")

        # Central widget
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)

        # Drag and Drop Widget
        self.drag_drop_widget = DragDropWidget(self)
        layout.addWidget(self.drag_drop_widget)

        # Status Label
        self.lab_status_show = QLabel("Upload please CSV file", self)
        layout.addWidget(self.lab_status_show)

        # Plain Text Edit for System Message
        self.plainTextEdit = QPlainTextEdit(self)
        self.plainTextEdit.setPlaceholderText("Enter system prompt here...")
        layout.addWidget(self.plainTextEdit)

        # Export JSONL Button
        self.but_jsonl_export = QPushButton("Export JSONL (OpenAI)", self)
        self.but_jsonl_export.setFixedHeight(50)
        self.but_jsonl_export.clicked.connect(self.export_jsonl)
        layout.addWidget(self.but_jsonl_export)

        # Export JSON Button
        self.but_json_export = QPushButton("Export JSON (Alpaca)", self)
        self.but_json_export.setFixedHeight(50)
        self.but_json_export.clicked.connect(self.export_json)
        layout.addWidget(self.but_json_export)

        self.show()

    def load_csv_file(self, file_path):
        """Load CSV file after successful drag and drop."""
        try:
            with open(file_path, newline='', encoding='utf-8') as csvfile:
                reader = csv.reader(csvfile)
                data = [row for row in reader]
                if not data:
                    raise ValueError("CSV file is empty.")

            self.csvFile = file_path
            self.csv_data = data
            self.lab_status_show.setText(f"{os.path.basename(self.csvFile)} is uploaded")
            self.drag_drop_widget.setText(f"Loaded: {os.path.basename(self.csvFile)}")
            print(f"Successfully loaded: {file_path}")

        except Exception as e:
            QMessageBox.critical(self, "Error", f"Failed to load CSV file: {e}")
            self.csvFile = None
            self.csv_data = None
            self.lab_status_show.setText("Upload please CSV file")
            self.drag_drop_widget.setText("Drag & Drop CSV File Here")

    def export_jsonl(self):
        """Export CSV data to JSONL format. OpenAI structure."""
        if not self.csvFile:
            QMessageBox.critical(self, "Error", "No uploaded CSV file. Please upload a CSV file first.")
            return

        system_message_content = self.plainTextEdit.toPlainText().strip()
        if not system_message_content:
            QMessageBox.critical(self, "Error", "System message is empty. Please enter a system message.")
            return

        system_message = {
            "role": "system",
            "content": system_message_content
        }

        output_jsonl_file = os.path.splitext(self.csvFile)[0] + "_openai.jsonl"

        try:
            with open(self.csvFile, mode='r', encoding='utf-8') as csv_file, open(output_jsonl_file, mode='w', encoding='utf-8') as jsonl_file:
                csv_reader = csv.DictReader(csv_file)
                for row in csv_reader:
                    user_prompt = row.get("Prompt", "").strip()
                    assistant_answer = row.get("Answer", "").strip()

                    # Skip empty rows
                    if not user_prompt or not assistant_answer:
                        continue

                    jsonl_entry = {
                        "messages": [
                            system_message,
                            {"role": "user", "content": user_prompt},
                            {"role": "assistant", "content": assistant_answer}
                        ]
                    }
                    jsonl_file.write(json.dumps(jsonl_entry) + '\n')

            QMessageBox.information(self, "Success", f"Exported JSONL file: {output_jsonl_file}")
            print(f"Converted {self.csvFile} to {output_jsonl_file} successfully!")

        except Exception as e:
            QMessageBox.critical(self, "Error", f"Failed to export JSONL file: {e}")

    def export_json(self):
        """Export CSV data to JSON format (Alpaca structure)."""

        if not self.csvFile:
            QMessageBox.critical(self, "Error", "No uploaded CSV file. Please upload a CSV file first.")
            return

        output_json_file = os.path.splitext(self.csvFile)[0] + "_alpaca.json"

        try:
            with open(self.csvFile, mode='r', encoding='utf-8') as csv_file, open(output_json_file, mode='w',
                                                                                  encoding='utf-8') as json_file:
                csv_reader = csv.DictReader(csv_file)
                json_data = []

                for row in csv_reader:
                    prompt = row.get("Prompt", "").strip()
                    answer = row.get("Answer", "").strip()
                    if not prompt or not answer:
                        continue

                    # Convert to Alpaca format
                    json_entry = {
                        "instruction": prompt,
                        # Alpaca format requires an "input" field (empty here)
                        "input": "",
                        "output": answer
                    }
                    json_data.append(json_entry)

                json.dump(json_data, json_file, indent=4, ensure_ascii=False)

            QMessageBox.information(self, "Success", f"Exported JSON file: {output_json_file}")
            print(f"Converted {self.csvFile} to {output_json_file} successfully!")

        except Exception as e:
            QMessageBox.critical(self, "Error", f"Failed to export JSON file: {e}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyApp()
    sys.exit(app.exec_())
