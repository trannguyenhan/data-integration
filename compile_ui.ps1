# Powershell script 
# Compile .ui file into .py file

$filenames = @("new_project", "project_management", "init_project", "workbench")

foreach ($element in $filenames) {
    pyuic5 ui/designs/$element.ui -o ui/$element.py
    Write-Output "$element.ui -> $element.py"
}