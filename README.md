<h1>Autocorrect Spell Checker</h1>
<p>Goals: </p>
<p>(1) Compare runtime efficiency between Levanstein distance and Wagner-fisher dynamic programming approach</p>
<p>(2) Create a command line tool for non-technical users to quickly autocorrect their mistakes</p>

<h2>Runtime Efficiency</h2>
With Levanstein distance: O(3^min(m,n))

With Wagner-fisher distance: O(mn)

With a test dataset of 10000 trials with words of length 5 or less, these were the following results:
```
Comparing Average Computing Time...
Wagner-fisher: 1.3365840911865235e-05
Levanstein: 0.00029788732528686525
```
The Wagner-fisher approach proves more than 20x faster per word over the Levanstein approach. This difference is only compounded as the words of comparison grow longer.

<h2>Document Autocorrecter Usage</h2>
Sample input: <b>hello wrld</b>

```
Spelling error: wrld
Did you mean: 
1. wild         2. wold         3. world        4. 3rd  5. Ald  6. (Leave as is)
Enter an option: 3
```
Sample output: <b>hello world</b>
