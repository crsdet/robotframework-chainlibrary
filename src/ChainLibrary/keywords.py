from robot.errors import DataError
from robot.libraries.BuiltIn import BuiltIn
from robot.utils import is_string


class ChainKeywords:

    def __init__(self, separator: str = 'AND', replace: str = '$_') -> None:
        self._built_in = BuiltIn()
        self._separator = separator
        self._replace = replace

    def chain_keywords(self, *keywords):
        """Executes all the given keywords in a chain where the returned value
        of a keyword is an argument for the following one.

        This keyword splits the given keywords using the AND separator, then
        execute the first keyword and saves the returned value, and replaces it
        if $_ is present on an argument of the next keyword and so on. If $_ is
        not present in the next keyword, the last returned value is used as the
        last argument of the following keyword.

        Both separator and replace string can be customized when importing the library.

        Example:
        | ${str} | `Chain Keywords` |
        | ... | `Name` |
        | ... | AND |
        | ... | `Catenate` | SEPARATOR=${SPACE} | Hi, | $_. |
        | ... | AND |
        | ... | `Log` |
        =>
        | ${str} = Hi, John Doe.

        The last value returned by a keyword that is not None is returned at the
        end of the chain.
        """
        return self._run_chain(self._split_chain(keywords))

    def _run_chain(self, iterable: list):
        last = None
        for kw in iterable:
            if not kw or not is_string(kw[0]):
                raise RuntimeError('Keyword name must be a string.')
            if last:
                kw = self._replace_kw(kw, last)
            if arg := self._built_in.run_keyword(*kw):
                last = arg
        return last

    def _split_chain(self, iterable: list) -> list:
        keywords = []
        tmp = []
        for i, kw in enumerate(iterable):
            if self._is_separator(kw):
                if not tmp or i == len(iterable) - 1:
                    raise DataError(f'{self._separator} must have a keyword before and after.')
                keywords.append(tmp)
                tmp = []
            else:
                tmp.append(kw)
        keywords.append(tmp)
        return keywords

    def _replace_kw(self, iterable: list, arg):
        replace = False
        for i, kw in enumerate(iterable):
            if replace := self._replace in kw:
                iterable[i] = kw.replace(self._replace, str(arg))
        if not replace:
            iterable.append(arg)
        return iterable

    def _is_separator(self, arg) -> bool:
        return is_string(arg) and arg.upper() == self._separator.upper()
