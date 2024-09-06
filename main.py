import argparse
import sys
import re
import rex_prox

def main():
    parser = argparse.ArgumentParser(description='Check-Proxy-rex tools CLI tool.');
    parser.add_argument('--version', action='version', version='rex-scan-proxy 1.0')
    parser.add_argument('--scan',nargs='?' , type=str,default=None, help='you can use --scan config or --scan proxy')
    parser.add_argument('-p',nargs='?' , type=str,default=None, help='you can use example : -p 127.0.0.1')
    parser.add_argument('--dir',nargs='?' , type=str,default=None, help='you can use example : ./file/text.txt')
    args = parser.parse_args();
    # check main argument 
    if args.scan == "config" or args.scan == "proxy":
        if(args.scan == "config"):
            if args.dir is not None:
               file_config = rex_prox.read_file(args.dir);
            else:
                parser.print_help();
                sys.exit(1);

        if(args.scan == 'proxy'):
            print('Running Proxy')
    else:
        parser.print_help();
        sys.exit(1);
        


if __name__ == "__main__":
    main()