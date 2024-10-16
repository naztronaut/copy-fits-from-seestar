$sourceDirectory = "z:\path\to\seestar\folder"
$destinationDirectory = "C:\path\to\local\folder"

# Create the destination directory if it doesn't exist
if (-not (Test-Path -Path $destinationDirectory)) {
    New-Item -ItemType Directory -Path $destinationDirectory
}

while ($true) {
    # Use xcopy to copy only .fit files
    $xcopyCommand = "xcopy `"$sourceDirectory\*.fit`" `"$destinationDirectory`" /D /Y"
    Invoke-Expression $xcopyCommand

    # Wait for 1 minute (60 seconds)
    Start-Sleep -Seconds 60
}
