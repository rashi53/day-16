Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 21:26:53) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import numpy
>>> dir(numpy)
['ALLOW_THREADS', 'AxisError', 'BUFSIZE', 'CLIP', 'ComplexWarning', 'DataSource', 'ERR_CALL', 'ERR_DEFAULT', 'ERR_IGNORE', 'ERR_LOG', 'ERR_PRINT', 'ERR_RAISE', 'ERR_WARN', 'FLOATING_POINT_SUPPORT', 'FPE_DIVIDEBYZERO', 'FPE_INVALID', 'FPE_OVERFLOW', 'FPE_UNDERFLOW', 'False_', 'Inf', 'Infinity', 'MAXDIMS', 'MAY_SHARE_BOUNDS', 'MAY_SHARE_EXACT', 'MachAr', 'ModuleDeprecationWarning', 'NAN', 'NINF', 'NZERO', 'NaN', 'PINF', 'PZERO', 'RAISE', 'RankWarning', 'SHIFT_DIVIDEBYZERO', 'SHIFT_INVALID', 'SHIFT_OVERFLOW', 'SHIFT_UNDERFLOW', 'ScalarType', 'Tester', 'TooHardError', 'True_', 'UFUNC_BUFSIZE_DEFAULT', 'UFUNC_PYVALS_NAME', 'VisibleDeprecationWarning', 'WRAP', '_NoValue', '_UFUNC_API', '__NUMPY_SETUP__', '__all__', '__builtins__', '__cached__', '__config__', '__doc__', '__file__', '__git_revision__', '__loader__', '__name__', '__package__', '__path__', '__spec__', '__version__', '_add_newdoc_ufunc', '_arg', '_distributor_init', '_globals', '_mat', '_pytesttester', 'abs', 'absolute', 'absolute_import', 'add', 'add_docstring', 'add_newdoc', 'add_newdoc_ufunc', 'alen', 'all', 'allclose', 'alltrue', 'amax', 'amin', 'angle', 'any', 'append', 'apply_along_axis', 'apply_over_axes', 'arange', 'arccos', 'arccosh', 'arcsin', 'arcsinh', 'arctan', 'arctan2', 'arctanh', 'argmax', 'argmin', 'argpartition', 'argsort', 'argwhere', 'around', 'array', 'array2string', 'array_equal', 'array_equiv', 'array_repr', 'array_split', 'array_str', 'asanyarray', 'asarray', 'asarray_chkfinite', 'ascontiguousarray', 'asfarray', 'asfortranarray', 'asmatrix', 'asscalar', 'atleast_1d', 'atleast_2d', 'atleast_3d', 'average', 'bartlett', 'base_repr', 'binary_repr', 'bincount', 'bitwise_and', 'bitwise_not', 'bitwise_or', 'bitwise_xor', 'blackman', 'block', 'bmat', 'bool', 'bool8', 'bool_', 'broadcast', 'broadcast_arrays', 'broadcast_to', 'busday_count', 'busday_offset', 'busdaycalendar', 'byte', 'byte_bounds', 'bytes0', 'bytes_', 'c_', 'can_cast', 'cast', 'cbrt', 'cdouble', 'ceil', 'cfloat', 'char', 'character', 'chararray', 'choose', 'clip', 'clongdouble', 'clongfloat', 'column_stack', 'common_type', 'compare_chararrays', 'compat', 'complex', 'complex128', 'complex64', 'complex_', 'complexfloating', 'compress', 'concatenate', 'conj', 'conjugate', 'convolve', 'copy', 'copysign', 'copyto', 'core', 'corrcoef', 'correlate', 'cos', 'cosh', 'count_nonzero', 'cov', 'cross', 'csingle', 'ctypeslib', 'cumprod', 'cumproduct', 'cumsum', 'datetime64', 'datetime_as_string', 'datetime_data', 'deg2rad', 'degrees', 'delete', 'deprecate', 'deprecate_with_doc', 'diag', 'diag_indices', 'diag_indices_from', 'diagflat', 'diagonal', 'diff', 'digitize', 'disp', 'divide', 'division', 'divmod', 'dot', 'double', 'dsplit', 'dstack', 'dtype', 'e', 'ediff1d', 'einsum', 'einsum_path', 'emath', 'empty', 'empty_like', 'equal', 'errstate', 'euler_gamma', 'exp', 'exp2', 'expand_dims', 'expm1', 'extract', 'eye', 'fabs', 'fastCopyAndTranspose', 'fft', 'fill_diagonal', 'find_common_type', 'finfo', 'fix', 'flatiter', 'flatnonzero', 'flexible', 'flip', 'fliplr', 'flipud', 'float', 'float16', 'float32', 'float64', 'float_', 'float_power', 'floating', 'floor', 'floor_divide', 'fmax', 'fmin', 'fmod', 'format_float_positional', 'format_float_scientific', 'format_parser', 'frexp', 'frombuffer', 'fromfile', 'fromfunction', 'fromiter', 'frompyfunc', 'fromregex', 'fromstring', 'full', 'full_like', 'fv', 'gcd', 'generic', 'genfromtxt', 'geomspace', 'get_array_wrap', 'get_include', 'get_printoptions', 'getbufsize', 'geterr', 'geterrcall', 'geterrobj', 'gradient', 'greater', 'greater_equal', 'half', 'hamming', 'hanning', 'heaviside', 'histogram', 'histogram2d', 'histogram_bin_edges', 'histogramdd', 'hsplit', 'hstack', 'hypot', 'i0', 'identity', 'iinfo', 'imag', 'in1d', 'index_exp', 'indices', 'inexact', 'inf', 'info', 'infty', 'inner', 'insert', 'int', 'int0', 'int16', 'int32', 'int64', 'int8', 'int_', 'int_asbuffer', 'intc', 'integer', 'interp', 'intersect1d', 'intp', 'invert', 'ipmt', 'irr', 'is_busday', 'isclose', 'iscomplex', 'iscomplexobj', 'isfinite', 'isfortran', 'isin', 'isinf', 'isnan', 'isnat', 'isneginf', 'isposinf', 'isreal', 'isrealobj', 'isscalar', 'issctype', 'issubclass_', 'issubdtype', 'issubsctype', 'iterable', 'ix_', 'kaiser', 'kron', 'lcm', 'ldexp', 'left_shift', 'less', 'less_equal', 'lexsort', 'lib', 'linalg', 'linspace', 'little_endian', 'load', 'loads', 'loadtxt', 'log', 'log10', 'log1p', 'log2', 'logaddexp', 'logaddexp2', 'logical_and', 'logical_not', 'logical_or', 'logical_xor', 'logspace', 'long', 'longcomplex', 'longdouble', 'longfloat', 'longlong', 'lookfor', 'ma', 'mafromtxt', 'mask_indices', 'mat', 'math', 'matmul', 'matrix', 'matrixlib', 'max', 'maximum', 'maximum_sctype', 'may_share_memory', 'mean', 'median', 'memmap', 'meshgrid', 'mgrid', 'min', 'min_scalar_type', 'minimum', 'mintypecode', 'mirr', 'mod', 'modf', 'moveaxis', 'msort', 'multiply', 'nan', 'nan_to_num', 'nanargmax', 'nanargmin', 'nancumprod', 'nancumsum', 'nanmax', 'nanmean', 'nanmedian', 'nanmin', 'nanpercentile', 'nanprod', 'nanquantile', 'nanstd', 'nansum', 'nanvar', 'nbytes', 'ndarray', 'ndenumerate', 'ndfromtxt', 'ndim', 'ndindex', 'nditer', 'negative', 'nested_iters', 'newaxis', 'nextafter', 'nonzero', 'not_equal', 'nper', 'npv', 'numarray', 'number', 'obj2sctype', 'object', 'object0', 'object_', 'ogrid', 'oldnumeric', 'ones', 'ones_like', 'outer', 'packbits', 'pad', 'partition', 'percentile', 'pi', 'piecewise', 'place', 'pmt', 'poly', 'poly1d', 'polyadd', 'polyder', 'polydiv', 'polyfit', 'polyint', 'polymul', 'polynomial', 'polysub', 'polyval', 'positive', 'power', 'ppmt', 'print_function', 'printoptions', 'prod', 'product', 'promote_types', 'ptp', 'put', 'put_along_axis', 'putmask', 'pv', 'quantile', 'r_', 'rad2deg', 'radians', 'random', 'rank', 'rate', 'ravel', 'ravel_multi_index', 'real', 'real_if_close', 'rec', 'recarray', 'recfromcsv', 'recfromtxt', 'reciprocal', 'record', 'remainder', 'repeat', 'require', 'reshape', 'resize', 'result_type', 'right_shift', 'rint', 'roll', 'rollaxis', 'roots', 'rot90', 'round', 'round_', 'row_stack', 's_', 'safe_eval', 'save', 'savetxt', 'savez', 'savez_compressed', 'sctype2char', 'sctypeDict', 'sctypeNA', 'sctypes', 'searchsorted', 'select', 'set_numeric_ops', 'set_printoptions', 'set_string_function', 'setbufsize', 'setdiff1d', 'seterr', 'seterrcall', 'seterrobj', 'setxor1d', 'shape', 'shares_memory', 'short', 'show_config', 'sign', 'signbit', 'signedinteger', 'sin', 'sinc', 'single', 'singlecomplex', 'sinh', 'size', 'sometrue', 'sort', 'sort_complex', 'source', 'spacing', 'split', 'sqrt', 'square', 'squeeze', 'stack', 'std', 'str', 'str0', 'str_', 'string_', 'subtract', 'sum', 'swapaxes', 'sys', 'take', 'take_along_axis', 'tan', 'tanh', 'tensordot', 'test', 'testing', 'tile', 'timedelta64', 'trace', 'tracemalloc_domain', 'transpose', 'trapz', 'tri', 'tril', 'tril_indices', 'tril_indices_from', 'trim_zeros', 'triu', 'triu_indices', 'triu_indices_from', 'true_divide', 'trunc', 'typeDict', 'typeNA', 'typecodes', 'typename', 'ubyte', 'ufunc', 'uint', 'uint0', 'uint16', 'uint32', 'uint64', 'uint8', 'uintc', 'uintp', 'ulonglong', 'unicode', 'unicode_', 'union1d', 'unique', 'unpackbits', 'unravel_index', 'unsignedinteger', 'unwrap', 'ushort', 'vander', 'var', 'vdot', 'vectorize', 'version', 'void', 'void0', 'vsplit', 'vstack', 'warnings', 'where', 'who', 'zeros', 'zeros_like']
>>> 
>>> 
================= RESTART: C:/python/Python37-32/day16/1.py =================
Traceback (most recent call last):
  File "C:/python/Python37-32/day16/1.py", line 3, in <module>
    a=np.arrary(b)
AttributeError: module 'numpy' has no attribute 'arrary'
>>> 
================= RESTART: C:/python/Python37-32/day16/1.py =================
Traceback (most recent call last):
  File "C:/python/Python37-32/day16/1.py", line 3, in <module>
    a=np.arrary(b)
AttributeError: module 'numpy' has no attribute 'arrary'
>>> 
================= RESTART: C:/python/Python37-32/day16/1.py =================
[1 2 3]
type of a: <class 'numpy.ndarray'>
[[1 2 3]
 [4 5 6]]
type of a: <class 'numpy.ndarray'>
>>> 
================= RESTART: C:/python/Python37-32/day16/2.py =================
memory occupied by list: 14000
memory occupied by numpy array: 4000
>>> 
================= RESTART: C:/python/Python37-32/day16/3.py =================
Traceback (most recent call last):
  File "C:/python/Python37-32/day16/3.py", line 8, in <module>
    start=time.time()
NameError: name 'time' is not defined
>>> 
================= RESTART: C:/python/Python37-32/day16/3.py =================
time taken by the list operation: 1395.9169387817383
time taken by numpy array operation: 4974.794387817383
>>> 
================= RESTART: C:/python/Python37-32/day16/3.py =================
time taken by the list operation: 245742.65480041504
time taken by numpy array operation: 59141.8981552124
>>> 
================= RESTART: C:/python/Python37-32/day16/4.py =================
1
2
4
int32
3
7
(3,)
(2, 3)
>>> 
================= RESTART: C:/python/Python37-32/day16/5.py =================
[[1 2 3 4]
 [3 4 5 6]]
[[1 2]
 [3 4]
 [3 4]
 [5 6]]
3
15
[ 4 16]
out: [[ 1  2  3  4]
 [13 14 15 16]
 [21 22 23 24]]
[ 4 16]
Traceback (most recent call last):
  File "C:/python/Python37-32/day16/5.py", line 13, in <module>
    a=np.linespace(1,3,5)
AttributeError: module 'numpy' has no attribute 'linespace'
>>> 
================= RESTART: C:/python/Python37-32/day16/5.py =================
[[1 2 3 4]
 [3 4 5 6]]
[[1 2]
 [3 4]
 [3 4]
 [5 6]]
3
15
[ 4 16]
out: [[ 1  2  3  4]
 [13 14 15 16]
 [21 22 23 24]]
[ 4 16]
[1.  1.5 2.  2.5 3. ]
[1.         1.22222222 1.44444444 1.66666667 1.88888889 2.11111111
 2.33333333 2.55555556 2.77777778 3.        ]
>>> 
================= RESTART: C:/python/Python37-32/day16/6.py =================
min: 1
max: 4
sum: 10
min: 1
max: 8
sum: 36
>>> 
================= RESTART: C:/python/Python37-32/day16/7.py =================
a:
 [[1 2 3]
 [3 4 5]]
sum axis 0: [4 6 8]
sum axis 1: [ 6 12]
>>> 
================= RESTART: C:/python/Python37-32/day16/8.py =================
sqrt: [[1.         1.41421356 1.73205081]
 [1.73205081 2.         2.23606798]]
mean: 3.0
std: 1.2909944487358056
>>> 
================= RESTART: C:/python/Python37-32/day16/9.py =================
[[ 2  4  6]
 [ 6  8 10]]
[[0 0 0]
 [0 0 0]]
[[ 1  4  9]
 [ 9 16 25]]
[[1. 1. 1.]
 [1. 1. 1.]]
np.vstack:
 [[1 2 3]
 [3 4 5]
 [1 2 3]
 [3 4 5]]
np.hstack:
 [[1 2 3 1 2 3]
 [3 4 5 3 4 5]]
[1 2 3 3 4 5]
>>> 
================= RESTART: C:/python/Python37-32/day16/10.py =================
X:
 [-1.00000000e+00 -9.00000000e-01 -8.00000000e-01 -7.00000000e-01
 -6.00000000e-01 -5.00000000e-01 -4.00000000e-01 -3.00000000e-01
 -2.00000000e-01 -1.00000000e-01 -2.22044605e-16  1.00000000e-01
  2.00000000e-01  3.00000000e-01  4.00000000e-01  5.00000000e-01
  6.00000000e-01  7.00000000e-01  8.00000000e-01  9.00000000e-01
  1.00000000e+00  1.10000000e+00  1.20000000e+00  1.30000000e+00
  1.40000000e+00  1.50000000e+00  1.60000000e+00  1.70000000e+00
  1.80000000e+00  1.90000000e+00  2.00000000e+00  2.10000000e+00
  2.20000000e+00  2.30000000e+00  2.40000000e+00  2.50000000e+00
  2.60000000e+00  2.70000000e+00  2.80000000e+00  2.90000000e+00
  3.00000000e+00  3.10000000e+00  3.20000000e+00  3.30000000e+00
  3.40000000e+00  3.50000000e+00  3.60000000e+00  3.70000000e+00
  3.80000000e+00  3.90000000e+00  4.00000000e+00  4.10000000e+00
  4.20000000e+00  4.30000000e+00  4.40000000e+00  4.50000000e+00
  4.60000000e+00  4.70000000e+00  4.80000000e+00  4.90000000e+00
  5.00000000e+00  5.10000000e+00  5.20000000e+00  5.30000000e+00
  5.40000000e+00  5.50000000e+00  5.60000000e+00  5.70000000e+00
  5.80000000e+00  5.90000000e+00  6.00000000e+00  6.10000000e+00
  6.20000000e+00  6.30000000e+00  6.40000000e+00  6.50000000e+00
  6.60000000e+00  6.70000000e+00  6.80000000e+00  6.90000000e+00
  7.00000000e+00  7.10000000e+00  7.20000000e+00  7.30000000e+00
  7.40000000e+00  7.50000000e+00  7.60000000e+00  7.70000000e+00
  7.80000000e+00  7.90000000e+00  8.00000000e+00  8.10000000e+00
  8.20000000e+00  8.30000000e+00  8.40000000e+00  8.50000000e+00
  8.60000000e+00  8.70000000e+00  8.80000000e+00  8.90000000e+00
  9.00000000e+00  9.10000000e+00  9.20000000e+00  9.30000000e+00
  9.40000000e+00]
Y:
 [-8.41470985e-01 -7.83326910e-01 -7.17356091e-01 -6.44217687e-01
 -5.64642473e-01 -4.79425539e-01 -3.89418342e-01 -2.95520207e-01
 -1.98669331e-01 -9.98334166e-02 -2.22044605e-16  9.98334166e-02
  1.98669331e-01  2.95520207e-01  3.89418342e-01  4.79425539e-01
  5.64642473e-01  6.44217687e-01  7.17356091e-01  7.83326910e-01
  8.41470985e-01  8.91207360e-01  9.32039086e-01  9.63558185e-01
  9.85449730e-01  9.97494987e-01  9.99573603e-01  9.91664810e-01
  9.73847631e-01  9.46300088e-01  9.09297427e-01  8.63209367e-01
  8.08496404e-01  7.45705212e-01  6.75463181e-01  5.98472144e-01
  5.15501372e-01  4.27379880e-01  3.34988150e-01  2.39249329e-01
  1.41120008e-01  4.15806624e-02 -5.83741434e-02 -1.57745694e-01
 -2.55541102e-01 -3.50783228e-01 -4.42520443e-01 -5.29836141e-01
 -6.11857891e-01 -6.87766159e-01 -7.56802495e-01 -8.18277111e-01
 -8.71575772e-01 -9.16165937e-01 -9.51602074e-01 -9.77530118e-01
 -9.93691004e-01 -9.99923258e-01 -9.96164609e-01 -9.82452613e-01
 -9.58924275e-01 -9.25814682e-01 -8.83454656e-01 -8.32267442e-01
 -7.72764488e-01 -7.05540326e-01 -6.31266638e-01 -5.50685543e-01
 -4.64602179e-01 -3.73876665e-01 -2.79415498e-01 -1.82162504e-01
 -8.30894028e-02  1.68139005e-02  1.16549205e-01  2.15119988e-01
  3.11541364e-01  4.04849921e-01  4.94113351e-01  5.78439764e-01
  6.56986599e-01  7.28969040e-01  7.93667864e-01  8.50436621e-01
  8.98708096e-01  9.37999977e-01  9.67919672e-01  9.88168234e-01
  9.98543345e-01  9.98941342e-01  9.89358247e-01  9.69889811e-01
  9.40730557e-01  9.02171834e-01  8.54598908e-01  7.98487113e-01
  7.34397098e-01  6.62969230e-01  5.84917193e-01  5.01020856e-01
  4.12118485e-01  3.19098362e-01  2.22889914e-01  1.24454424e-01
  2.47754255e-02]

================= RESTART: C:/python/Python37-32/day16/10.py =================
X:
 [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Y:
 [ 4  7  1  3  2  8  9  6  5 10]

================= RESTART: C:/python/Python37-32/day16/11.py =================
Traceback (most recent call last):
  File "C:/python/Python37-32/day16/11.py", line 8, in <module>
    plt.bars(x_pos,performance,align='center')
AttributeError: module 'matplotlib.pyplot' has no attribute 'bars'
>>> 
================= RESTART: C:/python/Python37-32/day16/11.py =================

================= RESTART: C:/python/Python37-32/day16/12.py =================

================= RESTART: C:/python/Python37-32/day16/12.py =================

================= RESTART: C:/python/Python37-32/day16/13.py =================
Traceback (most recent call last):
  File "C:/python/Python37-32/day16/13.py", line 8, in <module>
    plt.pie(sies,explode=explode,labels=labels,colors=colors,autopct='%1.21%%',shadow=True,startangle=140)
NameError: name 'sies' is not defined
>>> 
================= RESTART: C:/python/Python37-32/day16/13.py =================
Traceback (most recent call last):
  File "C:/python/Python37-32/day16/13.py", line 10, in <module>
    autopct='%1.21%%',shadow=True,startangle=140)
  File "C:\python\Python37-32\lib\site-packages\matplotlib\pyplot.py", line 2787, in pie
    data is not None else {}))
  File "C:\python\Python37-32\lib\site-packages\matplotlib\__init__.py", line 1601, in inner
    return func(ax, *map(sanitize_sequence, args), **kwargs)
  File "C:\python\Python37-32\lib\site-packages\matplotlib\axes\_axes.py", line 3065, in pie
    s = autopct % (100. * frac)
ValueError: unsupported format character '%' (0x25) at index 5
>>> 
================= RESTART: C:/python/Python37-32/day16/13.py =================

================= RESTART: C:/python/Python37-32/day16/14.py =================
'c' argument looks like a single numeric RGB or RGBA sequence, which should be avoided as value-mapping will have precedence in case its length matches with 'x' & 'y'.  Please use a 2-D array with a single row if you really want to specify the same RGB or RGBA value for all points.
Traceback (most recent call last):
  File "C:/python/Python37-32/day16/14.py", line 12, in <module>
    plt.x.label('x')
AttributeError: module 'matplotlib.pyplot' has no attribute 'x'
>>> 
================= RESTART: C:/python/Python37-32/day16/14.py =================
'c' argument looks like a single numeric RGB or RGBA sequence, which should be avoided as value-mapping will have precedence in case its length matches with 'x' & 'y'.  Please use a 2-D array with a single row if you really want to specify the same RGB or RGBA value for all points.
Traceback (most recent call last):
  File "C:/python/Python37-32/day16/14.py", line 12, in <module>
    plt.x.label('x')
AttributeError: module 'matplotlib.pyplot' has no attribute 'x'
>>> 
================= RESTART: C:/python/Python37-32/day16/14.py =================
'c' argument looks like a single numeric RGB or RGBA sequence, which should be avoided as value-mapping will have precedence in case its length matches with 'x' & 'y'.  Please use a 2-D array with a single row if you really want to specify the same RGB or RGBA value for all points.

================= RESTART: C:/python/Python37-32/day16/15.py =================
Traceback (most recent call last):
  File "C:/python/Python37-32/day16/15.py", line 11, in <module>
    chartBox=ax.get+position()
AttributeError: 'AxesSubplot' object has no attribute 'get'
>>> 
================= RESTART: C:/python/Python37-32/day16/15.py =================
Traceback (most recent call last):
  File "C:/python/Python37-32/day16/15.py", line 12, in <module>
    ax.set_position([chartBox.x(),chartBox.y(),chartBox.width*0.6,chartBox.height])
AttributeError: 'Bbox' object has no attribute 'x'
>>> 
================= RESTART: C:/python/Python37-32/day16/15.py =================

================= RESTART: C:/python/Python37-32/day16/16.py =================
Traceback (most recent call last):
  File "C:/python/Python37-32/day16/16.py", line 9, in <module>
    plt.gcf().auto.fmt_xdate()
AttributeError: 'Figure' object has no attribute 'auto'
>>> 
