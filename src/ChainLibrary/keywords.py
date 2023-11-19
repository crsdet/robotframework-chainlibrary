from robot.errors import DataError
from robot.libraries.BuiltIn import BuiltIn
from robot.utils import is_string


class ChainKeywords:

    def __init__(self, separator: str = 'AND', replace: str = '%') -> None:
        self._built_in = BuiltIn()
        self._separator = separator
        self._replace = replace

    def chain_arguments(self, *keywords):
        """Executes all the given arguments over the same keyword.

        This keyword takes the specified keyword and runs it with the first
        arguments, then runs the keyword with the arguments defined after the
        first AND separator and so on. The % replaces an argument with the last
        returned value that is not none that can be used in the following keyword.

        Both separator and replace string can be customized when importing the library.

        Example:
        | ${str} | `Chain Arguments` | `Replace String` |
        | ... Hello, world! | ! | . |
        | ...  AND |
        | ...  % | Hello | Hi |
        | ...  AND |
        | ...  % | world | John Doe |
        =>
        | ${str} = Hi, John Doe.

        The last value returned by a keyword that is not None is returned at the
        end of the chain.
        """
        if not keywords or not is_string(keywords[0]):
            raise RuntimeError('Keyword name must be a string.')
        return self._run_chained_arguments(self._split_chain(keywords))

    def chain_keywords(self, *keywords):
        """Executes all the given keywords in a chain where the returned value
        of a keyword is an argument for the following one.

        This keyword splits the given keywords using the AND separator, then
        execute the first keyword and saves its returned value on a % variable
        which is replaced in the second keyword and so on.

        Both separator and replace string can be customized when importing the library.

        Example:
        | ${str} | `Chain Keywords` | `Name` |
        | ...  AND |
        | ...  `Catenate` | SEPARATOR=${SPACE} | Hi, | %. |
        | ...  AND |
        | ...  `Log` |
        =>
        | ${str} = Hi, John Doe.

        The last value returned by a keyword that is not None is returned at the
        end of the chain.
        """
        if not keywords or not is_string(keywords[0]):
            raise RuntimeError('Keyword name must be a string.')
        return self._run_chained_keywords(self._split_chain(keywords))

    def _run_chained_arguments(self, keywords: list):
        args = [None]
        keyword = keywords[0].pop(0)
        for kw in keywords:
            if any(args):
                kw = self._replace_kw(kw, args[-1])
            if arg := self._built_in.run_keyword(keyword, *kw):
                args.append(arg)
        return  args[-1]

    def _run_chained_keywords(self, keywords: list):
        args = [None]
        for kw in keywords:
            if any(args):
                kw = self._replace_kw(kw, args[-1], True)
            if arg := self._built_in.run_keyword(*kw):
                args.append(arg)
        return args[-1]

    def _split_chain(self, keywords: list) -> list:
        replace_list = []
        tmp = []
        for i, kw in enumerate(keywords):
            if self._is_separator(kw):
                if i in (0, len(keywords) - 1) or self._is_separator(keywords[i + 1]):
                    raise DataError(f'{self._separator.upper()} must have a keyword before and after.')
                else:
                    replace_list.append(tmp)
                    tmp = []
            else:
                tmp.append(kw)
        replace_list.append(tmp)
        return replace_list

    def _replace_kw(self, keywords: list, arg, append: bool = False):
        replace_list = []
        replace = None
        for kw in keywords:
            if self._replace in kw:
                replace = kw.replace(self._replace, str(arg))
                replace_list.append(replace)
            else:
                replace_list.append(kw)
        if append and not replace:
            replace_list.append(arg)
        return replace_list

    def _is_separator(self, arg) -> bool:
        return is_string(arg) and arg.upper() == self._separator.upper()
