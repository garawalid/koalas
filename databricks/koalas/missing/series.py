#
# Copyright (C) 2019 Databricks, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

from databricks.koalas.missing import _unsupported_function, _unsupported_property


def unsupported_function(method_name, deprecated=False):
    return _unsupported_function(class_name='pd.Series', method_name=method_name,
                                 deprecated=deprecated)


def unsupported_property(property_name, deprecated=False):
    return _unsupported_property(class_name='pd.Series', property_name=property_name,
                                 deprecated=deprecated)


class _MissingPandasLikeSeries(object):

    # Properties
    T = unsupported_property('T')
    argmax = unsupported_function('argmax')
    argmin = unsupported_function('argmin')
    array = unsupported_property('array')
    asobject = unsupported_property('asobject')
    at = unsupported_property('at')
    axes = unsupported_property('axes')
    base = unsupported_property('base')
    data = unsupported_property('data')
    empty = unsupported_property('empty')
    flags = unsupported_property('flags')
    ftype = unsupported_property('ftype')
    ftypes = unsupported_property('ftypes')
    hasnans = unsupported_property('hasnans')
    iat = unsupported_property('iat')
    imag = unsupported_property('imag')
    is_copy = unsupported_property('is_copy')
    is_monotonic = unsupported_property('is_monotonic')
    is_monotonic_decreasing = unsupported_property('is_monotonic_decreasing')
    is_monotonic_increasing = unsupported_property('is_monotonic_increasing')
    itemsize = unsupported_property('itemsize')
    ix = unsupported_property('ix')
    nbytes = unsupported_property('nbytes')
    ndim = unsupported_property('ndim')
    real = unsupported_property('real')
    strides = unsupported_property('strides')

    # Deprecated properties
    blocks = unsupported_property('blocks', deprecated=True)

    # Functions
    add = unsupported_function('add')
    add_prefix = unsupported_function('add_prefix')
    add_suffix = unsupported_function('add_suffix')
    agg = unsupported_function('agg')
    aggregate = unsupported_function('aggregate')
    align = unsupported_function('align')
    append = unsupported_function('append')
    argmax = unsupported_function('argmax')
    argmin = unsupported_function('argmin')
    argsort = unsupported_function('argsort')
    asfreq = unsupported_function('asfreq')
    asof = unsupported_function('asof')
    at_time = unsupported_function('at_time')
    autocorr = unsupported_function('autocorr')
    between = unsupported_function('between')
    between_time = unsupported_function('between_time')
    bfill = unsupported_function('bfill')
    bool = unsupported_function('bool')
    combine = unsupported_function('combine')
    combine_first = unsupported_function('combine_first')
    compound = unsupported_function('compound')
    copy = unsupported_function('copy')
    cov = unsupported_function('cov')
    cummax = unsupported_function('cummax')
    cummin = unsupported_function('cummin')
    cumprod = unsupported_function('cumprod')
    cumsum = unsupported_function('cumsum')
    diff = unsupported_function('diff')
    div = unsupported_function('div')
    divide = unsupported_function('divide')
    divmod = unsupported_function('divmod')
    dot = unsupported_function('dot')
    drop = unsupported_function('drop')
    drop_duplicates = unsupported_function('drop_duplicates')
    droplevel = unsupported_function('droplevel')
    duplicated = unsupported_function('duplicated')
    eq = unsupported_function('eq')
    equals = unsupported_function('equals')
    ewm = unsupported_function('ewm')
    expanding = unsupported_function('expanding')
    factorize = unsupported_function('factorize')
    ffill = unsupported_function('ffill')
    filter = unsupported_function('filter')
    first = unsupported_function('first')
    first_valid_index = unsupported_function('first_valid_index')
    floordiv = unsupported_function('floordiv')
    ge = unsupported_function('ge')
    get = unsupported_function('get')
    get_dtype_counts = unsupported_function('get_dtype_counts')
    get_values = unsupported_function('get_values')
    gt = unsupported_function('gt')
    hist = unsupported_function('hist')
    idxmax = unsupported_function('idxmax')
    idxmin = unsupported_function('idxmin')
    infer_objects = unsupported_function('infer_objects')
    interpolate = unsupported_function('interpolate')
    item = unsupported_function('item')
    items = unsupported_function('items')
    iteritems = unsupported_function('iteritems')
    keys = unsupported_function('keys')
    last = unsupported_function('last')
    last_valid_index = unsupported_function('last_valid_index')
    le = unsupported_function('le')
    lt = unsupported_function('lt')
    mad = unsupported_function('mad')
    map = unsupported_function('map')
    mask = unsupported_function('mask')
    median = unsupported_function('median')
    memory_usage = unsupported_function('memory_usage')
    mod = unsupported_function('mod')
    mode = unsupported_function('mode')
    mul = unsupported_function('mul')
    multiply = unsupported_function('multiply')
    ne = unsupported_function('ne')
    nonzero = unsupported_function('nonzero')
    nunique = unsupported_function('nunique')
    pct_change = unsupported_function('pct_change')
    pipe = unsupported_function('pipe')
    pop = unsupported_function('pop')
    pow = unsupported_function('pow')
    prod = unsupported_function('prod')
    product = unsupported_function('product')
    ptp = unsupported_function('ptp')
    put = unsupported_function('put')
    quantile = unsupported_function('quantile')
    radd = unsupported_function('radd')
    rank = unsupported_function('rank')
    ravel = unsupported_function('ravel')
    rdiv = unsupported_function('rdiv')
    rdivmod = unsupported_function('rdivmod')
    reindex = unsupported_function('reindex')
    reindex_like = unsupported_function('reindex_like')
    rename_axis = unsupported_function('rename_axis')
    reorder_levels = unsupported_function('reorder_levels')
    repeat = unsupported_function('repeat')
    replace = unsupported_function('replace')
    resample = unsupported_function('resample')
    rfloordiv = unsupported_function('rfloordiv')
    rmod = unsupported_function('rmod')
    rmul = unsupported_function('rmul')
    rolling = unsupported_function('rolling')
    round = unsupported_function('round')
    rpow = unsupported_function('rpow')
    rsub = unsupported_function('rsub')
    rtruediv = unsupported_function('rtruediv')
    searchsorted = unsupported_function('searchsorted')
    sem = unsupported_function('sem')
    set_axis = unsupported_function('set_axis')
    shift = unsupported_function('shift')
    slice_shift = unsupported_function('slice_shift')
    sort_index = unsupported_function('sort_index')
    squeeze = unsupported_function('squeeze')
    sub = unsupported_function('sub')
    subtract = unsupported_function('subtract')
    swapaxes = unsupported_function('swapaxes')
    swaplevel = unsupported_function('swaplevel')
    tail = unsupported_function('tail')
    take = unsupported_function('take')
    to_dense = unsupported_function('to_dense')
    to_frame = unsupported_function('to_frame')
    to_hdf = unsupported_function('to_hdf')
    to_msgpack = unsupported_function('to_msgpack')
    to_period = unsupported_function('to_period')
    to_pickle = unsupported_function('to_pickle')
    to_sparse = unsupported_function('to_sparse')
    to_sql = unsupported_function('to_sql')
    to_timestamp = unsupported_function('to_timestamp')
    to_xarray = unsupported_function('to_xarray')
    transform = unsupported_function('transform')
    transpose = unsupported_function('transpose')
    truediv = unsupported_function('truediv')
    truncate = unsupported_function('truncate')
    tshift = unsupported_function('tshift')
    tz_convert = unsupported_function('tz_convert')
    tz_localize = unsupported_function('tz_localize')
    unstack = unsupported_function('unstack')
    update = unsupported_function('update')
    view = unsupported_function('view')
    where = unsupported_function('where')
    xs = unsupported_function('xs')

    # Deprecated functions
    as_blocks = unsupported_function('as_blocks', deprecated=True)
    as_matrix = unsupported_function('as_matrix', deprecated=True)
    clip_lower = unsupported_function('clip_lower', deprecated=True)
    clip_upper = unsupported_function('clip_upper', deprecated=True)
    compress = unsupported_function('compress', deprecated=True)
    convert_objects = unsupported_function('convert_objects', deprecated=True)
    get_ftype_counts = unsupported_function('get_ftype_counts', deprecated=True)
    get_value = unsupported_function('get_value', deprecated=True)
    nonzero = unsupported_function('nonzero', deprecated=True)
    reindex_axis = unsupported_function('reindex_axis', deprecated=True)
    select = unsupported_function('select', deprecated=True)
    set_value = unsupported_function('set_value', deprecated=True)
    valid = unsupported_function('valid', deprecated=True)
