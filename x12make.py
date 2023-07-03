import logging
import configparser as cp
from x12testbed import testbed

db_config_file = 'D:\Tools\Python\Jobaids\\x12make\\x12make.parms'

def setuplogger(config):

    logfile = config['logging']['logfile']    

    FORMAT = '%(asctime)s -%(name)s.%(module)s - %(filename)s - %(funcName)s - %(message)s'
    
    # set up logging to log file
    logging.basicConfig(level=logging.INFO,
                        format=FORMAT,
                        datefmt='%y%m%d %H:%M',
                        filename=logfile,
                        filemode='w')

    # define a Handler which writes messages to sys.stderr
    console = logging.StreamHandler()
    console.setLevel(logging.ERROR)

    # set a format which is simpler for console use
    formatter = logging.Formatter('%(name)s: %(levelname)s %(message)s')

    # tell the handler to use this format
    console.setFormatter(formatter)

    # add the handler to the root logger
    logging.getLogger('').addHandler(console)

def main():

    config = cp.ConfigParser(allow_no_value=True)    
    config.read(db_config_file)   

    #setup logger
    setuplogger(config)

    tbed = testbed(config)
    tbed.load_data(config)


    return

if __name__ == '__main__':
    try:        
        main()
    except Exception as error:
        logging.error(str(error))
    quit()    