[![progress-banner](https://backend.codecrafters.io/progress/redis/7a867735-dc37-4ad3-8c18-d206904adf30)](https://app.codecrafters.io/users/8885os?r=2qF)

### redis-codecrafters-python

# Building my own version of a Redis Database

## Current Version

- Made a TCP server that can handle 'ECHO', 'PING', 'SET', 'GET' commands.
- Can handle concurrent clients via the using the asyncio event loop instead of having to create too many threads.
- Has an expiry function to delete values of certain keys after a certain amount of time provided by the client.
- RDB files can now be read and keys can be returned

## Future Versions

- RDB Persistence - Add persistence support to my Redis implementation. - still needs to return other values as well as key
- Replication - I will add support for Replication to my Redis implementation. Along the way I will learn about how Redis's leader-follower replication works, the PSYNC command and more.
- Streams - I will add support for the Stream data type to my Redis implementation. Along the way I will learn about commands like XADD, XRANGE and more.
- Transactions - I will add support for Transactions to my Redis implementation. Along the way, I will learn about the MULTI, EXEC, and DISCARD commands, as well as how Redis handles transactions atomically.
