import logging
logging.basicConfig(filename="pdf.log",level=logging.ERROR,format="%(asctime)s %(levelname)s %(message)s",filemode='W')
logger=logging.getLogger()
logging.info("importing gui")
#import main
logging.info("gui closed")