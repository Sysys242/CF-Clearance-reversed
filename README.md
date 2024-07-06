# CF-Clearance-reversed
Reverse engineer of cf clearance ( for discord )

-> based on [CloudflareX](https://github.com/Sysys242/CloudFlareX) ( outdated )

---

## How to use
- Install nodejs and python
- run in a cmd in the folder: `pip install tls_client` & `npm i`
- Then run the server.js file using `node server.js`
- And finally, in an other cmd, use the get_cf_clearance python file using: `python get_cf_clearance.py`

## How does it work
- Cloudflare script is added to the req if cf_clearance not in cookies. This script call an [other](https://discord.com/cdn-cgi/challenge-platform/scripts/jsd/main.js) with "r" a unique id for each task.
- The script will get the fingerprint and encrypt it using the function uETzEaKEEO in server.js.
- The encryption is made using a unique key ( named k in the python code )
- An other value is required called S in python code, parsed by splitting the text by 0. 0. two time.
- The task is sent to `https://discord.com/cdn-cgi/challenge-platform/h/g/jsd/r/{r}` where {r} is the unique task id.
