# Footer HTML Fix Script
$file = "e:\CM\MU\templates\base.html"
$content = Get-Content $file -Raw
$content = $content -replace '\\"', '"'
Set-Content -Path $file -Value $content
Write-Host "Fixed escaped quotes in base.html"
