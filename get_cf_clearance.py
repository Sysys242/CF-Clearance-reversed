import tls_client

def printv(key, val):
    print(f"{key}: {val}")

class Cloudflare:
    def __init__(self) -> None:
        self.session = tls_client.Session(
            client_identifier="chrome_120",
            random_tls_extension_order=True
        )
    
    def CFCVParams(self) -> str:
        response = self.session.get('https://discord.com/').text
        r = response.split("r:'")[1].split("'")[0]
        return r

    def getInvisible(self) -> dict:
        response = self.session.get(
            'https://discord.com/cdn-cgi/challenge-platform/scripts/jsd/main.js',
            allow_redirects=True
        )
        s = "0." + response.text.split("0.")[1]
        s = s[:73]
        data = response.text.split('function a(ah){return ah=\'')[1].split("'.split(','),")[0]
        k = next(K for K in data.split(",") if len(K) == 65)

        return [k, s]
    
    def get_cf_clearance(self, invisible:dict, r:str) -> str:
        wp = self.session.post(
            'http://127.0.0.1:3000/wp',
            json={
                "pass": invisible[0]
            }
        ).text

        response = self.session.post(
            f'https://discord.com/cdn-cgi/challenge-platform/h/g/jsd/r/{r}',
            json={
                "S": invisible[1],
                "Wp": wp
            }
        )
        return response.cookies['cf_clearance']

if __name__ == "__main__":
    cloudflare = Cloudflare()
    CFCV = cloudflare.CFCVParams()
    printv("R", CFCV)
    invisble = cloudflare.getInvisible()
    printv("K", invisble[0])
    printv("S", invisble[1])
    cf_clearance = cloudflare.get_cf_clearance(invisble, CFCV)
    printv("cf_clearance", cf_clearance)
    if len(cf_clearance) == 149:
        printv('Pass', True)