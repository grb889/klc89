# **Unique Search Operators in Bing and Yandex (Not Available in Google)**

---

## **🔹 Bing Operators Not Available on Google**

* (Plus Symbol): Forces Bing to include a word that would normally be ignored as a stop word.  
   Example: `search +the term`

ip: : Searches for sites hosted on a specific IP address.  
 Example: `ip:192.168.1.1`

feed: or hasfeed: : Finds web pages that contain an RSS feed.  
 Example: `site:example.com hasfeed:`, `feed:news`

language: : Restricts results by language directly from the search bar.  
 Example: `language:en "search operators"`

loc: or location: : Filters results by a specific country or region code.  
 Example: `loc:gb "football"`

prefer: : Tells Bing to prefer results that contain a certain word (not mandatory).  
 Example: `AI prefer:ethics`

contains: : Finds pages that contain a specific file type (different from Google’s `filetype:`).  
 Example: `report contains:pdf`

url: : Matches a full URL exactly.  
 Example: `url:https://www.example.com/page.html`

**linkfromdomain:** Finds all pages that a given domain *links out to* (outbound links).  
 Example: `linkfromdomain:example.com -site:example.com`

**linkdomain:** Finds all pages that *link to* a given domain (inbound backlinks).  
 Example: `linkdomain:example.com`

---

## **🔹 Yandex Operators Not Available on Google or Bing**

\*\* (Double Asterisk): Wildcard for two consecutive words.  
 Example: `best ** game`

/number (Proximity Search): Ensures words are within a certain distance.  
 Example: `"computer" /5 "network"`

cat: : Restricts results to a category in the Yandex Catalog.  
 Example: `cat:travel "hotels in London"`

url: : Searches for a specific full URL.  
 Example: `url:https://www.example.com/page.html`

rhost: : Searches pages hosted on an exact registered host (ignores subdomains).  
 Example: `rhost:example.com "login"`

mime: : Searches by MIME type.  
 Example: `report mime:application/pdf`

date: : Filters by publication date directly in query.  
 Example: `"cyber attack" date:2025`

storage: : Restricts results to certain storage/hosting services.  
 Example: `"project files" storage:disk`

