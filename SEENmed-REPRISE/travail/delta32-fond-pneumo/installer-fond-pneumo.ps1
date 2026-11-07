# DELTA32 - Windows installer. Only the shared background engine is changed.
$ErrorActionPreference = 'Stop'
Add-Type -AssemblyName System.Windows.Forms
$originalHash = '2B5212243CB35C387E0735BA7DD69D81'
$fixedHash = '1E8EE4390BE8942FC22F182E86A16F89'
$source = Join-Path $PSScriptRoot 'medstudy\js\pneumo-field.js'
try {
    if ((Get-FileHash -LiteralPath $source -Algorithm MD5).Hash -ne $fixedHash) {
        throw 'The Delta 32 file is missing or damaged. Extract the ZIP again.'
    }
    $dialog = New-Object System.Windows.Forms.FolderBrowserDialog
    $dialog.Description = 'Select your EXISTING medstudy folder (or its parent folder).'
    $dialog.ShowNewFolderButton = $false
    if ($dialog.ShowDialog() -ne [System.Windows.Forms.DialogResult]::OK) { exit 0 }
    $root = $dialog.SelectedPath
    if (-not (Test-Path -LiteralPath (Join-Path $root 'index.html')) -and (Test-Path -LiteralPath (Join-Path $root 'medstudy\index.html'))) {
        $root = Join-Path $root 'medstudy'
    }
    $target = Join-Path $root 'js\pneumo-field.js'
    if (-not (Test-Path -LiteralPath (Join-Path $root 'index.html')) -or -not (Test-Path -LiteralPath $target)) {
        throw 'This is not your existing medstudy folder, or the pneumology engine is missing. No files were changed.'
    }
    $hash = (Get-FileHash -LiteralPath $target -Algorithm MD5).Hash
    if ($hash -eq $fixedHash) {
        [System.Windows.Forms.MessageBox]::Show('Delta 32 is already installed. Open a pneumology lesson and press Ctrl+F5.', 'SEENmed - Delta 32') | Out-Null
        exit 0
    }
    if ($hash -ne $originalHash) {
        throw ('Your pneumology engine has a different version (MD5: ' + $hash + '). No files were changed. Send this message to your agent.')
    }
    $backup = Join-Path $root 'js\pneumo-field.before-delta32.js'
    if (Test-Path -LiteralPath $backup) {
        if ((Get-FileHash -LiteralPath $backup -Algorithm MD5).Hash -ne $originalHash) {
            throw 'A different backup already exists. No files were changed. Send this message to your agent.'
        }
    } else { Copy-Item -LiteralPath $target -Destination $backup }
    Copy-Item -LiteralPath $source -Destination $target -Force
    if ((Get-FileHash -LiteralPath $target -Algorithm MD5).Hash -ne $fixedHash) {
        Copy-Item -LiteralPath $backup -Destination $target -Force
        throw 'Installation verification failed. The original was restored.'
    }
    [System.Windows.Forms.MessageBox]::Show('Done! Open a pneumology lesson and press Ctrl+F5. Only its shared background engine was changed; your lessons and dashboard were not replaced.', 'SEENmed - Delta 32') | Out-Null
} catch {
    [System.Windows.Forms.MessageBox]::Show($_.Exception.Message, 'SEENmed - Installation stopped', 'OK', 'Error') | Out-Null
    exit 1
}
