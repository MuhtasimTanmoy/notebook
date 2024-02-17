# VSCode

- vscode auto completion snippet

```json
{
	// Place your snippets for cpp here. Each snippet is defined under a snippet name and has a prefix, body and 
	// description. The prefix is what is used to trigger the snippet and the body will be expanded and inserted. Possible variables are:
	// $1, $2 for tab stops, $0 for the final cursor position, and ${1:label}, ${2:another} for placeholders. Placeholders with the 
	// same ids are connected.
	// Example:
	// "Print to console": {
	// 	"prefix": "log",
	// 	"body": [
	// 		"console.log('$1');",Certificate add"
	
	// 		"$2"
	// 	],
	// 	"description": "Log output to console"
	// }
	"comment": {
		"prefix": "q",
		"body": [
			"cout << endl<< \"$1 \"<< \"....\" << $2 << \"....\" << endl;"
		],
		"description": "Log output to console"
	},
	"for": {
		"prefix": "fo",
		"body": [
			"for (int i = 0; i < n; i++){}"
		],
		"description": "Log output to console"
	},
	"temp": {
		"prefix": "pr",
		"body": [
			"\nfor (int i = 0; i < n; i++){\ncout<<li[i]<<\" \";\n}"
		],
		"description": "Log output to console"
	},
	"tem": {
		"prefix": "te",
		"body": [
			"int n;\ncin>>n;\nint li[n];\nfor (int i = 0; i < n; i++){\ncin>>li[i];\n}"
		],
		"description": "Log output to console"
	}
}

```