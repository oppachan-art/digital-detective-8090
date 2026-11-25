# Mission 7 — How computers communicate

## 2. Task / objective
Explain network concepts, observe a DNS lookup and connectivity test, and describe opening a website.

## 3. Work completed
### Network concepts
| Concept | Explanation | Example |
|---|---|---|
| LAN | Network covering a small local area | Home or lab network |
| MAN | Network spanning a city or large campus | City-wide municipal network |
| WAN | Network covering large geographic areas | The Internet |
| DNS | Finds network address records associated with domain names | Resolving a domain before connecting |
| Router | Forwards packets between networks | Home router linking local devices to an ISP |
| Protocol | Agreed rules for communication | HTTPS uses HTTP over TLS |
| Packet switching | Sends data in packets that may travel across shared networks | Internet traffic |
| Client-server | Client requests a service; server responds | Browser requests a web page |

A connectivity test checks whether a destination responds over the network; its result depends on the destination, firewall and network. A DNS lookup asks a resolver for records such as IP addresses associated with a domain. DNS lets a person use a domain name while network connections use address information.

### What happens when you open a website
1. You enter a URL in the browser; it identifies the domain and requested resource.
2. The browser or operating system checks available DNS information and asks a DNS resolver for the domain's address if needed.
3. The computer sends packets through the local network and router toward the server, using the relevant network protocols.
4. The browser establishes a secure connection when HTTPS is used.
5. The browser sends an HTTP request; the server processes it and returns a response.
6. The browser interprets the response and displays the page; additional files may require more requests.

Observed test and lookup: Looked up `example.com`: DNS resolution succeeded. HTTPS request succeeded with status 200. Resolved addresses and local network details were omitted.

## 4. Commands / tools used
Used Python socket DNS resolution and an HTTPS request to `https://example.com`; DNS returned address records and the HTTPS response was successful (200). Address values were not recorded.

## 5. My understanding
DNS helps translate memorable names into network records. Routers forward packets, and client-server protocols let the browser request resources and receive a response.

## 6. Difficulties faced
No major difficulties; the public example domain resolved and responded over HTTPS.

## 7. How I resolved them
Repeated the lookup and HTTPS request for the same public domain; omitted all address values and device/network details.

## 8. Evidence / files
Privacy-safe notes or redacted screenshot, if used.

## 9. Commit details
Suggested message: `Explain networking concepts and website communication`. Commit hash: https://github.com/oppachan-art/digital-detective-8090 (see Git history).
