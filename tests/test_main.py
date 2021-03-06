from MesoPy import Meso, MesoPyError
from nose.tools import *


# Basic Function Tests
def testvarlistfunc():
    m = Meso(api_token='3428e1e281164762870915d2ae6781b4')
    var_list = m.variable_list()
    ok_(var_list)


def teststationsfunc():
    m = Meso(api_token='3428e1e281164762870915d2ae6781b4')
    stations = m.station_list(state='CO', county='Larimer')
    ok_('KFNL' == stations['STATION'][1]['STID'])


def testtimeseriesfunc():
    m = Meso(api_token='3428e1e281164762870915d2ae6781b4')
    timeseries = m.timeseries_obs(stid='kfnl', start='201504261800', end='201504262300')
    ok_(timeseries)


def testclimatologyfunc():
    m = Meso(api_token='3428e1e281164762870915d2ae6781b4')
    climatology = m.climatology_obs(stid='kden', startclim='04260000', endclim='04270000', units='precip|in')
    ok_(climatology)


def testprecipfunc():
    m = Meso(api_token='3428e1e281164762870915d2ae6781b4')
    precip = m.precipitation_obs(stid='kfnl', start='201504261800', end='201504271200', units='precip|in')
    ok_(precip)


# Miscellaneous Tests
def testvarexists():
    m = Meso(api_token='3428e1e281164762870915d2ae6781b4')
    var_list = m.variable_list()
    ok_('relative_humidity' in var_list['VARIABLES'])


def testlateststrlist():
    m = Meso(api_token='3428e1e281164762870915d2ae6781b4')
    latest = m.latest_obs(stid=['kfnl', 'kden', 'ksdf'])
    eq_(len(latest['STATION']), 3)


# Error Handling
@raises(MesoPyError)
def testbadurlstring():
    m = Meso(api_token='3428e1e281164762870915d2ae6781b4')
    latest = m.latest_obs(stid='')
    print(latest)


@raises(MesoPyError)
def testauth():
    m = Meso(api_token='3030')
    m.latest_obs(stid=['kfnl', 'kden', 'ksdf'])


@raises(MesoPyError)
def testgeoparms():
    m = Meso(api_token='3428e1e281164762870915d2ae6781b4')
    m.precipitation_obs(start='201504261800', end='201504271200', units='precip|in')