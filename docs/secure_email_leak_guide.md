
# OSINT Tutorial: Creating a Secure Email Account and Forums for Leaks

This enhanced tutorial outlines how to create a secure, anonymous email account for OSINT investigations or whistleblowing, and identifies platforms where digital content (including leaks) is often shared. The goal is operational security (OpSec), privacy, and resilience against doxxing or attribution.

---

## Step 1: Choose a Privacy-Focused Email Provider

Use a provider that offers end-to-end encryption, strong privacy policies, and does not require personal information.

### Recommended Providers:

- **ProtonMail** ([protonmail.com](https://protonmail.com))  
  Based in Switzerland, ProtonMail offers end-to-end encryption and anonymous signup. Use the Tor version for enhanced anonymity: [protonmail.com/tor](https://protonmail.com/tor).

- **Tutanota** ([tutanota.com](https://tutanota.com))  
  Encrypted email and calendar services. Allows anonymous signup without a phone number. Also offers an Onion address.

- **StartMail** ([startmail.com](https://startmail.com))  
  Based in the Netherlands. Offers unlimited aliases, strong encryption, and no logging.

- **Mailbox.org** ([mailbox.org](https://mailbox.org))  
  Privacy-first German provider supporting PGP encryption and pseudonymous usage.

- **CTemplar** (formerly active, now archived – verify availability before use)

### Extra Tool:
- **SimpleLogin** ([simplelogin.io](https://simplelogin.io)) or **AnonAddy** ([anonaddy.com](https://anonaddy.com))  
  Create anonymous aliases to forward to your secure inbox.

---

## Step 2: Mask Your Identity During Account Creation

Even with a secure email provider, you must ensure your network and hardware setup is not leaking identity.

### Recommended Methods:
- **VPN**: Use a no-log provider (e.g., Mullvad, IVPN, ProtonVPN). Prefer cash or crypto payments for higher anonymity.
- **Tor Browser**: Route traffic through the Tor network. Launch your email provider's .onion URL where available.
- **Tails OS**: A live OS focused on anonymity and privacy. Automatically routes through Tor. Useful for high-risk whistleblowing or sensitive OSINT.
- **Browser Isolation**: Use Firefox with hardened privacy settings or a browser container (e.g., Firefox Multi-Account Containers).

---

## Step 3: Create the Email Account Securely

Follow these principles during sign-up:

- Use a **non-identifying username**. Avoid handles you've used elsewhere.
- Do **not reuse passwords**. Use a password manager like Bitwarden or KeePassXC.
- Avoid **real information**: fake names, birthdates, etc.
- **Never link a phone number** unless using a temporary/burner solution.

### Temporary Number Services (Use Cautiously):
- [Receive SMS Online](https://www.receive-sms-online.info)
- [AnonymSMS](https://anonymsms.com)
- [FreePhoneNum.com](https://freephonenum.com)
- [Receive-smss.com](https://receive-smss.com)
- **Alternative**: Use apps like TextNow or Hushed (with VPN + dummy info).

**⚠️ Note**: Avoid using these numbers for accounts where long-term access is required. Numbers may be recycled.

---

## Step 4: Maintain Ongoing Operational Security (OpSec)

- **Dedicated Browsers or VMs**: Run a separate browser profile or VM for all activity tied to your anonymous email.
- **Do Not Cross-Link**: Don’t log into personal accounts, social media, or shopping sites using the same browser/IP/session.
- **Email Aliases for Separation**: Use SimpleLogin or AnonAddy to create aliases for different purposes (leaks, monitoring, registration).
- **Turn Off JavaScript** (where possible): Consider using NoScript or JS blockers in Tor/Firefox for leak submission.
- **Beware of Email Headers**: Avoid sending emails directly to recipients. Use pastebin-style services or public-key encrypted messaging instead.

---

## Step 5: Platforms Used for Digital Content Sharing & Leaks

These forums/platforms often host or share modded content, game repacks, and occasionally leaks. Monitor for investigative purposes.

### Forums & Leak Sharing Platforms:

- **VeryLeak's** ([veryleaks.is](https://veryleaks.is))  
  A platform known for sharing software, exploits, and leaked documents.

- **4chan /r9k/ or /g/** ([4chan.org](https://www.4chan.org))  
  Anonymous boards where leaks often appear before mainstream attention.

- **Exploit.in / BreachForums** *(verify legal status and avoid posting)*

- **Dread Forum** (Tor-only Reddit-style forum, often used by whistleblowers and hackers)

---

### Game & Mod Content Platforms (often used for distribution):

- **NexusMods** ([nexusmods.com](https://www.nexusmods.com))  
  Hosting for over 700K+ game mods, sometimes includes illicit or grey-market uploads.

- **SteamCommunity** ([steamcommunity.com](https://steamcommunity.com))  
  Used for sharing guides, mods, and announcements. Leaks may be shared in discussions.

- **FitGirl Repacks** ([fitgirl-repacks.site](https://fitgirl-repacks.site))  
  Offers highly compressed versions of games, popular in grey-market redistribution.

- **SkidrowReloaded** ([skidrowreloaded.com](https://skidrowreloaded.com))  
  Hosts cracks, repacks, and modded game content.

- **Reddit Communities**: e.g., r/Piracy, r/OSINT, r/PrivacyToolsIO *(watch, don’t post)*

---

## Final Tips for Leak-Related Email Use

- Don’t use HTML email format. Stick with plain text.
- Never send attachments unless pre-scanned and anonymized (e.g., stripped EXIF, zipped with AES encryption).
- If submitting leaks, use secure pastebins (e.g., [0bin.net](https://0bin.net), [paste.debian.net](https://paste.debian.net)) with auto-destruct.
- For long-term secure communication, exchange PGP keys.

---

## Tools Summary

| Purpose | Tool |
|--------|------|
| Anonymous Email | ProtonMail, Tutanota, StartMail |
| Email Alias | SimpleLogin, AnonAddy |
| VPN | Mullvad, ProtonVPN, IVPN |
| Network Obfuscation | Tor Browser, Tails OS |
| Temporary SMS | Receive-smss.com, AnonymSMS |
| Password Management | KeePassXC, Bitwarden |
| Secure Pastebins | 0bin, PrivateBin, Paste.debian.net |

Stay safe, stay legal, and always verify platforms before interacting.
