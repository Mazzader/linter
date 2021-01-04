console.time('Time');
const fs = require('fs');
let simpleString = fs.readFileSync(process.argv[process.argv.length - 2],'utf8');
let simpleSubstring = fs.readFileSync(process.argv[process.argv.length - 1], 'utf8');
let lengthOfSubstring = simpleSubstring.length;
let indexesOfSub = new Array();
let isSub = true;
for (let i = 0; i < process.argv.length; i++)
{
	if (process.argv[i] == '-n')
		N = process.argv[i + 1];
	if (process.argv[i] == '-t')
		timeKey = true;
	if (process.argv[i] == '-c')
		cKey = true;
	if (process.argv[i] == 'b')
		Bruteforce(simpleString, simpleSubString, N, isSub);
	if (process.argv[i] == 'h1')
		HashSum(simpleString, simpleSubString, N, isSub);
	if (process.argv[i] == 'h2')
		HashSumSquares(simpleString, simpleSubString, N, isSub);
	if (process.argv[i] == 'h3')
		RabinKarpa(simpleString, simpleSubString, N, isSub);
}
	function BruteForce(simpleString, simpleSubstring, N, isSub) {
		for(let i = 0; i < simpleString.length; i++)
		{
			isSub = true;
			for(let j = 0; j < simpleSubstring.length; j++)
			{
				if(simpleString.charCodeAt(i+j) != simpleSubstring.charCodeAt(j))
				{
					isSub = false;
					break;
				}
			}
				if(isSub)
				{
					indexesOfSub.push(i)
				}
		}
		CheckN(N, array, c);
	}
	function HashSum(simpleString, simpleSubstring, N, isSub)
	{
	let sumOfHashSubstr = 0;
	let	sumOfCurrentStr = 0;
		for(let i = 0; i < lengthOfSubstring; i++)
		{
			sumOfHashSubstr = sumOfHashSubstr + simpleSubstring.charCodeAt(i);
			sumOfCurrentStr = sumOfCurrentStr + simpleString.charCodeAt(i);
		}
	console.log(sumOfHashSubstr);
		for(let i = 0; i <= simpleString.length - lengthOfSubstring;)
		{
			if(sumOfHashSubstr == sumOfCurrentStr){
			k = 0;
			C++;
			while(simpleString.charCodeAt(i + k) == simpleSubstring.charCodeAt(k) && k < simpleSubstring.length)
			{
				k++;
			}
			if (k == simpleSubstring.length)
			{
				indexesOfSub.push(i);
			}
		}
		i++
			if (i <= simpleString.length - simpleSubstring.length)
			{
				sumOfCurrentStr += simpleString.charCodeAt(i + simpleSubstring.length - 1) - simpleString.charCodeAt(i - 1);
			}
		}
		CheckN(N, array, c);
	}
function HashSumSquares(simpleString, simpleSubstring, N, isSub)
{
	let sumOfHashSubstr = 0;
	let	sumOfCurrentStr = 0;
	for(let i = 0; i < lengthOfSubstring; i++)
	{
		sumOfHashSubstr = sumOfHashSubstr*sumOfHashSubstr + simpleSubstring.charCodeAt(i) * simpleSubstring.charCodeAt(i);
		sumOfCurrentStr = sumOfCurrentStr * sumOfCurrentStr + simpleString.charCodeAt(i) * simpleString.charCodeAt(i);
	}
	console.log(sumOfHashSubstr);
	for(let i = 0; i <= simpleString.length - lengthOfSubstring;)
	{
		if(sumOfHashSubstr == sumOfCurrentStr)
		{
		k = 0;
		C++;
		while(simpleString.charCodeAt(i + k) == simpleSubstring.charCodeAt(k) && k < simpleSubstring.length)
		{
			k++;
		}
			if (k == simpleSubstring.length)
			{
				indexesOfSub.push(i);
			}
		}
		i++
			if (i <= simpleString.length - simpleSubstring.length)
			{
				sumOfCurrentStr += simpleString.charCodeAt(i + simpleSubstring.length - 1)*simpleString.charCodeAt(i + simpleSubstring.length - 1)
				- simpleString.charCodeAt(i - 1) * simpleString.charCodeAt(i - 1);
			}
	}
	CheckN(N, array, c);
}
function HashRabinKarpa(simpleString, simpleSubstring, N)
{
	let c = 0;
	let sumOfHashSubstr = 0;
	let currentSum = 0;
	let r = simpleSubString.length - 1;
	let st2 = 1;
	let array = new Array();
	let count = 0;
	while(r >= 0)
	{
    	sumOfHashSubstr += simpleSubString.charCodeAt(r) * st2;
    	currentSum += simpleString.charCodeAt(r) * st2;
    	r = r - 1;
    	st2 = st2 * 2;
	}
	st2 = st2 / 2;
	let i = 0;
	while(i <= simpleString.length - simpleSubString.length)
	{
    	if(currentSum == sumOfHashSubstr)
    	{
    		c++;
        	j = 0;
        	while((simpleString.charAt(i+j) == simpleSubstring.charAt(j)) && (j < simpleSubstring.length))
        	{
            	j++;
        	}
        	if(j == simpleSubstring.length)
        	{
           		array.push(i);
        	}
        }
    	i++
    	if(i <= simpleString.length - simpleSubString.length)
        	currentSum = (currentSum - simpleString.charCodeAt(i - 1) * st2) * 2 + simpleString.charCodeAt(i + simpleSubstring.length - 1);
    }
	CheckN(N, array, c)
}
function CheckN(N, array, c)
{
	if (N == 0)
	{
		for (let i = 0; i < array.length; i++)
		{
			console.log(array[i]);
		}
	}
	else
	{
		if (N > array.length)
			var min = array.length;
		else
			var min = N;
		for (var i = 0; i < min; i++)
			console.log(array[i]);
	}
	if (cKey)
		console.log('Количество колизий = ', c);
	if (timeKey)
		console.timeEnd('Time');
}