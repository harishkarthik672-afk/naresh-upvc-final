$files = @(
    "aluminium-fabrication.html",
    "false-ceiling.html",
    "gallery.html",
    "modular-kitchen.html",
    "mosquito-nets.html",
    "painting.html",
    "pvc-doors.html",
    "roofing-shed-work.html",
    "services.html",
    "ss-work.html"
)

$cssLinks = @"
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Lexend:wght@300;400;500;600;700;800&family=Poppins:wght@400;500;600;700;800&family=Inter:wght@400;500;600&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <link rel="stylesheet" href="style.css">

"@

foreach ($file in $files) {
    $filePath = "c:\Users\haris\Downloads\d\$file"
    if (Test-Path $filePath) {
        $content = Get-Content $filePath -Raw
        
        # Add CSS links before </head>
        $content = $content -replace '</head>', "$cssLinks</head>"
        
        # Write back to file
        Set-Content -Path $filePath -Value $content -NoNewline
        
        Write-Host "Updated: $file" -ForegroundColor Green
    } else {
        Write-Host "File not found: $file" -ForegroundColor Red
    }
}

Write-Host "`nAll files updated successfully!" -ForegroundColor Cyan
