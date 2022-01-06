 param (
	[Parameter(Mandatory=$true)]
	[string] $OutputPath
 )


function Edit-YamlFile {
	param (
		[string]$OutputPath
	)
	
	(Get-Content $OutputPath) | Foreach-Object {
		$_ -replace '\s?(\\r)?\\n\s+', ' ' `
		   -replace '(\\\\\s*)+', ' ' `
		} | Set-Content $OutputPath
	
}

Edit-YamlFile $OutputPath