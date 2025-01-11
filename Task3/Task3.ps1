#Create a Notepad that shows all results
New-Item -ItemType Directory -Path "C:\Scripts"

# Define the output file path
$outputFile = "C:\Scripts\output.txt"

# Find all scripting commands that are print related and output the list to a local file.
Get-Command -Name *print* | Out-File -FilePath $outputFile

# Append the long version of the current date and time to the same file.
Get-Date -Format "F" | Out-File -FilePath $outputFile -Append

# Close all Notepad files.
Get-Process notepad | ForEach-Object { $_.Kill() }

# Append the last 20 errors from the event log to the same file.
Get-EventLog -LogName Application -EntryType Error -Newest 20 | Out-String | Out-File -FilePath $outputFile -Append

# Append a list of all available WMI classes to the same file.
Get-WmiObject -List | Select-Object -ExpandProperty __CLASS | Out-File -FilePath $outputFile -Append
