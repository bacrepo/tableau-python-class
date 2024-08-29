$envPath = [System.Environment]::GetEnvironmentVariable("Path", [System.EnvironmentVariableTarget]::User).Split(";")

$pathsToRemove = @(
    "C:\miniconda3",
    "C:\miniconda3\Library\mingw-w64\bin",
    "C:\miniconda3\Library\usr\bin",
    "C:\miniconda3\Library\bin",
    "C:\miniconda3\Scripts"
)

$pathUpdated = $false

$envPath = $envPath | Where-Object { $pathsToRemove -notcontains $_ }
$pathUpdated = $true

if ($pathUpdated) {
    [System.Environment]::SetEnvironmentVariable("Path", ($envPath -join ";"), [System.EnvironmentVariableTarget]::User)
    Write-Output "Specified paths removed from the environment variable 'Path' successfully."
} else {
    Write-Output "No changes made to the environment variable 'Path'."
}
