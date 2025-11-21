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
In main.py file, Set those two values:
```python
grist_doc_path="path/to/grist/doc"
dbml_output_path="path/to/output/file"
```

You can then run the script.
