$envPath = [System.Environment]::GetEnvironmentVariable("Path", [System.EnvironmentVariableTarget]::User).Split(";")
$scriptsPath = "C:\miniconda3\Scripts"
$minicondaPath = "C:\miniconda3"
$pathUpdated = $false

if ($scriptsPath -notin $envPath) {
    $envPath += $scriptsPath
    $pathUpdated = $true
}

if ($minicondaPath -notin $envPath) {
    $envPath += $minicondaPath
    $pathUpdated = $true
}

if ($pathUpdated) {
    [System.Environment]::SetEnvironmentVariable("Path", ($envPath -join ";"), [System.EnvironmentVariableTarget]::User)
    Write-Output "Environment variable 'Path' updated successfully."
} else {
    Write-Output "No changes made to the environment variable 'Path'."
}
