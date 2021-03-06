# Data integration - SSIS 
A tool allow to convert from different data source (flatfile, xml, excel, json, SQLServer, MySQL) to save into a single destination data source. This tool is inspired from SSIS (SQLServer Integration Services)

### Project structures
- `database`: Database used for this project.
- `engine`: Engine for opening, reading, converting data sources
- `ui`: ui file of Qt designer + generated python file
- `widgets`: Bussines for each screen

### Tools
- run powershell script `compile_ui.ps1` to compile `.ui` file automatically.


### Update requirements.txt

```
pip freeze > requirements.txt
```

### Data types
- integer
- string
- date
- float

### Source/Destination type
- Flatfile
- XML
- CSV
- JSON
- MySQL
- SQL Server

### Issue

if fail when install `pyodbc` in ubuntu, install package with command: 

```bash
sudo apt-get install unixodbc-dev
```

after install, install `pyodbc` with `pip`: 

```bash
pip isntall pyodbc
```
