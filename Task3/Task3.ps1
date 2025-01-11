# Define the output file path
$outputFile = "C:\Scripts\output.txt"

# Task 1: Find all scripting commands that are print related and output the list to a local file.
Get-Command -Name *print* | Out-File -FilePath $outputFile

# Task 2: Append the long version of the current date and time to the same file.
Get-Date -Format "F" | Out-File -FilePath $outputFile -Append

# Task 3: Close all Notepad files.
Get-Process notepad | ForEach-Object { $_.Kill() }

# Task 4: Append the last 20 errors from the event log to the same file.
Get-EventLog -LogName Application -EntryType Error -Newest 20 | Out-String | Out-File -FilePath $outputFile -Append

# Task 5: Append a list of all available WMI classes to the same file.
Get-WmiObject -List | Select-Object -ExpandProperty __CLASS | Out-File -FilePath $outputFile -Append

# Task 6: List the start command or full path of every executable.
Get-WmiObject -Query "SELECT ProcessID, CommandLine FROM Win32_Process WHERE ExecutablePath IS NOT NULL" |
    Select-Object ProcessID, CommandLine | Out-String | Out-File -FilePath $outputFile -Append

# Task 7: Identify what account the spooler is running as.
Get-WmiObject -Query "SELECT StartName FROM Win32_Service WHERE Name='Spooler'" |
    Select-Object -ExpandProperty StartName | Out-File -FilePath $outputFile -Append
