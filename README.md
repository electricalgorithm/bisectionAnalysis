# bisectionAnalysis
This program made for seeking roots of any function via giving error rate. Program using Bisection Method from Numerical Analysis field of Mathematics.


## Usage
```bash
python3 bisectionAnalysis.py -f <function> -l <lower number of range> -h <higher number of range> -e <error rate>
```

**-f** : To initialize the function. Only one parameter (x) accepted. The function you provide must be formatted as Python scripts. You can't use any other unknown except (lower case) "x".

For example, if you want to write a function like this:
```math
15(x)^3 + (14x)^2 + |-5| + 10x^(-1)
```
You need to write it as like this:
```python
15(x**3) + (14*x)**2 + abs(-5) + 10(x**(-1))
```
>NOTE: Math library is included. You can use it.
For more information: https://docs.python.org/3/library/math.html

**-l** : To initialize range's lower number.

**-h** : To initialize range's higher number.

To search root in [a, b] and b > a, you need to write as like: "-l a -h b". Numbers a and b are also included in the range/gap.

> NOTE: Program gives error when you tried to give -l a -h -a because
(a + -a)/2 is zero. You should careful about it.

**-e** : To initialize error number as relative approach error.
Relative approach error is a error type and can be formulated:
a: last found root, b: earlier found root -->   (a-b)/a

## License
This program/script made by Gökhan Koçmarlı (electricalgorithm in GitHub). The program is licensed under the Mozilla Public License 2.0 (MPL-2.0).
To see license's details use **--license** command or check the LICENSE file.

## Contribution
All contributions are excepted. Make the world free and open source together!
