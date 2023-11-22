from robot.libraries.BuiltIn import register_run_keyword

from .keywords import ChainKeywords

class ChainLibrary(ChainKeywords):
    """``ChainLibrary`` is a Robot Framework library for running keywords in a chain.

    The following keywords are included:

    - `Chain Keywords`
    """

    ROBOT_LIBRARY_SCOPE = 'GLOBAL'

register_run_keyword('ChainLibrary', 'chain_keywords', deprecation_warning=False)
