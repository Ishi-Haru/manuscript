$ErrorActionPreference = "Stop"

$root = Split-Path -Parent $MyInvocation.MyCommand.Path
$buildDir = Join-Path $root "build"
$zipPath = Join-Path $buildDir "submission_source.zip"
$stageDir = Join-Path $buildDir "submission_source"

$files = @(
  "main.tex",
  "supporting_information.tex",
  "point_by_point_response.tex",
  "main.bib",
  "latexmkrc",
  "figs/TOC.png",
  "figs/slip_length_summary/previous_slip_length.png",
  "figs/schematics_of_measurement.png",
  "figs/mapping_results.png",
  "figs/scaling_result.png",
  "figs/DLC_bubble.png",
  "figs/HOPG_strong_force.png",
  "figs/mapping_colormaps.png"
)

New-Item -ItemType Directory -Force -Path $buildDir | Out-Null

if (Test-Path $zipPath) {
  Remove-Item $zipPath
}

if (Test-Path $stageDir) {
  Remove-Item $stageDir -Recurse -Force
}
New-Item -ItemType Directory -Force -Path $stageDir | Out-Null

$missing = @()
foreach ($file in $files) {
  $path = Join-Path $root $file
  if (-not (Test-Path $path)) {
    $missing += $file
  }
}

if ($missing.Count -gt 0) {
  Write-Error ("Missing required file(s): " + ($missing -join ", "))
}

foreach ($file in $files) {
  $source = Join-Path $root $file
  $dest = Join-Path $stageDir $file
  $destDir = Split-Path -Parent $dest
  New-Item -ItemType Directory -Force -Path $destDir | Out-Null
  Copy-Item -Path $source -Destination $dest
}

Compress-Archive -Path (Join-Path $stageDir "*") -DestinationPath $zipPath
Remove-Item $stageDir -Recurse -Force

Write-Host "Created: $zipPath"
