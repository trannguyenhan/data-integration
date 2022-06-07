# Data integration - SSIS 
A tool allow to convert from different data source (flatfile, xml, excel, json, SQLServer, MySQL) to save into a single destination data source. This tool is inspired from SSIS (SQLServer Integration Services)

### Project structures
Project is designed as 3 tier architecture (Presentation Layer, Bussiness Layer, Data Layer)

- `dal` folder: Data access layer
- `ui` folder: Presentation layer
- `widget` folder: Bussiness layer

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


### Công việc tuần tới
- Anh Hoàng: sqlite3 -> json, tìm cách query file json, support ae
- Xuân Huy + E Hoàng: Tiếp tục phát triển Workbench, Config, tự liên lạc với nhau làm việc
- Quang Huy: Tiếp tục phát triển các Engine
- Deadline: 1 tuần (tối t4 tuần sau)

