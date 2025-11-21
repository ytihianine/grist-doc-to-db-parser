## Installation

Clone this repository using Git:
```bash
git clone https://github.com/ytihianine/grist-doc-to-db-parser.git
cd grist-doc-to-db-parser/
```

Install the packages:
```bash
pip install -r requirements.txt
```

## Usage 

First, you need to download the structure of your Grist document (no data are needed, only the structure).  
In `main.py` file, Set those values:
```python
grist_doc_path = ""
dbml_output_path = ""
export = False
csv_output_path = ""
```

You can then run the `main.py` script.
