$result = python main.py
if ( $result -eq "x" )
{
	git add -A && git commit * --allow-empty-message -m ''
}