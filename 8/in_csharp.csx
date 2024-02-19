int cnt = 0;
foreach (string A in Enumerable.Range(1000, 9000 - 1).Select(i => i.ToString()))
{
	if (A[0] != A[1] && A[1] != A[2] && A[2] != A[3]) 
		continue;
	foreach (char d in "0123456789")
		if (((ReadOnlySpan<char>)A).Count(d) > 2)
			break;
	else
		cnt++;
}
Console.WriteLine(cnt);