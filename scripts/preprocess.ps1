 param (
	[Parameter(Mandatory=$true)]
	[string] $OutputPath
 )


function Edit-YamlFile {
	param (
		[string]$OutputPath
	)
	(Get-Content $OutputPath).replace('\r\n            ', ' ') | Set-Content $OutputPath
}

Edit-YamlFile $OutputPath