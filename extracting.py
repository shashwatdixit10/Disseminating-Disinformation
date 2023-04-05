from urllib.parse import urlparse
import phrases as ph
# import back as bc

def get_website_name(url):
    parsed_url = urlparse(url)
    if parsed_url.netloc.startswith("www."):
        return parsed_url.netloc[4:]
    
    elif parsed_url.netloc.startswith("cdn."):
        return parsed_url.netloc[4:]
    
    # elif parsed_url.netloc.startswith("en."):
    #     return parsed_url.netloc[4:]
    
    else:
        return parsed_url.netloc
    
def check_point(point):
    if point == 1 :
        # print("\nSensitive phrases present!! High Chances of a Misinformation")
        return "\nSensitive phrases present!! High Chances of a Misinformation"

    elif point == 2:
        # print("\nThe Information is not very sensitive")
        return "\nThe Information is not very sensitive"

    elif point==3:
        # print("\nThis is a Fact check condition!! May not be a fake news")
        return "\nThis is a Fact check condition!! May not be a fake news"

    else:
        # print("\nThe news dosent seem to be very sensitive!! May not be a Fake news")
        return "\nThe news dosent seem to be very sensitive!! "


def check_web(url):
    website_name = get_website_name(url)
    print(website_name)
    name = website_name.split(".")
    web = name[0].lower()

    # bc.bck(web)

    if web in open("sitename.csv").read():
        # print("The News is hosted on a Fake Website!! Very Likely A Fake News")
        return web+"\nThe News is hosted on a Fake Website!! Very Likely A Fake News" +check_point(ph.check_phrases(url))

    elif web in open("Authenticwebsites.csv").read():
        # print("The News is from a Trusted source!! Most probably a True News")
        return web +"\n"+ "\nThe News is from a Trusted source!! Most probably a True News"

    elif web in open("SuspiciousWebsites.csv").read():
        # print("Hosted on a suspicious Websites!! Likely a fake news")
        return web+"\nHosted on a suspicious Websites!! Likely a fake news" +check_point(ph.check_phrases(url))

    else:
        # print("May on May not be a fake News")
        
        return web + "\nMay on May not be a fake News" + check_point(ph.check_phrases(url))
        


