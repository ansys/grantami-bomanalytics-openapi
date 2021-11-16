 param (
	[Parameter(Mandatory=$true)]
	[string] $DefinitionPath,
	[Parameter(Mandatory=$true)]
	[string] $OutputPath,
 )


function Edit-YamlFile {
	param (
		[string]$YamlFile
		[string]$OutputPath
	)
	(Get-Content $YamlFile).replace('  - url: http://localhost', '  - url: http://localhost/mi_servicelayer') | Set-Content $OutputPath
	(Get-Content $OutputPath).replace('  /mi_servicelayer/', '  /') | Set-Content $OutputPath
	(Get-Content $OutputPath).replace('\r\n            ', ' ') | Set-Content $OutputPath
}

Edit-YamlFile $DefinitionPath $OutputPath