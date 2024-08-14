from binascii import *
import logging

class get_MitM(object):
    """
    The RelayMiddleman class serves as a base from which a user might derive
    their own relay middle man class.  This base class implements the simplest
    Man-in-the-Middle:  the NoOp.
    """

    payload = ""

    def handleInPDU(self, inPDU: bytes):
        """
        This method is called on each PDU that is fed into the realy (vdpu -> vicc).
        It may be overwritten to modify the packages send from the terminal to the 
        real smart card.
        """
        
        return inPDU

    def handleOutPDU(self, outPDU: bytes):
        """
        This method is called on each PDU that is produced by the relay (vicc -> vdpu).
        It may be overwritten to modify the packages send from the real smart card to the
        terminal.
        """
        outPDU_hex = ''.join('{:02x}'.format(x) for x in outPDU)
        if outPDU_hex == "6f2f840e325041592e5359532e4444463031a51dbf0c1a61184f07a0000000041010500a4d4153544552434152448701019000":
            logging.info("PPSE response found, sending payload...")
            #outPDU = list(unhexlify(self.payload))

        return outPDU
