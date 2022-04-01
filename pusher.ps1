cd C:\Users\8bity\Desktop\banner\bitbanner
$result = python main.py
if ( $result -eq "x" )
{
	git add -A ; git commit * --allow-empty-message -m "Seasons Greetings" ; git push
}
