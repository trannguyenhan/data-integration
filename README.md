# Data integration - SSIS 
A tool allow to convert from different data source (flatfile, xml, excel, json, SQLServer, MySQL) to save into a single destination data source. This tool is inspired from SSIS (SQLServer Integration Services)

### Project structures
Project is designed as 3 tier architecture (Presentation Layer, Bussiness Layer, Data Layer)

- `dal` folder: Data access layer
- `ui` folder: Presentation layer


### Tools
- run powershell script `compile_ui.ps1` to compile `.ui` file automatically.
