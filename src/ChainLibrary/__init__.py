from .keywords import ChainKeywords

class ChainLibrary(ChainKeywords):
    """``ChainLibrary`` is a Robot Framework library for running keywords in a chain.

    The following keywords are included:

    - `Chain Arguments`
    - `Chain Keywords`
    """

    ROBOT_LIBRARY_SCOPE = 'GLOBAL'
