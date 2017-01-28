from couchpotato.core.logger import CPLog
from couchpotato.core.media._base.providers.torrent.torrent9 import Base
from couchpotato.core.media.movie.providers.base import MovieProvider

log = CPLog(__name__)

autoload = 'torrent9'


class torrent9(MovieProvider, Base):
    pass
