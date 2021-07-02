"""
 	@author
 		Domnan Diretnan
 		Artificial Intelligence Enthusiast & Software Engineer.
 		Email: diretnandomnan@gmail.com
 		Github: https://github.com/deven96
 		GitLab: https://gitlab.com/Deven96

        Mmadu Manasseh
 		Email: mmadumanasseh@gmail.com
 		Github: https://github.com/mensaah
 		GitLab: https://gitlab.com/mensaah

 	@project
 		@create date 2019-02-01 22:15:44
 		@modify date 2019-02-01 22:15:44

	@license
		MIT License
		Copyright (c) 2018. Domnan Diretnan. All rights reserved

"""

# Allow import using `search_engine_parser.engines`
from search_engine_parser.core import engines

# Support for older versions of imports
# DEPRECATION_WARNING: These imports will be removed in later versions
from search_engine_parser.core.engines.aol import Search as AolSearch
from search_engine_parser.core.engines.ask import Search as AskSearch
from search_engine_parser.core.engines.duckduckgo import Search as DuckDuckGoSearch
from search_engine_parser.core.engines.github import Search as GithubSearch
from search_engine_parser.core.engines.google import Search as GoogleSearch
from search_engine_parser.core.engines.myanimelist import Search as AnimeSearch
from search_engine_parser.core.engines.yahoo import Search as YahooSearch

name = "search-engine-parser"  # pylint: disable=invalid-name
__version__ = "0.6.2"
