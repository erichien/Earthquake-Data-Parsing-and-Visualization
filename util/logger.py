from time import localtime, strftime


def logger(results, place):
    """
    Print out results
    """

    print
    
    for result in results:
        print result
        
    print '\n----------------------------------------------------------------\n'
    print 'Current time is {}'.format(strftime('%Y-%m-%d %H:%M:%S%z', localtime()))
    print 'There were {} earthquakes in {} in the past month\n'.format(len(results), place)
