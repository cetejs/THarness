param(
    [Parameter(Mandatory = $true)]
    [string]$Path,

    [switch]$Raw
)

$ErrorActionPreference = "Stop"

$utf8 = [System.Text.UTF8Encoding]::new($false)
[Console]::OutputEncoding = $utf8
[Console]::InputEncoding = $utf8
$OutputEncoding = $utf8

if ($Raw) {
    Get-Content -LiteralPath $Path -Encoding UTF8 -Raw
} else {
    Get-Content -LiteralPath $Path -Encoding UTF8
}
