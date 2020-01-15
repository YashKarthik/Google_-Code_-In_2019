from linkEXT import LinkExtractor, Vuln
from termcolor import colored, cprint

def main():
    cprint("Enter the complete url of the website: ", 'yellow')
    url = input("url:  ")
    if Vuln(url):
        cprint("The website is vulnerable at", 'red', url)
    else:
        Links = LinkExtractor().GetAllLinks(url)
        Direcs = LinkExtractor().DirectoryExtractor(Links)
        print('-'*60)
        cprint('All Links Extracted.', 'green')
        print('-'*60)
        cprint("Checking vulnerablities.", 'yellow')
        safe = True 
        for direc in Direcs:
            cprint(f"Checking if the site is vulnerable at {direc}", 'magenta')
            if Vuln(direc):
                safe = False
                cprint(f"The website is vulnerable at: {direc}", 'red')
        if safe:
            cprint("The website is secure (Atleast of directory listing vulnerabilities).", 'green')

if __name__ == "__main__":
    main()