# DELTA34: patch only the installed cardio background engine. Windows PowerShell 5.1.
$ErrorActionPreference = 'Stop'
Add-Type -AssemblyName System.Windows.Forms
$utf8 = New-Object System.Text.UTF8Encoding($false, $true)
$marker = 'SEENMED_CARDIO_THEMES_DELTA34'
$fragmentDir = Join-Path $PSScriptRoot 'patch'
$temp = $null
$backup = $null
$target = $null
$originalHash = $null
$replaced = $false
try {
    $checks = @{
        'cardio-skin-fragment.js' = '8164E3C967E81B64C0024A89AB2264F1'
        'cardio-particle-fragment.js' = 'C63CC8FA1C5FAAAAC062825740F3B96A'
        'signature-carte.txt' = '878708071198CED09CEC66F6D804F21A'
    }
    foreach ($name in $checks.Keys) {
        $p = Join-Path $fragmentDir $name
        if (-not (Test-Path -LiteralPath $p -PathType Leaf) -or (Get-FileHash -LiteralPath $p -Algorithm MD5).Hash -ne $checks[$name]) {
            throw 'The Delta 34 patch files are missing or damaged. Extract the ZIP again. No files were changed.'
        }
    }
    $dialog = New-Object System.Windows.Forms.FolderBrowserDialog
    $dialog.Description = 'Select your EXISTING medstudy folder (or its parent folder). Do NOT select the reference folder inside Delta 34.'
    $dialog.ShowNewFolderButton = $false
    if ($dialog.ShowDialog() -ne [System.Windows.Forms.DialogResult]::OK) { exit 0 }
    $root = $dialog.SelectedPath
    if (-not (Test-Path -LiteralPath (Join-Path $root 'index.html')) -and (Test-Path -LiteralPath (Join-Path $root 'medstudy\index.html'))) { $root = Join-Path $root 'medstudy' }
    $target = Join-Path $root 'js\cardio-field.js'
    if (-not (Test-Path -LiteralPath (Join-Path $root 'index.html') -PathType Leaf) -or -not (Test-Path -LiteralPath $target -PathType Leaf)) {
        throw 'This is not your existing medstudy folder, or the cardio engine is missing. No files were changed.'
    }
    $reference = Join-Path $PSScriptRoot 'medstudy\js\cardio-field.js'
    if ((Test-Path -LiteralPath $reference) -and ((Resolve-Path -LiteralPath $target).Path -eq (Resolve-Path -LiteralPath $reference).Path)) {
        throw 'You selected the reference folder in the Delta 34 ZIP. Select your existing medstudy folder instead. No files were changed.'
    }
    $bytes = [System.IO.File]::ReadAllBytes($target)
    $hasBom = $bytes.Length -ge 3 -and $bytes[0] -eq 0xEF -and $bytes[1] -eq 0xBB -and $bytes[2] -eq 0xBF
    $offset = if ($hasBom) { 3 } else { 0 }
    $original = $utf8.GetString($bytes, $offset, $bytes.Length - $offset)
    $originalHash = (Get-FileHash -LiteralPath $target -Algorithm MD5).Hash
    if ($original.Contains($marker)) {
        [System.Windows.Forms.MessageBox]::Show('Delta 34 is already present. Open a cardio lesson and press Ctrl+F5.', 'SEENmed - Delta 34') | Out-Null
        exit 0
    }
    $pattern = '(?s)\bvar\s+THEME_MAP\s*=\s*\{.*?\};\s*function\s+readTheme\s*\(\s*\)\s*\{.*?\r?\n[ \t]*\}'
    $matches = [regex]::Matches($original, $pattern)
    $signature = [System.IO.File]::ReadAllText((Join-Path $fragmentDir 'signature-carte.txt'), $utf8)
    if ($matches.Count -ne 1 -or $matches[0].Value.Replace("`r`n", "`n") -cne $signature.Replace("`r`n", "`n") -or -not $original.Contains("getElementById('cardioFieldCanvas')")) {
        throw ('This cardio engine has an incompatible palette structure (MD5: ' + $originalHash + '). No files were changed. Send this message to your agent.')
    }
    $read = [regex]::Matches($original, '\bfunction\s+readTheme\s*\(\s*\)')
    if ($read.Count -ne 1) { throw 'The theme entry point is ambiguous. No files were changed.' }
    $skin = [System.IO.File]::ReadAllText((Join-Path $fragmentDir 'cardio-skin-fragment.js'), $utf8)
    $particles = [System.IO.File]::ReadAllText((Join-Path $fragmentDir 'cardio-particle-fragment.js'), $utf8)
    $changed = $original.Insert($read[0].Index, $particles + "`n    ")
    $changed = $skin + "`n" + $changed
    $newBytes = $utf8.GetBytes($changed)
    if ($hasBom) { $newBytes = [byte[]](@(0xEF,0xBB,0xBF) + $newBytes) }
    $unique = [guid]::NewGuid().ToString('N')
    $temp = Join-Path (Split-Path -Parent $target) ('cardio-field.delta34-' + $unique + '.tmp')
    $backup = Join-Path (Split-Path -Parent $target) ('cardio-field.before-delta34-' + $unique + '.js')
    [System.IO.File]::WriteAllBytes($temp, $newBytes)
    $newHash = (Get-FileHash -LiteralPath $temp -Algorithm MD5).Hash
    if ((Get-FileHash -LiteralPath $target -Algorithm MD5).Hash -ne $originalHash) { throw 'The engine changed during installation. No replacement was made.' }
    [System.IO.File]::Replace($temp, $target, $backup)
    $replaced = $true
    if ((Get-FileHash -LiteralPath $target -Algorithm MD5).Hash -ne $newHash -or (Get-FileHash -LiteralPath $backup -Algorithm MD5).Hash -ne $originalHash) {
        throw 'Installation verification failed.'
    }
    [System.Windows.Forms.MessageBox]::Show('Done! Only the cardio background engine was changed. Your original engine was saved in the js folder. Open a cardio lesson and press Ctrl+F5.', 'SEENmed - Delta 34') | Out-Null
} catch {
    $message = $_.Exception.Message
    if ($replaced -and $backup -and (Test-Path -LiteralPath $backup)) {
        try { Copy-Item -LiteralPath $backup -Destination $target -Force; $message += ' The original engine was restored from the backup.' }
        catch { $message += (' Restore manually from: ' + $backup) }
    }
    [System.Windows.Forms.MessageBox]::Show($message, 'SEENmed - Installation stopped', 'OK', 'Error') | Out-Null
    exit 1
} finally {
    if ($temp -and (Test-Path -LiteralPath $temp)) { Remove-Item -LiteralPath $temp -Force -ErrorAction SilentlyContinue }
}
