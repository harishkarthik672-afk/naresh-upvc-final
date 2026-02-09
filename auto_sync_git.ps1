
$intervalSeconds = 30
Write-Host "Started Auto-Git Sync. Checking for changes every $intervalSeconds seconds..."
Write-Host "Press Ctrl+C to stop."

while ($true) {
    $status = git status --porcelain
    if ($status) {
        $timestamp = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
        Write-Host "[$timestamp] Changes detected. Syncing..."
        
        git add .
        git commit -m "Auto-save: $timestamp"
        git push origin main
        
        Write-Host "[$timestamp] Sync complete."
    }
    Start-Sleep -Seconds $intervalSeconds
}
