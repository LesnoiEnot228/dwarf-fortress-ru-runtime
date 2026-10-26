# Translation worker

This directory is reserved for the asynchronous translation layer. It is not implemented yet.

Planned responsibilities:
- dictionary and rule lookup must be handled before machine translation;
- provider work must run outside the game's rendering thread;
- duplicate in-flight phrases should be coalesced;
- results should be cached with schema/provider versions;
- providers must be optional and disabled by default when they send text externally;
- provider errors must fall back to the original English string without affecting game stability.
