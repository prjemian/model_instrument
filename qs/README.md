# Support for the Bluesky Queueserver.

File [`qs-config.yml`](../qs/qs-config.yml) contains all configuration of the QS
host process. See the
[documentation](https://blueskyproject.io/bluesky-queueserver/manager_config.html)
for more details of the configuration.

The QS host process writes files into this directory. This directory can be
relocated. However, it should not be moved into the instrument package since
that might be installed into a read-only directory.

## shell script

A [shell script](./qs_host.sh) is used to start the QS host process. Typically,
it is run in the background: `./qs/qs_host.sh restart`.  This command looks for
a running QS host process.  If found, that process is stopped.  Then, a new QS
host process is started in a
[screen](https://www.gnu.org/software/screen/manual/screen.html) session.

```bash
(bstest) $ ./qs/qs_host.sh help
Usage: qs_host.sh {start|stop|restart|status|checkup|console|run} [NAME]

    COMMANDS
        console   attach to process console if process is running in screen
        checkup   check that process is running, restart if not
        restart   restart process
        run       run process in console (not screen)
        start     start process
        status    report if process is running
        stop      stop process

    OPTIONAL TERMS
        NAME      name of process (default: bluesky_queueserver-)
```

Alternatively, run the QS host's startup comand directly within the `qs/`
subdirectory.

```bash
cd .qs
start-re-manager --config=./qs-config.yml
```
