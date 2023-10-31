import sys

from converter.app.cli import CLI

if __name__ == "__main__":
    try:
        cli = CLI()
        cli.run()
    except KeyboardInterrupt:
        sys.exit('Stop processing')
    except ModuleNotFoundError:
        sys.exit('Format not exist or is invalid')
    except OSError:
        sys.exit('No input data in the standard input')
