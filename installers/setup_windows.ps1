
# Hybrid_Sub Windows Environment Setup Script
Write-Host "Hybrid_Sub Windows Setup Script" -ForegroundColor Cyan

# Check for Go installation
$goPath = Get-Command go -ErrorAction SilentlyContinue
if (-not $goPath) {
    Write-Host "Go is not installed. Downloading and installing Go..." -ForegroundColor Yellow
    Invoke-WebRequest -Uri "https://go.dev/dl/go1.21.5.windows-amd64.msi" -OutFile "go_installer.msi"
    Start-Process "msiexec.exe" -Wait -ArgumentList '/i go_installer.msi /qn'
    Remove-Item "go_installer.msi"
    $env:Path += ";C:\Program Files\Go\bin"
    [Environment]::SetEnvironmentVariable("Path", $env:Path, [System.EnvironmentVariableTarget]::Machine)
} else {
    Write-Host "Go is already installed." -ForegroundColor Green
}

# Create Go bin path if not present
$goBin = "$env:USERPROFILE\go\bin"
if (!(Test-Path $goBin)) {
    New-Item -ItemType Directory -Path $goBin
}
$env:Path += ";$goBin"
[Environment]::SetEnvironmentVariable("Path", $env:Path, [System.EnvironmentVariableTarget]::Machine)

# Install Go tools
$tools = @(
    "github.com/projectdiscovery/subfinder/v2/cmd/subfinder@latest",
    "github.com/owasp-amass/amass/v3/...@master",
    "github.com/d3mondev/puredns/v2@latest",
    "github.com/projectdiscovery/shuffledns/cmd/shuffledns@latest",
    "github.com/projectdiscovery/dnsx/cmd/dnsx@latest",
    "github.com/tomnomnom/assetfinder@latest"
)

foreach ($tool in $tools) {
    Write-Host "Installing $tool..." -ForegroundColor Cyan
    go install -v $tool
}

# Download Findomain binary
Write-Host "Downloading Findomain..." -ForegroundColor Cyan
Invoke-WebRequest -Uri "https://github.com/Findomain/Findomain/releases/latest/download/findomain.exe" -OutFile "findomain.exe"
Move-Item "findomain.exe" "C:\Windows\System32\findomain.exe" -Force

Write-Host "Installation complete. Restart your PowerShell or system if needed." -ForegroundColor Green
